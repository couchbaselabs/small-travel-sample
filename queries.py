from query import Query

## Playground SQL++ Documents
PG_SQL_1 = Query(
    id="PG_SQL_1",
    query="""
    SELECT DISTINCT airline.name, airline.callsign, route.schedule,
route.sourceairport, route.destinationairport, META(airline).id airline_id, META(route).id route_id
FROM route
  INNER JOIN airline
  ON route.airlineid = META(airline).id
WHERE route.sourceairport = "JFK"
AND route.destinationairport = "SFO"
AND airline.callsign = "UNITED";
""",
)

PG_SQL_2 = Query(
    id="PG_SQL_2",
    query="""
    SELECT DISTINCT route.airline, route.schedule,
route.sourceairport, route.airlineid, META(route).id route_id FROM route
WHERE route.sourceairport = "JFK"
ORDER BY route.airline
LIMIT 5;
""",
)

PG_SQL_3 = Query(
    id="PG_SQL_3",
    query="""
SELECT DISTINCT route.airline, route.schedule,
route.sourceairport, route.destinationairport, META(route).id route_id, route.airlineid FROM route
WHERE route.sourceairport = "JFK"
AND route.destinationairport = "SFO";
""",
)

PG_SQL_4 = Query(
    id="PG_SQL_4",
    query="""
    SELECT DISTINCT airline.name, airline.callsign, route.schedule, 
route.sourceairport, route.destinationairport, META(airline).id airline_id, META(route).id route_id
FROM route
  INNER JOIN airline
  ON route.airlineid = META(airline).id
WHERE route.sourceairport = "JFK"
AND route.destinationairport = "SFO"
AND airline.callsign = "UNITED";
    """,
)

PLAYGROUND_SQL_QUERIES = [PG_SQL_1, PG_SQL_2, PG_SQL_3, PG_SQL_4]

## Playground SDK Documents
PG_SDK_1 = Query(
    id="PG_SDK_1",
    query="""
SELECT META(airline).id airline_id from airline where META(airline).id="airline_10";
""",
)

PG_SDK_2 = Query(
    id="PG_SDK_2",
    query="""
    SELECT META(h).id hotel_id, name, city, state
            FROM hotel h
            WHERE h.city = 'San Francisco'
            AND h.state = 'California' 
            ORDER BY NAME 
            LIMIT 5
    """,
)

PG_SDK_3 = Query(
    id="PG_SDK_3",
    query="""
    SELECT META(airport).id airport_id from airport where META(airport).id="airport_1254";""",
)

PLAYGROUND_SDK_QUERIES = [PG_SDK_1, PG_SDK_2, PG_SDK_3]

## Docs: N1QL Language Reference Queries

N1QL_REF_1 = Query(
    id="N1QL_REF_1",
    query="""
    SELECT airportname, city, geo, ROUND(geo.lat) AS latitude, META(t1).id airport_id
FROM airport t1
LIMIT 1;
""",
)

N1QL_REF_2 = Query(
    id="N1QL_REF_2",
    query="""
    SELECT sourceairport, destinationairport, ROUND(distance) AS DistanceInMiles,
       ROUND(distance)*5280 AS DistanceInFeet, meta(route).id route_id
FROM route
ORDER BY distance DESC
LIMIT 1;
    """,
)

N1QL_REF_3 = Query(
    id="N1QL_REF_3",
    query="""
    SELECT *, META(route).id route_id FROM route
WHERE airline="KL" AND sourceairport="ABQ"
  AND destinationairport="ATL"
  AND ANY departure IN schedule SATISFIES departure.utc > "23:40" END;
  """,
)

N1QL_REF_4 = Query(
    id="N1QL_REF_4",
    query="""
    SELECT *, META(route).id route_id FROM route
WHERE airline="KL"
  AND sourceairport="ABQ"
  AND destinationairport="ATL"
  AND EVERY departure IN schedule SATISFIES departure.utc > "00:35" END;
  """,
)

N1QL_REF_5 = Query(
    id="N1QL_REF_5",
    query="""
    SELECT ARRAY v FOR v IN schedule WHEN v.day = 5 END AS fri_flights, META(route).id route_id
FROM route
WHERE airline="KL"
  AND sourceairport="ABQ"
  AND destinationairport="ATL";
    """,
)

N1QL_REF_6 = Query(
    id="N1QL_REF_6",
    query="""
    SELECT ARRAY v
  FOR v IN schedule, w IN schedule WHEN v.utc > "19:00" AND w.day = 5 END
  AS fri_evening_flight, META(route).id route_id
FROM route
WHERE airline="KL"
  AND sourceairport="ABQ"
  AND destinationairport="ATL";
    """,
)

N1QL_REF_7 = Query(
    id="N1QL_REF_7",
    query="""
    SELECT ARRAY v FOR i:v IN schedule WHEN i < 2 END AS two_flights, META(route).id route_id
FROM route
WHERE airline="KL"
  AND sourceairport="ABQ"
  AND destinationairport="ATL";
  """,
)

N1QL_REF_8 = Query(
    id="N1QL_REF_8",
    query="""
    SELECT FIRST v FOR v IN schedule WHEN v.utc > "19:00" END AS first_flight, META(route).id route_id
FROM route
WHERE airline="KL"
  AND sourceairport="ABQ"
  AND destinationairport="ATL";
  """,
)

N1QL_REF_9 = Query(
    id="N1QL_REF_9",
    query="""
    SELECT OBJECT UUID():v FOR v IN schedule WHEN v.day = 5 END AS fri_flights, META(route).id route_id
FROM route
WHERE airline="KL"
  AND sourceairport="ABQ"
  AND destinationairport="ATL";
    """,
)

N1QL_REF_10 = Query(
    id="N1QL_REF_10",
    query="""
    SELECT OBJECT "num_" || TOSTRING(i):v
  FOR i:v IN schedule WHEN v.day = 5 END
  AS fri_flights, META(route).id route_id
FROM route
WHERE airline="KL"
  AND sourceairport="ABQ"
  AND destinationairport="ATL";
    """,
)

N1QL_REF_11 = Query(
    id="N1QL_REF_11",
    query="""
    SELECT *, META(t).id airline_id FROM airline AS t
WHERE country IN ["United Kingdom", "France"]
ORDER BY t.callsign
LIMIT 10;
    """,
)

N1QL_REF_12 = Query(
    id="N1QL_REF_12",
    query="""
    SELECT *, META(t).id hotel_id FROM hotel AS t WHERE "Walton Wolf" WITHIN t;
    """,
)

N1QL_REF_13 = Query(
    id="N1QL_REF_13",
    query="""
    SELECT DISTINCT h.city, META(h).id hotel_id
FROM hotel AS h
WHERE EXISTS h.reviews
ORDER BY h.name 
LIMIT 10;
    """,
)

N1QL_REF_14 = Query(
    id="N1QL_REF_14",
    query="""
    SELECT [ address, city, country ] AS location, meta(hotel).id hotel_id
FROM hotel LIMIT 3;
    """,
)

N1QL_REF_15 = Query(
    id="N1QL_REF_15",
    query="""
    SELECT { "street": address, city, country } AS location, meta(hotel).id hotel_id
FROM hotel LIMIT 3;
    """,
)

N1QL_REF_16 = Query(
    id="N1QL_REF_16",
    query="""
    SELECT ARRAY_APPEND(t.public_likes, "Valerie Smith") AS add_user_likes, meta(t).id hotel_id
FROM hotel t
LIMIT 1;
    """,
)

N1QL_REF_17 = Query(
    id="N1QL_REF_17",
    query="""
    SELECT ARRAY_BINARY_SEARCH(ARRAY_SORT(t.public_likes), "Brian Kilback")
AS sorted_position,  meta(t).id hotel_id
FROM hotel t
LIMIT 1;
    """,
)

N1QL_REF_18 = Query(
    id="N1QL_REF_18",
    query="""
    SELECT ARRAY_CONCAT(t.public_likes, ["John McHill", "Dave Smith"]) AS add_user_likes, meta(t).id hotel_id
FROM hotel t
LIMIT 1;
    """,
)

N1QL_REF_19 = Query(
    id="N1QL_REF_19",
    query="""
    SELECT ARRAY_CONTAINS(t.public_likes, "Vallie Ryan") AS array_contains_value, meta(t).id hotel_id
FROM hotel t
LIMIT 1;
    """,
)

N1QL_REF_20 = Query(
    id="N1QL_REF_20",
    query="""
    SELECT ARRAY_COUNT(t.reviews) AS total_reviews, meta(t).id hotel_id
FROM hotel t
LIMIT 1;
    """,
)

N1QL_REF_21 = Query(
    id="N1QL_REF_21",
    query="""
    SELECT ARRAY_INSERT(public_likes, 2, "jsmith") AS insert_val, meta(hotel).id hotel_id
FROM hotel
LIMIT 1;
""",
)

N1QL_REF_22 = Query(
    id="N1QL_REF_22",
    query="""
    SELECT ARRAY_LENGTH(t.public_likes) AS total_likes, meta(t).id hotel_id
FROM hotel t
LIMIT 1;
    """,
)

N1QL_REF_23 = Query(
    id="N1QL_REF_23",
    query="""
    SELECT ARRAY_MAX(t.public_likes) AS max_val, meta(t).id hotel_id
FROM hotel t
LIMIT 1;
    """,
)

N1QL_REF_24 = Query(
    id="N1QL_REF_24",
    query="""
    SELECT ARRAY_MIN(t.public_likes) AS min_val, meta(t).id hotel_id
FROM hotel t
LIMIT 1;
    """,
)

N1QL_REF_25 = Query(
    id="N1QL_REF_25",
    query="""
    SELECT ARRAY_POSITION(t.public_likes, "Brian Kilback") AS array_position, meta(t).id hotel_id
FROM hotel t
LIMIT 1;
    """,
)

N1QL_REF_26 = Query(
    id="N1QL_REF_26",
    query="""
    SELECT ARRAY_PREPEND("Dave Smith",t.public_likes) AS prepend_val, meta(t).id hotel_id
FROM hotel t
LIMIT 1;
    """,
)

N1QL_REF_27 = Query(
    id="N1QL_REF_27",
    query="""
    SELECT ARRAY_PUT(t.public_likes, "Dave Smith") AS array_put, meta(t).id hotel_id
FROM hotel t
LIMIT 1;""",
)

N1QL_REF_28 = Query(
    id="N1QL_REF_28",
    query="""
    SELECT ARRAY_REMOVE(t.public_likes, "Vallie Ryan") AS remove_val, meta(t).id hotel_id
FROM hotel t
LIMIT 1;
    """,
)

N1QL_REF_29 = Query(
    id="N1QL_REF_29",
    query="""
    SELECT ARRAY_REPLACE(t.public_likes, "Vallie Ryan", "Valerie Ryan") AS replace_val, meta(t).id hotel_id
FROM hotel t
LIMIT 1;
    """,
)

N1QL_REF_30 = Query(
    id="N1QL_REF_30",
    query="""
    SELECT ARRAY_REVERSE(t.public_likes) AS reverse_val, meta(t).id hotel_id
FROM hotel t
LIMIT 1;
    """,
)

N1QL_REF_31 = Query(
    id="N1QL_REF_31",
    query="""
    SELECT ARRAY_SORT(t.public_likes) AS sorted_array, meta(t).id hotel_id
FROM hotel t
LIMIT 1;
    """,
)

N1QL_REF_32 = Query(
    id="N1QL_REF_32",
    query="""
    SELECT airline, stops, schedule[0].day, meta(route).id route_id FROM route
WHERE stops = 1;
    """,
)

N1QL_REF_33 = Query(
    id="N1QL_REF_33",
    query="""
    SELECT airline, stops, schedule[0].day, meta(route).id route_id FROM route
WHERE BITTEST(stops,1);
    """,
)

N1QL_REF_34 = Query(
    id="N1QL_REF_34",
    query="""
    SELECT a.airportname AS Airport,
DECODE(a.tz, "Pacific/Honolulu", "-10:00",
             "America/Anchorage", "-09:00",
             "America/Los_Angeles", "-08:00",
             "America/Denver", "-07:00",
             "America/Chicago", "-06:00",
             "America/New_York", "-05:00", a.tz) AS UTCOffset,
meta(a).id airport_id
FROM airport a
WHERE a.country = "United States" AND a.geo.alt > 1000
LIMIT 5;
    """,
)

N1QL_REF_35 = Query(
    id="N1QL_REF_35",
    query="""
    SELECT name as Name, NVL(iata, "n/a") as IATA, meta(airline).id airline_id
FROM airline
LIMIT 5;
    """,
)

N1QL_REF_36 = Query(
    id="N1QL_REF_36",
    query="""
    SELECT name as Name, NVL2(directions, "Yes", "No") as DirectionsAvailable, meta(hotel).id hotel_id
FROM hotel
LIMIT 5;
""",
)

N1QL_REF_37 = Query(
    id="N1QL_REF_37",
    query="""
    SELECT name, reviews[0].date, meta(hotel).id hotel_id
FROM hotel
WHERE reviews[0].date BETWEEN "2013-01-01 %" AND "2014-01-01 %"
ORDER BY name
LIMIT 10;
""",
)

N1QL_REF_38 = Query(
    id="N1QL_REF_38",
    query="""
    SELECT name, reviews[0].date, meta(hotel).id hotel_id
FROM hotel
WHERE reviews[0].date BETWEEN "2013-01-01 00:00:00 +0100" AND "2014-01-01 00:00:00 +0100"
ORDER BY name
LIMIT 10;
    """,
)

N1QL_REF_39 = Query(
    id="N1QL_REF_39",
    query="""
    SELECT META() AS metadata, META(airline).id airline_id
FROM airline
LIMIT 3;
    """,
)

N1QL_REF_40 = Query(
    id="N1QL_REF_40",
    query="""
    SELECT META().id AS airline_id
FROM airline
LIMIT 3;
    """,
)

N1QL_REF_41 = Query(
    id="N1QL_REF_41",
    query="""
    SELECT META(route).id AS route_id, META(airport).id airport_id 
FROM route
JOIN airport
ON route.sourceairport = airport.faa
WHERE airport.city = "Paris"
LIMIT 3;
    """,
)

N1QL_REF_42 = Query(
    id="N1QL_REF_42",
    query="""
    SELECT t AS orig_t,
       PAIRS(t) AS pairs_t,
       meta(t).id airport_id
FROM   airport t
LIMIT  1;
    """,
)

N1QL_REF_43 = Query(
    id="N1QL_REF_43",
    query="""
    SELECT public_likes          AS orig_t,
       PAIRS(public_likes)   AS pairs_array_t,
       PAIRS({public_likes}) AS pairs_obj_t,
       META(hotel).id hotel_id
FROM   hotel
LIMIT  1;
    """,
)

N1QL_REF_44 = Query(
    id="N1QL_REF_44",
    query="""
    SELECT country        AS orig_t,
       PAIRS(country) AS pairs_t,
       META(airport).id airport_id
FROM   airport
LIMIT  1;
    """,
)

N1QL_REF_45 = Query(
    id="N1QL_REF_45",
    query="""
    SELECT reviews[*].ratings,
       PAIRS({reviews[*].ratings}) AS pairs_t,
       META(hotel).id hotel_id
FROM   hotel
LIMIT  1;
    """,
)

N1QL_REF_46 = Query(
    id="N1QL_REF_46",
    query="""
    SELECT * FROM landmark, META(landmark).id landmark_id
WHERE landmark.activity = 'eat' AND landmark.city = 'Paris'
order by landmark.name 
limit 10;
    """,
)

N1QL_REF_47 = Query(
    id="N1QL_REF_47",
    query="""
    SELECT *, META(t).id route_id FROM route t
             WHERE t.sourceairport = 'SFO'
             ORDER BY airline
             LIMIT 10;
    """,
)

N1QL_REF_48 = Query(
    id="N1QL_REF_48",
    query="""
    SELECT schedule[0] AS original,
       OBJECT_ADD(schedule[0], "day_new", 1) AS output,
       meta(route).id route_id
FROM route
LIMIT 1;
""",
)

N1QL_REF_49 = Query(
    id="N1QL_REF_49",
    query="""
    SELECT OBJECT_FIELD(hotel, "public_likes") AS `array`,
       OBJECT_FIELD(hotel, "vacancy") AS `boolean`,
       OBJECT_FIELD(hotel, "id") AS `number`,
       OBJECT_FIELD(hotel, "geo") AS `object`,
       OBJECT_FIELD(hotel, "name") AS `string`,
       META(hotel).id hotel_id
FROM hotel
LIMIT 1;
    """,
)

N1QL_REF_50 = Query(
    id="N1QL_REF_50",
    query="""
    SELECT
  OBJECT_FIELD(hotel, "reviews[1]")
    AS array_element,
  OBJECT_FIELD(hotel, "reviews[1].ratings.`Business service (e.g., internet access)`")
    AS object_attribute,
META(hotel).id hotel_id
FROM hotel
LIMIT 1;
    """,
)

N1QL_REF_51 = Query(
    id="N1QL_REF_51",
    query="""
    SELECT schedule[0] AS original,
       OBJECT_PUT(schedule[0], "day", 1) AS output,
       META(route).id route_id
FROM route
LIMIT 1;
""",
)

N1QL_REF_52 = Query(
    id="N1QL_REF_52",
    query="""
    SELECT t AS original,
       OBJECT_RENAME(t, "name", "new_name") AS output,
       meta(t).id airline_id
FROM airline AS t
LIMIT 1;""",
)

N1QL_REF_53 = Query(
    id="N1QL_REF_53",
    query="""
    SELECT schedule[0] AS original,
       OBJECT_REMOVE(schedule[0], "day") AS output,
       meta(route).id route_id
FROM route
LIMIT 1;
    """,
)

N1QL_REF_54 = Query(
    id="N1QL_REF_54",
    query="""
    SELECT t AS original,
       OBJECT_REPLACE(t, "airline", "airplane") AS output,
       meta(t).id airline_id
FROM airline AS t
LIMIT 1;
    """,
)

N1QL_REF_55 = Query(
    id="N1QL_REF_55",
    query="""
    SELECT name, META(landmark).id landmark_id
FROM landmark
WHERE REGEXP_CONTAINS(name, "In+.*")
LIMIT 5;
    """,
)

N1QL_REF_56 = Query(
    id="N1QL_REF_56",
    query="""
    SELECT name, META(landmark).id landmark_id
FROM landmark
WHERE REGEXP_LIKE(name, "In+.*")
LIMIT 5;
""",
)

N1QL_REF_57 = Query(
    id="N1QL_REF_57",
    query="""
SELECT name, ARRAY REGEXP_POSITION(x, "[aeiou]") FOR x IN TOKENS(name) END, meta(hotel).id hotel_id
FROM hotel
LIMIT 2;
""",
)

N1QL_REF_58 = Query(
    id="N1QL_REF_58",
    query="""
    SELECT name, REGEXP_REPLACE(name, "n+", "NNNN") as new_name, meta(airline).id airline_id
FROM airline
LIMIT 4;
    """,
)

N1QL_REF_59 = Query(
    id="N1QL_REF_59",
    query="""
    SELECT META(t1).id airline_id
FROM airline AS t1
WHERE SEARCH(t1.country, "+United +States")
LIMIT 10;
    """,
)

N1QL_REF_60 = Query(
    id="N1QL_REF_60",
    query="""
    SELECT META(t1).id airline_id
FROM airline AS t1
WHERE SEARCH(t1, "country:United States")
Limit 10;
    """,
)

N1QL_REF_61 = Query(
    id="N1QL_REF_61",
    query="""
    SELECT t1.name, meta(t1).id hotel_id
FROM hotel AS t1
WHERE SEARCH(t1, {
  "match": "bathrobes",
  "field": "reviews.content",
  "analyzer": "standard"
});
    """,
)

N1QL_REF_62 = Query(
    id="N1QL_REF_62",
    query="""
    SELECT t1.name, meta(t1).id hotel_id
FROM hotel AS t1
WHERE SEARCH(t1, {
  "explain": false,
  "fields": [
     "*"
   ],
   "highlight": {},
   "query": {
     "match": "bathrobes",
     "field": "reviews.content",
     "analyzer": "standard"
   },
   "size" : 5,
   "sort": [
      {
       "by" : "field",
       "field" : "reviews.ratings.Overall",
       "mode" : "max",
       "missing" : "last"
      }
   ]
});
    """,
)

N1QL_REF_63 = Query(
    id="N1QL_REF_63",
    query="""
    SELECT META(t1).id hotel_id
FROM hotel AS t1
WHERE t1.type = "hotel" AND SEARCH(t1.description, "amazing");
    """,
)

N1QL_REF_64 = Query(
    id="N1QL_REF_64",
    query="""
    SELECT SEARCH_META() AS meta, META(t1).id hotel_id
FROM hotel AS t1
WHERE SEARCH(t1, {
  "query": {
    "match": "bathrobes",
    "field": "reviews.content",
    "analyzer": "standard"
  },
  "includeLocations": true 
})
LIMIT 3;
    """,
)

N1QL_REF_65 = Query(
    id="N1QL_REF_65",
    query="""
    SELECT t1.name, SEARCH_META(s1) AS meta, META(t1).id hotel_id 
FROM hotel AS t1
WHERE SEARCH(t1.description, "mountain", {"out": "s1"}) 
AND SEARCH(t1, {
  "query": {
    "match": "bathrobes",
    "field": "reviews.content",
    "analyzer": "standard"
  }
});
    """,
)

N1QL_REF_66 = Query(
    id="N1QL_REF_66",
    query="""
    SELECT name, description, SEARCH_SCORE() AS score, meta(t1).id hotel_id
FROM hotel AS t1
WHERE SEARCH(t1.description, "mountain")
ORDER BY score DESC
LIMIT 3;
    """,
)

N1QL_REF_67 = Query(
    id="N1QL_REF_67",
    query="""
    SELECT airportname, meta(airport).id airport_id
FROM airport
WHERE ANY array_element
IN SUFFIXES(LOWER(airportname)) SATISFIES array_element LIKE 'washing%' END
    """,
)

N1QL_REF_68 = Query(
    id="N1QL_REF_68",
    query="""
    SELECT name, address, url, meta(hotel).id hotel_id
FROM hotel
WHERE ANY  v in tokens(url, {"specials":true, "case":"UPPER"})
      SATISFIES v = "HTTP://WWW.YHA.ORG.UK"
      END
AND type = 'hotel' ;
    """,
)

N1QL_REF_69 = Query(
    id="N1QL_REF_69",
    query="""
    SELECT name, meta(hotel).id hotel_id
FROM hotel
WHERE CONTAINS_TOKEN(name, "Inn",{"specials":true})
LIMIT 4;
    """,
)

N1QL_REF_70 = Query(
    id="N1QL_REF_70",
    query="""
    SELECT email, meta(hotel).id hotel_id
FROM hotel
WHERE CONTAINS_TOKEN_LIKE(email, "%uk",{"specials":true})
LIMIT 4;
""",
)

N1QL_REF_71 = Query(
    id="N1QL_REF_71",
    query="""
    SELECT name, meta(hotel).id hotel_id
FROM hotel
WHERE CONTAINS_TOKEN_REGEXP(name, "In+.*",{"specials":true})
LIMIT 4;
    """,
)

N1QL_REF_72 = Query(
    id="N1QL_REF_72",
    query="""
    SELECT ARRAY_SORT( TOKENS(url) ) AS defaulttoken,
       ARRAY_SORT( TOKENS(url, {"specials":true, "case":"UPPER"}) ) AS specialtoken,
       meta(hotel).id hotel_id
FROM hotel
LIMIT 1;
""",
)

N1QL_REF_73 = Query(
    id="N1QL_REF_73",
    query="""
    SELECT name, address, url, meta(hotel).id hotel_id
FROM hotel
WHERE ANY  v in tokens(url, {"specials":true, "case":"UPPER"})
      SATISFIES v = "HTTP://WWW.YHA.ORG.UK"
      END
AND type = 'hotel' ;
""",
)

N1QL_REF_74 = Query(
    id="N1QL_REF_74",
    query="""
    SELECT id, name, address, city, meta(landmark).id landmark_id
  FROM landmark
  WHERE activity = "eat"
  AND city ="Gillingham";
    """,
)

N1QL_REF_75 = Query(
    id="N1QL_REF_75",
    query="""
    SELECT d.id, d.destinationairport, meta(d).id route_id, CUME_DIST() OVER (
  PARTITION BY d.destinationairport
  ORDER BY d.distance NULLS LAST
) AS `rank`
FROM route AS d
LIMIT 7;
    """,
)

N1QL_REF_76 = Query(
    id="N1QL_REF_76",
    query="""
    SELECT a.airportname, a.geo.alt, DENSE_RANK() OVER (
  PARTITION BY a.country
  ORDER BY a.geo.alt NULLS LAST
) AS `rank`,
meta(a).id airport_id
FROM airport AS a
LIMIT 10;
    """,
)

N1QL_REF_77 = Query(
    id="N1QL_REF_77",
    query="""
    SELECT r.sourceairport, r.destinationairport, r.distance,
FIRST_VALUE(r.distance) OVER (
  PARTITION BY r.sourceairport
  ORDER BY r.distance
) AS `shortest_distance`,
meta(r).id route_id
FROM route AS r
LIMIT 7;
    """,
)

N1QL_REF_78 = Query(
    id="N1QL_REF_78",
    query="""
    SELECT r.airline, r.id, r.distance,
LAG(r.distance, 1, "No previous distance") OVER (
  PARTITION BY r.airline
  ORDER BY r.distance NULLS LAST
) AS `previous-distance`,
meta(r).id route_id
FROM route AS r
LIMIT 7;
    """,
)

N1QL_REF_79 = Query(
    id="N1QL_REF_79",
    query="""
    SELECT r.sourceairport, r.destinationairport, r.distance,
LAST_VALUE(r.distance) OVER (
  PARTITION BY r.sourceairport
  ORDER BY r.distance
  ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING 
) AS `longest_distance`,
meta(r).id route_id
FROM route AS r
LIMIT 7;
    """,
)

N1QL_REF_80 = Query(
    id="N1QL_REF_80",
    query="""
    SELECT r.airline, r.id, r.distance,
LEAD(r.distance, 1, "No next distance") OVER (
  PARTITION BY r.airline
  ORDER BY r.distance NULLS LAST
) AS `next-distance`,
meta(r).id route_id
FROM route AS r
LIMIT 7;
""",
)

N1QL_REF_81 = Query(
    id="N1QL_REF_81",
    query="""
    SELECT r.sourceairport, r.destinationairport, r.distance,
NTH_VALUE(r.distance, 2) FROM FIRST OVER (
  PARTITION BY r.sourceairport
  ORDER BY r.distance
  ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING 
) AS `shortest_distance_but_1`,
meta(r).id route_id
FROM route AS r
LIMIT 7;
    """,
)

N1QL_REF_82 = Query(
    id="N1QL_REF_82",
    query="""
    SELECT r.sourceairport, r.destinationairport, r.distance,
NTH_VALUE(r.distance, 2) FROM LAST OVER (
  PARTITION BY r.sourceairport
  ORDER BY r.distance
  ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING 
) AS `longest_distance_but_1`,
META(r).id route_id
FROM route AS r
LIMIT 7;
    """,
)

N1QL_REF_83 = Query(
    id="N1QL_REF_83",
    query="""
    SELECT r.airline, r.distance, NTILE(3) OVER (
  PARTITION BY r.airline
  ORDER BY r.distance
) AS `ntile`,
META(r).id route_id
FROM route AS r
LIMIT 16;
    """,
)

N1QL_REF_84 = Query(
    id="N1QL_REF_84",
    query="""
    SELECT d.id, d.destinationairport, PERCENT_RANK() OVER (
  PARTITION BY d.destinationairport
  ORDER BY d.distance NULLS LAST
) AS `rank`,
META(d).id route_id
FROM route AS d
LIMIT 7;
""",
)

N1QL_REF_85 = Query(
    id="N1QL_REF_85",
    query="""
    SELECT a.airportname, a.geo.alt, RANK() OVER (
  PARTITION BY a.country
  ORDER BY a.geo.alt NULLS LAST
) AS `rank`,
meta(a).id airport_id
FROM airport AS a
LIMIT 10;
    """,
)

N1QL_REF_86 = Query(
    id="N1QL_REF_86",
    query="""
    SELECT d.id, d.destinationairport, RATIO_TO_REPORT(d.distance) OVER (
  PARTITION BY d.destinationairport
) AS `distance-ratio`,
META(d).id route_id
FROM route AS d
LIMIT 7;
    """,
)

N1QL_REF_87 = Query(
    id="N1QL_REF_87",
    query="""
    SELECT d.id, d.destinationairport, ROW_NUMBER() OVER (
  PARTITION BY d.destinationairport
  ORDER BY d.distance NULLS LAST
) AS `row`,
META(d).id route_id
FROM route AS d
LIMIT 7;
    """,
)

N1QL_REF_88 = Query(
    id="N1QL_REF_88",
    query="""
      SELECT t1.city, META(t1).id landmark_id FROM landmark t1 WHERE t1.city IN (SELECT RAW city FROM airport )
  order by t1.city
  limit 10;  
    """,
)

N1QL_REF_89 = Query(
    id="N1QL_REF_89",
    query="""
    SELECT t1.city, t1.name, meta(t1).id landmark_id
FROM landmark t1
WHERE t1.city IN SPLIT((SELECT RAW t2.name
                        FROM t1 AS t2)[0])
order by t1.name
limit 10;
""",
)

N1QL_REF_90 = Query(
    id="N1QL_REF_90",
    query="""
    SELECT t1.city, t1.name, meta(t1).id landmark_id
FROM landmark t1
WHERE t1.city IN SPLIT(t1.name)
order by t1.name
limit 10;
    """,
)

N1QL_REF_91 = Query(
    id="N1QL_REF_91",
    query="""
    SELECT META(t).id airport_id FROM airport t
WHERE (SELECT RAW t.geo.alt FROM t t1)[0] > 6000 
order by t.geo.alt desc
limit 10;
""",
)

N1QL_REF_92 = Query(
    id="N1QL_REF_92",
    query="""
    SELECT meta(t1).id landmark_id FROM landmark t1
WHERE t1.city IN (SELECT RAW city
                  FROM hotel
                  LIMIT 3
                  );
    """,
)

N1QL_REF_93 = Query(
    id="N1QL_REF_93",
    query="""
    SELECT t1.city, t1.geo.alt, meta(t1).id airport_id
FROM airport t1
WHERE (SELECT RAW t2.alt FROM t1.geo t2)[0] > 4000
order by t1.geo.alt desc
limit 10;
""",
)

N1QL_REF_94 = Query(
    id="N1QL_REF_94",
    query="""
    SELECT name, cnt_reviewers, meta(t).id hotel_id
FROM hotel AS t
LET cnt_reviewers = (SELECT raw count(*)
                     FROM t.reviews AS s
                     WHERE s.ratings.Overall >= 4)[0]
WHERE cnt_reviewers >= 6
ORDER BY cnt_reviewers DESC
LIMIT 10;
    """,
)

N1QL_REF_95 = Query(
    id="N1QL_REF_95",
    query="""
    SELECT airline_details, t1.destinationairport, t1.stops, meta(t1).id route_id
FROM route  t1
LET airline_details = (SELECT t2.name, t2.callsign
                       FROM airline t2
	               USE KEYS t1.airlineid
                       WHERE t2.iata = t1.airline)
WHERE  t1.sourceairport = "SFO"
      AND ARRAY_LENGTH(airline_details) > 0
LIMIT 2;
    """,
)

N1QL_REF_96 = Query(
    id="N1QL_REF_96",
    query="""SELECT DISTINCT airline.name, airline.callsign, route.destinationairport, route.stops, route.airline, meta(route).id route_id, meta(airline).id airline_id
FROM route
      JOIN airline
      ON KEYS route.airlineid
WHERE route.sourceairport = "SFO"
LIMIT 2;
""",
)

N1QL_REF_97 = Query(
    id="N1QL_REF_97",
    query="""SELECT name, (SELECT raw avg(s.ratings.Overall)
              FROM   t.reviews  as s)[0] AS overall_avg_rating,
              meta(t).id hotel_id
FROM   hotel AS t
ORDER BY overall_avg_rating DESC
LIMIT 3;
    """,
)

N1QL_REF_98 = Query(
    id="N1QL_REF_98",
    query="""
    SELECT  id, sourceairport, destinationairport,
            (SELECT s.*
             FROM route.schedule s
             WHERE s.utc > "22:00:00"
             ORDER BY s.utc)  after_10pm,
             META(route).id route_id
FROM route
WHERE sourceairport = "SFO"
LIMIT 2;
    """,
)

N1QL_REF_99 = Query(
    id="N1QL_REF_99",
    query="""
    SELECT airline, sourceairport, meta(route).id route_id
FROM  route
WHERE (SELECT raw count(*)
       FROM route.schedule as s WHERE s.day = 1)[0] > 4
LIMIT 3;
    """,
)

N1QL_REF_100 = Query(
    id="N1QL_REF_100",
    query="""
    SELECT name, cnt_reviewers, meta(t).id hotel_id
FROM hotel AS t
LET cnt_reviewers = (SELECT raw count(*)
                     FROM t.reviews AS s
                     WHERE s.ratings.Overall >= 4)[0]
WHERE  cnt_reviewers >= 6
ORDER BY cnt_reviewers DESC
LIMIT 3;
    """,
)

N1QL_REF_101 = Query(
    id="N1QL_REF_101",
    query="""
    MERGE INTO hotel t USING [{"id":"21728"},{"id":"21730"}] source
ON KEY "hotel_"|| source.id
WHEN MATCHED THEN UPDATE SET t.old_vacancy = t.vacancy, t.vacancy = false
RETURNING meta(t).id hotel_id, t.old_vacancy, t.vacancy;
""",
)

N1QL_REF_102 = Query(
    id="N1QL_REF_102",
    query="""
    UPDATE airport t1 SET airportname_dup = "high_altitude_" || airportname
WHERE  t1.geo.alt IN (SELECT RAW t2.geo.alt
                      FROM airport t2
                      WHERE t2.geo.alt > 6000)
limit 10
RETURNING t1.airportname_dup, meta(t1).id airport_id""",
)

N1QL_REF_103 = Query(
    id="N1QL_REF_103",
    query="""
    UPDATE airport t1
SET airportname_dup = "high_altitude_2 " || airportname
WHERE (SELECT RAW geo.alt
       FROM t1.geo
       WHERE geo.alt > 6000)[0] = t1.geo.alt
limit 10
RETURNING t1.airportname_dup, meta(t1).id airport_id;
    """,
)

N1QL_REF_104 = Query(
    id="N1QL_REF_104",
    query="""
    UPDATE hotel t1
SET reviews_5star = (SELECT raw t2
                     FROM t1.reviews t2
                     WHERE t2.ratings.Overall = 5
                     ORDER BY t2.author)
LIMIT 1
RETURNING t1.reviews[*].author, meta(t1).id hotel_id
    """,
)

N1QL_REF_105 = Query(
    id="N1QL_REF_105",
    query="""
    DELETE FROM hotel t
WHERE (SELECT RAW count(*)
       FROM t.reviews t2
       WHERE t2.ratings.Overall = 1 )[0] > 4
RETURNING t.name, meta(t).id hotel_id;
    """,
)

N1QL_REF_106 = Query(
    id="N1QL_REF_106",
    query="""
    SELECT airportname, meta(airport).id airport_id
FROM airport
WHERE city = "San Francisco";
    """,
)

N1QL_REF_107 = Query(
    id="N1QL_REF_107",
    query="""
    SELECT a.airportname, r.airline, meta(a).id airport_id, meta(r).id route_id
FROM airport a
JOIN route r
ON a.faa = r.sourceairport
WHERE a.city = "San Francisco"
order by a.airline
limit 10;
    """,
)

N1QL_REF_108 = Query(
    id="N1QL_REF_108",
    query="""
    SELECT 
       a.airportname AS source, r.id AS route, l.name AS airline, meta(a).id airport_id, meta(r).id route_id, meta(l).id airline_id
FROM airport AS a
JOIN route AS r 
  ON r.sourceairport = a.faa
JOIN airline AS l 
  ON r.airlineid = META(l).id
WHERE l.name = "40-Mile Air";
    """,
)

N1QL_REF_109 = Query(
    id="N1QL_REF_109",
    query="""
    SELECT a.country, meta(a).id airline_id FROM airline a
WHERE a.name = "Excel Airways";
    """,
)

N1QL_REF_110 = Query(
    id="N1QL_REF_110",
    query="""
    SELECT meta(route).id route_id, meta(airline).id airline_id FROM route
JOIN airline
ON KEYS route.airlineid
WHERE route.airlineid IN ["airline_330", "airline_225"]
    """,
)

N1QL_REF_111 = Query(
    id="N1QL_REF_111",
    query="""
    SELECT meta(airport).id airport_id FROM airport
WHERE city IN (SELECT RAW city FROM landmark)
limit 10;
    """,
)

N1QL_REF_112 = Query(
    id="N1QL_REF_112",
    query="""
    SELECT meta(hotel).id hotel_id FROM hotel WHERE city = "Gillingham"
UNION
SELECT meta(landmark).id landmark_id FROM landmark WHERE city = "Gillingham";
    """,
)

N1QL_REF_113 = Query(
    id="N1QL_REF_113",
    query="""
    SELECT t.airportname, t.city, meta(t).id airport_id
FROM   airport t
WHERE  tz = "America/Anchorage"
       AND geo.alt >= 2100;
    """,
)

N1QL_REF_114 = Query(
    id="N1QL_REF_114",
    query="""
    SELECT meta(airport).id airport_id FROM airport USE KEYS "airport_3469";
    """,
)

N1QL_REF_115 = Query(
    id="N1QL_REF_115",
    query="""
    SELECT DISTINCT airline.name, airline.callsign,
  route.destinationairport, route.stops, route.airline, meta(route).id route_id, meta(airline).id airline_id
FROM route
  JOIN airline
  ON KEYS route.airlineid
WHERE route.sourceairport = "SFO"
LIMIT 2;
    """,
)

N1QL_REF_116 = Query(
    id="N1QL_REF_116",
    query="""
    SELECT t.schedule[0].flight AS flightid, meta(t).id route_id
FROM route t
WHERE destinationairport="ALG"
LIMIT 1;
    """,
)

N1QL_REF_117 = Query(
    id="N1QL_REF_117",
    query="""
    SELECT DISTINCT route.sourceairport,
                route.airlineid,
                airline[0].callsign, 
                meta(route).id route_id,
                meta(airline).id airline_id
FROM route
NEST airline
  ON KEYS route.airlineid
WHERE route.airline = "AA"
LIMIT 4;
    """,
)

N1QL_REF_118 = Query(
    id="N1QL_REF_118",
    query="""
    SELECT r.author, meta(t).id hotel_id
FROM hotel t
UNNEST t.reviews r
LIMIT 4;
    """,
)

N1QL_REF_119 = Query(
    id="N1QL_REF_119",
    query="""
    SELECT meta(route).id route_id FROM route
WHERE ANY v IN schedule SATISFIES v.flight LIKE 'UA%' END
order by v.flight
limit 10;
    """,
)

N1QL_REF_120 = Query(
    id="N1QL_REF_120",
    query="""
    SELECT META(r).id route_id
  FROM route AS r
  WHERE r.sourceairport = "SFO" 
    AND r.destinationairport = "ATL" 
    AND ANY s IN r.schedule SATISFIES s.day BETWEEN 1 AND 5 
    AND s.flight LIKE "DL%" END; 
    """,
)

N1QL_REF_121 = Query(
    id="N1QL_REF_121",
    query="""
    SELECT  s.day, s.flight,r.sourceairport, r.destinationairport, r.stops, meta(r).id route_id
FROM route AS r
UNNEST r.schedule AS s
WHERE r.sourceairport = "SFO" AND r.destinationairport = "ATL"
      AND s.day BETWEEN 1 AND 5 AND s.flight LIKE "DL%"
ORDER BY s.day DESC
OFFSET 2
LIMIT 3;
    """,
)

N1QL_REF_122 = Query(
    id="N1QL_REF_122",
    query="""
    SELECT meta(route).id route_id FROM route
WHERE stops >=1
AND ANY v IN schedule SATISFIES v.flight LIKE 'FL%' END;
    """,
)

N1QL_REF_123 = Query(
    id="N1QL_REF_123",
    query="""
    SELECT meta().id route_id FROM route
WHERE ANY v in schedule SATISFIES [v.flight, v.day] = ["US681", 2] END;
    """,
)

N1QL_REF_124 = Query(
    id="N1QL_REF_124",
    query="""
    SELECT meta(airport).id airport_id FROM airport WHERE airportname LIKE "San Francisco%";
    """,
)

N1QL_REF_QUERIES = [
    N1QL_REF_1,
    N1QL_REF_2,
    N1QL_REF_3,
    N1QL_REF_4,
    N1QL_REF_5,
    N1QL_REF_6,
    N1QL_REF_7,
    N1QL_REF_8,
    N1QL_REF_9,
    N1QL_REF_10,
    N1QL_REF_11,
    N1QL_REF_12,
    N1QL_REF_13,
    N1QL_REF_14,
    N1QL_REF_15,
    N1QL_REF_16,
    N1QL_REF_17,
    N1QL_REF_18,
    N1QL_REF_19,
    N1QL_REF_20,
    N1QL_REF_21,
    N1QL_REF_22,
    N1QL_REF_23,
    N1QL_REF_24,
    N1QL_REF_25,
    N1QL_REF_26,
    N1QL_REF_27,
    N1QL_REF_28,
    N1QL_REF_29,
    N1QL_REF_30,
    N1QL_REF_31,
    N1QL_REF_32,
    N1QL_REF_33,
    N1QL_REF_34,
    N1QL_REF_35,
    N1QL_REF_36,
    N1QL_REF_37,
    N1QL_REF_38,
    N1QL_REF_39,
    N1QL_REF_40,
    N1QL_REF_41,
    N1QL_REF_42,
    N1QL_REF_43,
    N1QL_REF_44,
    N1QL_REF_45,
    N1QL_REF_46,
    N1QL_REF_47,
    N1QL_REF_48,
    N1QL_REF_49,
    N1QL_REF_50,
    N1QL_REF_51,
    N1QL_REF_52,
    N1QL_REF_53,
    N1QL_REF_54,
    N1QL_REF_55,
    N1QL_REF_56,
    N1QL_REF_57,
    N1QL_REF_58,
    N1QL_REF_59,
    N1QL_REF_60,
    N1QL_REF_61,
    N1QL_REF_62,
    N1QL_REF_63,
    N1QL_REF_64,
    N1QL_REF_65,
    N1QL_REF_66,
    N1QL_REF_67,
    N1QL_REF_68,
    N1QL_REF_69,
    N1QL_REF_70,
    N1QL_REF_71,
    N1QL_REF_72,
    N1QL_REF_73,
    N1QL_REF_74,
    N1QL_REF_75,
    N1QL_REF_76,
    N1QL_REF_77,
    N1QL_REF_78,
    N1QL_REF_79,
    N1QL_REF_80,
    N1QL_REF_81,
    N1QL_REF_82,
    N1QL_REF_83,
    N1QL_REF_84,
    N1QL_REF_85,
    N1QL_REF_86,
    N1QL_REF_87,
    N1QL_REF_88,
    N1QL_REF_89,
    N1QL_REF_90,
    N1QL_REF_91,
    N1QL_REF_92,
    N1QL_REF_93,
    N1QL_REF_94,
    N1QL_REF_95,
    N1QL_REF_96,
    N1QL_REF_97,
    N1QL_REF_98,
    N1QL_REF_99,
    N1QL_REF_100,
    N1QL_REF_101,
    N1QL_REF_102,
    N1QL_REF_103,
    N1QL_REF_104,
    N1QL_REF_105,
    N1QL_REF_106,
    N1QL_REF_107,
    N1QL_REF_108,
    N1QL_REF_109,
    N1QL_REF_110,
    N1QL_REF_111,
    N1QL_REF_112,
    N1QL_REF_113,
    N1QL_REF_114,
    N1QL_REF_115,
    N1QL_REF_116,
    N1QL_REF_117,
    N1QL_REF_118,
    N1QL_REF_119,
    N1QL_REF_120,
    N1QL_REF_121,
    N1QL_REF_122,
    N1QL_REF_123,
    N1QL_REF_124,
]
