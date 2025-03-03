import functions_framework

# Triggered by a change in a storage bucket
@functions_framework.cloud_event
def invoke(cloud_event):
    data = cloud_event.data

    event_id = cloud_event["id"]
    event_type = cloud_event["type"]

    bucket = data["bucket"]
    name = data["name"]
    metageneration = data["metageneration"]
    timeCreated = data["timeCreated"]
    updated = data["updated"]

    print(f"Event ID: {event_id}")
    print(f"Event type: {event_type}")
    print(f"Bucket: {bucket}")
    print(f"File: {name}")
    print(f"Metageneration: {metageneration}")
    print(f"Created: {timeCreated}")
    print(f"Updated: {updated}")

    import pandas as pd
    import pandas_gbq
    from google.cloud import bigquery, storage
    import os

    # Initialize clients
    storage_client = storage.Client()
    bq_client = bigquery.Client()

    df = pd.read_csv(f"gs://{bucket}/{name}")
    pandas_gbq.to_gbq(
        df,
        "apestel.aaa_aaa_aaa_notebook",
        project_id=bq_client.project,
        if_exists="replace"
    )
