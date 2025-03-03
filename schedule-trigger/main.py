import functions_framework

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

        #df = pd.read_csv(f"gs://{bucket}/{name}")
        #pandas_gbq.to_gbq(
        #    df,
        #    "apestel.function_loaded_table",
        #    project_id=bq_client.project,
        #    if_exists="replace"
        #)

        print("Loaded table")

    return "Success"
