import boto3
import requests

# Configuration
bucket_name = "ds2002-f25-<yourID>"
local_file = "test.gif"
object_name = "test.gif"
expires_in = 604800  # 7 days

# Fetch file from internet
url = "https://media.giphy.com/media/ICOgUNjpvO0PC/giphy.gif"
r = requests.get(url)
with open(local_file, 'wb') as f:
    f.write(r.content)

# S3 client
s3 = boto3.client('s3', region_name="us-east-1")

# Upload file (private)
s3.upload_file(local_file, bucket_name, object_name)

# Generate presigned URL
url = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': bucket_name, 'Key': object_name},
    ExpiresIn=expires_in
)
print("Presigned URL:", url)
