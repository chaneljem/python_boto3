# Get creation date of S3 bucket
import boto3
s3_resource = boto3.client("s3")
response = s3_resource.list_buckets()["Buckets"]
print(response)
