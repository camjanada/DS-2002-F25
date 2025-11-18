#!/bin/bash

# Script: s3_upload_presign.sh
# Usage: ./s3_upload_presign.sh <local-file> <bucket-name> <expiration-seconds>

# --- Validate Arguments ---
if [ $# -ne 3 ]; then
  echo "Usage: $0 <local-file> <bucket-name> <expiration-seconds>"
  exit 1
fi

LOCAL_FILE="$1"
BUCKET="$2"
EXPIRATION="$3"

# --- Check File Exists ---
if [ ! -f "$LOCAL_FILE" ]; then
  echo "Error: File '$LOCAL_FILE' does not exist."
  exit 1
fi

# --- Upload File to S3 ---
echo "Uploading $LOCAL_FILE to s3://$BUCKET/"
aws s3 cp "$LOCAL_FILE" "s3://$BUCKET/" --acl private

if [ $? -ne 0 ]; then
  echo "Error: Failed to upload file."
  exit 1
fi

# --- Generate Presigned URL ---
echo "Generating presigned URL..."
URL=$(aws s3 presign "s3://$BUCKET/$(basename "$LOCAL_FILE")" --expires-in "$EXPIRATION")

if [ $? -ne 0 ]; then
  echo "Error: Failed to generate presigned URL."
  exit 1
fi

echo "Success! Presigned URL:"
echo "$URL"
