#!/usr/bin/env python3

import urllib.request
import boto3
import sys
import argparse
import os

def main():
    parser = argparse.ArgumentParser(description="Download a file and upload it to S3 with presigned URL.")
    parser.add_argument("url", help="URL of the file to download")
    parser.add_argument("bucket", help="S3 bucket name")
    parser.add_argument("key", help="S3 object name/key to save as")
    parser.add_argument("expires", type=int, help="Presigned URL expiration time in seconds")

    args = parser.parse_args()

    # Step 1: Download file
    print(f"Downloading file from {args.url} ...")
    urllib.request.urlretrieve(args.url, args.key)
    print(f"Saved file as {args.key}")

    # Step 2: Upload to S3
    s3 = boto3.client("s3")

    print(f"Uploading {args.key} to s3://{args.bucket}/{args.key} ...")
    try:
        s3.upload_file(args.key, args.bucket, args.key)
        print("Upload complete.")
    except Exception as e:
        print("Upload failed:", e)
        sys.exit(1)

    # Step 3: Generate presigned URL
    print("Generating presigned URL...")
    try:
        url = s3.generate_presigned_url(
            "get_object",
            Params={"Bucket": args.bucket, "Key": args.key},
            ExpiresIn=args.expires
        )
        print("\nPresigned URL:")
        print(url)
    except Exception as e:
        print("Failed to generate presigned URL:", e)

if __name__ == "__main__":
    main()
