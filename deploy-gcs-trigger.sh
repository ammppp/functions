#!/bin/bash

gcloud functions deploy gcs-trigger-function \
    --region="us-central1" \
    --runtime="python312" \
    --memory="16Gi" \
    --trigger-bucket="apestel" \
    --trigger-location="us" \
    --entry-point="invoke" \
    --no-allow-unauthenticated \
    --source=./gcs-trigger
