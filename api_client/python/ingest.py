from timesketch_api_client import config
from timesketch_api_client.client import TimesketchApi
import requests
import json
import uuid

max_value = 3  # amount of messages in timeline and amount of timelines
unique_id = str(uuid.uuid4())
OPENSEARCH_INDEX_NAME = unique_id
TIMELINE_NAME = unique_id


def insertData(msgNumber):
    headers = {"Content-Type": "application/json"}
    data = {
        "message": f"A message number {msgNumber}",
        "timestamp": 123456789,
        "datetime": "2015-07-24T19:01:01+00:00",
        "timestamp_desc": "Write time",
        "extra_field": "extratxt",
        "__ts_timeline_filter_id": msgNumber,
    }
    requests.post(
        f"http://localhost:9200/{OPENSEARCH_INDEX_NAME}/_doc",
        headers=headers,
        data=json.dumps(data),
    )


def ingest():
    ts_client = config.get_client()
    sketch = ts_client.create_sketch(  # Create new sketch
        name=f"Sketch {unique_id}", description=f"Sketch {unique_id} description"
    )
    print(f"Sketch id: {sketch.id} with uuid: {unique_id} has been created")

    for i in range(
        0, max_value
    ):  # Generate as many Timelines from the opensearch database as max_value allows
        sketch.generate_timeline_from_es_index(
            es_index_name=OPENSEARCH_INDEX_NAME,
            timeline_filter_id=i,
            name=f"Timeline #{i} {TIMELINE_NAME}",
            provider="test_direct_injection.py",
            context=f"python test_direct_ingestion.py",
        )
        print(f"Timeline: #{i} {TIMELINE_NAME} has been created")


for i in range(
    0, max_value
):  # Insert data into opensearch database as many times as max_value allows
    insertData(i)
ingest()  # ingest data into Timesketch
