import boto3

# --- SETUP ---
s3 = boto3.client('s3', region_name="us-east-1")
bucket = 'ds2002-f25-mpj6fa'

# local file you want to upload
local_file = 'red.png'       # must exist in your current folder
s3_key = 'red.png'           # destination name in S3

# --- UPLOAD (PRIVATE) ---
with open(local_file, 'rb') as data:
    response = s3.put_object(
        Body=data,
        Bucket=bucket,
        Key=s3_key
    )

print("Upload complete.")
print("S3 key:", s3_key)
