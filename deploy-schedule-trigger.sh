#!/bin/bash

gcloud functions deploy schedule-trigger-function \
    --region="us-central1" \
    --runtime="python312" \
    --memory="16Gi" \
    --trigger-http \
    --entry-point="invoke" \
    --no-allow-unauthenticated \
    --source=./schedule-trigger

gcloud scheduler jobs create http schedule-trigger-function \
    --location="us-central1" \
    --schedule="0 0 * * *" \
    --uri="https://us-central1-apestel.cloudfunctions.net/schedule-trigger-function" \
    --oidc-service-account-email="199375159079-compute@developer.gserviceaccount.com" \
    --http-method=POST \
    --headers="content-type=application/json" \
    --message-body='{"bucket": "apestel", "path": "test-folder/"}'