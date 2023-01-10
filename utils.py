import couchbase


def query_docs(scope: couchbase.scope.Scope, sql_query: str):
    """Run the query & return the document ids that match the query"""
    docs = set()
    try:
        results = scope.query(sql_query)
        docs = parse_docs_from_results(results)
    except Exception as e:
        print(e)
    return docs


def parse_docs_from_results(results: couchbase.result.QueryResult) -> list[str]:
    """Parse the unique document ids from the query results"""
    doc_ids = set()
    for record in results:
        docs = get_doc_ids(record)
        doc_ids.update(docs)
    return doc_ids


def get_doc_ids(result: couchbase.result.QueryResult) -> list[str]:
    """Parse the document ids from the query result.
    It parses the travel sample collection ids, airport_id, airline_id,
    route_id, hotel_id & landmark_id"""
    docs = []

    airport_doc = result.get("airport_id")
    airline_doc = result.get("airline_id")
    hotel_doc = result.get("hotel_id")
    route_doc = result.get("route_id")
    landmark_doc = result.get("landmark_id")

    if airport_doc:
        docs.append(airport_doc)

    if airline_doc:
        docs.append(airline_doc)

    if hotel_doc:
        docs.append(hotel_doc)

    if route_doc:
        docs.append(route_doc)

    if landmark_doc:
        docs.append(landmark_doc)

    return docs
