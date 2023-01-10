from datetime import timedelta
import json

# needed for any cluster connection
from couchbase.auth import PasswordAuthenticator
from couchbase.cluster import Cluster
from tqdm import tqdm
import pathlib

# needed for options -- cluster, timeout, SQL++ (N1QL) query, etc.
from couchbase.options import ClusterOptions, ClusterTimeoutOptions, QueryOptions
from queries import PLAYGROUND_SQL_QUERIES, PLAYGROUND_SDK_QUERIES, N1QL_REF_QUERIES
from dotenv import load_dotenv
import os
from utils import query_docs

if __name__ == "__main__":
    load_dotenv()

    # Read cluster info from environment
    conn_str = os.getenv("DB_CONN_STR")
    username = os.getenv("DB_USER")
    password = os.getenv("DB_PWD")
    bucket_name = os.getenv("DB_BUCKET")
    data_directory = os.getenv("DATA_DIR")

    required_docs = set()
    # Connect options - authentication
    auth = PasswordAuthenticator(username, password)

    # get a reference to our cluster
    options = ClusterOptions(auth)
    # Sets a pre-configured profile called "wan_development" to help avoid latency issues
    # when accessing Capella from a different Wide Area Network
    # or Availability Zone(e.g. your laptop).
    options.apply_profile("wan_development")
    cluster = Cluster(conn_str, ClusterOptions(auth))

    # Wait until the cluster is ready for use.
    cluster.wait_until_ready(timedelta(seconds=5))

    # get a reference to our bucket
    cb = cluster.bucket(bucket_name)
    cb_scope = cb.scope("inventory")

    # all queries to be satisfied
    QUERIES = PLAYGROUND_SQL_QUERIES + PLAYGROUND_SDK_QUERIES + N1QL_REF_QUERIES

    print("Identifying Required Documents")
    for example in tqdm(QUERIES):
        example.docs = query_docs(cb_scope, example.query)
        example.no_docs = len(example.docs)
        if example.no_docs < 1:
            print(f"Warning: Query {example.id} did not yield any documents")
        required_docs.update(example.docs)
    print(f"Identified {len(required_docs)} docs to be exported")

# print(required_docs, len(required_docs))
airport_docs = [a for a in required_docs if a.startswith("airport_")]
airline_docs = [a for a in required_docs if a.startswith("airline_")]
hotel_docs = [a for a in required_docs if a.startswith("hotel_")]
route_docs = [a for a in required_docs if a.startswith("route_")]
landmark_docs = [a for a in required_docs if a.startswith("landmark_")]

print("Exporting documents / collection")

EXPORT_MATRIX = [
    {
        "collection": "airline",
        "prefix": "inventory.airline",
        "doc_ids": airline_docs,
    },
    {
        "collection": "airport",
        "prefix": "inventory.airport",
        "doc_ids": airport_docs,
    },
    {"collection": "hotel", "prefix": "inventory.hotel", "doc_ids": hotel_docs},
    {
        "collection": "landmark",
        "prefix": "inventory.landmark",
        "doc_ids": landmark_docs,
    },
    {"collection": "route", "prefix": "inventory.route", "doc_ids": route_docs},
]

for export in EXPORT_MATRIX:
    collection = export["collection"]
    docs_location = export["prefix"]
    doc_ids = export["doc_ids"]

    collection_export = {}

    print(f"Exporting {collection}")
    for doc_id in tqdm(doc_ids):
        try:
            with open(
                pathlib.Path(data_directory, f"{docs_location}.{doc_id}.json")
            ) as f:
                doc = json.load(f)
                collection_export[doc_id] = doc
        except Exception as e:
            print(f"Exception while loading document {f}", e)

    with open(pathlib.Path(pathlib.Path.cwd(), f"{collection}.json"), "w") as out_file:
        json.dump(collection_export, out_file)
