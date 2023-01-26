## small-travel-sample

A Python script used to identify the documents to load from the travel-sample dataset.

The documents are identified based on satisying the queries identified in `queries.py`.

## Approach

- Define the list of queries that need to be satisfied by the documents to be exported.

- We run all these queries against a Couchbase instance having the entire travel-sample bucket using the Python SDK to identify the documents that match these queries.

Note that the queries should include the meta id of the document specified as the collection id for the document to be identified correctly.

### Example:

Query to be satisfied

```sql
SELECT name, city, state
            FROM hotel h
            WHERE h.city = 'San Francisco'
            AND h.state = 'California'
            ORDER BY NAME
            LIMIT 5
```

Query to be written in `queries.py`

```sql
SELECT META(h).id hotel_id, name, city, state
            FROM hotel h
            WHERE h.city = 'San Francisco'
            AND h.state = 'California'
            ORDER BY NAME
            LIMIT 5
```

Note that we added the document key using META(h).id as `hotel_id` for it to be exported to the hotel collection of the smaller sample data.

- We export all the identified documents into smalltravelsample.zip file which includes all the documents in the sample format for import using cbimport.

- The current queries have been taken from the SDK & SQL++ queries from the playground along with the queries from the [SQL++ Reference Documentation pages](https://docs.couchbase.com/server/current/n1ql/n1ql-language-reference/index.html).

## Running the Script

Prerequisites

- Python 3.9 or greater

- Download the travel-sample dataset from the [dataloader repo](https://github.com/couchbase/docloader/blob/master/examples/travel-sample.zip) and extract it. Store the path to /docs inside the folder in the environment variable DATA_DIR.

- Install the requirements
  `$ pip install -r requirements.txt`

- Copy `.env.example` to `.env` and fill the details of the Couchbase Cluster which is being used to identify the documents to be exported.

> DB_CONN_STR=<complete_connection_string> Example:couchbases://cb.xompk2curacvoatm.nonprod-project-avengers.com?tls_verify=no_verify

> DB_USER=database-username

> DB_PWD=database-password

> DB_BUCKET=travel-sample

> DATA_DIR=<path-to-folder-containing-the-travel-sample-documents> Example: ~/small-travel-sample/travel-sample/docs

> Note that the cluster needs to contain the travel-sample bucket with the entire data for the script to work.

- Update the queries if you like by adding new queries to `queries.py`. Note that you need to create a new query & add it to an existing list for it to be checked.

- Run the script, `identify_docs.py` to identify & export the docs that satisfy all the queries.

  `$ python identify_docs.py`

- The script displays a warning along with the query id if some query cannot be matched with any documents. These query ids can be debugged for errors.

- The exported documents can be found in `smalltravelsample.zip`. These can be imported into a bucket in Couchbase using cbimport.

```bash
./cbimport json -c couchbase://localhost:8091 -u <username> -p <password> -b <bucket> -f sample -d file://smalltravelsample.zip
```
