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

- We export all the identified documents into a collection_name.json file which includes all the documents specified by their document id.

```json
{"airline_551": {"id": 551, "type": "airline", "name": "Air Moorea", "iata": null, "icao": "TAH", "callsign": "AIR MOOREA", "country": "France"}, "airline_139": {"id": 139, "type": "airline", "name": "Air Caledonie International", "iata": "SB", "icao": "ACI", "callsign": "AIRCALIN", "country": "France"}, "airline_1316": {"id": 1316, "type": "airline", "name": "AirTran Airways", "iata": "FL", "icao": "TRS", "callsign": "CITRUS", "country": "United States"}, "airline_21": {"id": 21, "type": "airline", "name": "Aigle Azur", "iata": "ZI", "icao": "AAF", "callsign": "AIGLE AZUR", "country": "France"}...
```

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

> DATA_DIR=<path-to-folder-containing-the-travel-sample-documents> Example: /Users/nithishraghunandan/Code/small-travel-sample/travel-sample/docs

- Update the queries if you like by adding new queries to `queries.py`. Note that you need to create a new query & add it to an existing list for it to be checked.

- Run the script, `identify_docs.py` to identify & export the docs that satisfy all the queries.

  `$ python identify_docs.py`

- The script displays a warning along with the query id if some query cannot be matched with any documents. These query ids can be debugged for errors.

- The exported documents can be found in `airline.json`, `airport.json`, `hotel.json`, `landmark.json` and `route.json`. These can be imported into their respective collections in the small-travel-sample dataset.
