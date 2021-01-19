import os

import boto3

ENDPOINT_URL = os.environ['ENDPOINT_URL']
ACCESS_KEY = os.environ['MINIO_ACCESS_KEY']
SECRET_KEY = os.environ['MINIO_SECRET_KEY']
DATA_PREFIX = os.environ['DATA_PREFIX']
BUCKET_NAME = os.environ['BUCKET_NAME']
FILENAME = os.environ['FILENAME']

def upload():
    # Creating a S3 resource
    s3_resource = boto3.resource('s3', 
        endpoint_url=ENDPOINT_URL,
        aws_access_key_id=ACCESS_KEY, 
        aws_secret_access_key=SECRET_KEY)

    # Create a bucket
    bucket_response = s3_resource.create_bucket(Bucket=BUCKET_NAME)
    print(bucket_response)

    # Retrieve the list of existing buckets
    response = s3_resource.meta.client.list_buckets()

    # Output the bucket names
    print('Existing buckets:')
    for bucket in response['Buckets']:
        print(f'  {bucket["Name"]}')

    # Key (name) of the file inside Bucket
    FILEKEY = DATA_PREFIX + FILENAME

    # Upload the file to the bucket
    s3_resource.meta.client.upload_file(
        Filename=FILENAME, Bucket=BUCKET_NAME,
        Key=FILEKEY, ExtraArgs={"Metadata": {"type": "text_file"}}) # Metadata is for tagging

    my_bucket = s3_resource.Bucket(name=BUCKET_NAME)

    for obj in my_bucket.objects.all():
        print(obj.key)

    for obj in my_bucket.objects.filter(Prefix=DATA_PREFIX):
        print(obj.key)

if __name__ == "__main__":
    try:
        upload()
    except Exception as e:
        print("Error occurred.", e)