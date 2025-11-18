import boto3

s3 = boto3.client('s3', region_name="us-east-1")
bucket = 'ds2002-f25-mpj6fa'

local_file = 'google_logo.png'
s3_key = 'google_logo.png'

with open(local_file, 'rb') as data:
    response = s3.put_object(
        Body=data,
        Bucket=bucket,
        Key=s3_key,
        ACL='public-read'
    )

print("Public upload complete.")
