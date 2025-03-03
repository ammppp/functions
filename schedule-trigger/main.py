import functions_framework
import pandas as pd
import pandas_gbq
from google.cloud import bigquery, storage

@functions_framework.http
def invoke(request):

    request_json = request.get_json(silent=True)
    request_args = request.args

    bucket = request_json["bucket"]
    path = request_json["path"]

    storage_client = storage.Client()
    bq_client = bigquery.Client()

    blobs = storage_client.list_blobs(bucket, prefix=path)

    print("Processing blobs...")
    for blob in blobs:
        print(blob)

        table = blob.name.replace("/", "_")
        table = table.replace(".", "_")
        df = pd.read_csv(f"gs://{bucket}/{blob.name}")
        pandas_gbq.to_gbq(
            df,
            f"apestel.{table}",
            project_id=bq_client.project,
            if_exists="replace"
        )

        print("Loaded table")

    return "Success"
