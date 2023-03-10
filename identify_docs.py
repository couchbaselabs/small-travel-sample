from datetime import timedelta

# needed for any cluster connection
from couchbase.auth import PasswordAuthenticator
from couchbase.cluster import Cluster
from query import Query
from tqdm import tqdm
import pathlib
import shutil

# needed for options -- cluster, timeout, SQL++ (N1QL) query, etc.
from couchbase.options import ClusterOptions
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
    destination_directory = pathlib.Path(os.getcwd(), "smalltravelsample/docs")

    # Delete existing files from the destination_directory
    print("Deleting existing files in the output folder")
    for file_to_delete in destination_directory.glob("*.json"):
        try:
            file_to_delete.unlink()
        except Exception as e:
            print(f"Failed to delete file {file_to_delete}", e)

    # Deleting archive if it exists
    destination_archive = pathlib.Path(destination_directory, "smalltravelsample.zip")
    if os.path.exists(destination_archive):
        os.unlink(destination_archive)

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

    # Export users from tenant_agent_01
    tenant_scope = cb.scope("tenant_agent_01")
    CREATE_INDEX_QUERY = Query(
        id="CREATE_INDEX_USERS", query="""CREATE PRIMARY INDEX on users"""
    )
    try:
        CREATE_INDEX_QUERY.docs = query_docs(tenant_scope, CREATE_INDEX_QUERY.query)
    except Exception as e:
        print(f"Error while creating primary index: ", e)

    # all queries to be satisfied
    QUERIES = PLAYGROUND_SQL_QUERIES + PLAYGROUND_SDK_QUERIES + N1QL_REF_QUERIES

    print("Identifying Required Documents")
    for example in tqdm(QUERIES):
        example.docs = query_docs(cb_scope, example.query)
        example.no_docs = len(example.docs)
        if example.no_docs < 1:
            print(f"Warning: Query {example.id} did not yield any documents")
        required_docs.update(example.docs)

    # Export users from tenant_agent_01
    USER_EXPORT_QUERY = Query(
        id="TENANT_01_USERS", query="""select meta(users).id user_id from users"""
    )
    user_docs = query_docs(tenant_scope, USER_EXPORT_QUERY.query)
    if len(user_docs) < 1:
        print(f"Warning: Query {USER_EXPORT_QUERY.id} did not yield any documents")
    required_docs.update(user_docs)

    print(f"Identified {2*len(required_docs)} docs to be exported")

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
    {"collection": "users", "prefix": "tenant_agent_01.users", "doc_ids": user_docs},
]

for export in EXPORT_MATRIX:
    collection = export["collection"]
    docs_location = export["prefix"]
    doc_ids = export["doc_ids"]

    collection_export = {}
    dest_location = docs_location.replace("inventory", "sample")
    dest_location = dest_location.replace("tenant_agent_01", "sample")
    # print(dest_location)
    default_location = docs_location.replace("inventory", "_default")
    default_location = default_location.replace("tenant_agent_01", "_default")
    default_location = default_location.replace(collection, "_default")

    print(f"Exporting {collection}")

    # export into sample format for cbimport
    for doc_id in tqdm(doc_ids):
        try:
            src_file = pathlib.Path(data_directory, f"{docs_location}.{doc_id}.json")
            dst_file = pathlib.Path(
                destination_directory, f"{dest_location}.{doc_id}.json"
            )
            shutil.copy(src_file, dst_file)
            # Also copy the document to _default scope & collection
            def_file = pathlib.Path(
                destination_directory, f"{default_location}.{doc_id}.json"
            )
            shutil.copy(src_file, def_file)
        except Exception as e:
            print(f"Exception while copying file {doc_id}", e)

print("Exporting to archive")
try:
    shutil.make_archive("smalltravelsample", "zip", "smalltravelsample")
except Exception as e:
    print(f"Exception while creating the archive", e)

print("Exported to smalltravelsample.zip")
