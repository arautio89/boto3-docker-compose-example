import os
import time

import boto3

ENDPOINT_URL = os.environ['ENDPOINT_URL']
ACCESS_KEY = os.environ['MINIO_ACCESS_KEY']
SECRET_KEY = os.environ['MINIO_SECRET_KEY']
DATA_PREFIX = os.environ['DATA_PREFIX']
BUCKET_NAME = os.environ['BUCKET_NAME']
FILENAME = os.environ['FILENAME']

def download():
    s3_resource = boto3.resource('s3', 
        endpoint_url=ENDPOINT_URL,
        aws_access_key_id=ACCESS_KEY, 
        aws_secret_access_key=SECRET_KEY)

    # Key (name) of the file inside Bucket
    FILEKEY = DATA_PREFIX + FILENAME

    # Try to download the file
    while True:
        try:
            s3_resource.meta.client.download_file(BUCKET_NAME, FILEKEY, FILENAME)
            break
        except Exception as e:
            print(f"Couldn't find {FILEKEY}...")
            print(e)
            time.sleep(1)
    
    with open(FILENAME) as f:
        file_content = f.readlines()

    print(file_content)

if __name__ == "__main__":
    try:
        download()
    except Exception as e:
        print("Error occurred.", e)