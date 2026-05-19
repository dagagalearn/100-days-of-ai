import boto3
from botocore.exceptions import ClientError

BUCKET = "models_94"
MODEL_NAME = "titanic_model.joblib"

def upload_file(filename, bucket, s3_key):
    s3 = boto3.client("s3")
    try:
        s3.upload_file(filename,bucket,s3_key)
        print("Uploaded")
    except ClientError as e:
        print("Unseccesful: ",e)

def download_file(bucket,s3_key,filename):
    s3 = boto3.client("s3")
    try:
        s3.download_file(bucket,s3_key,filename)
        print("Success!")
    except ClientError as e:
        print("Unsecussful:", e)

def list_models(bucket, prefix="model/"):
    s3 = boto3.client("s3")
    try:
        response = s3.list_objects_v2(Prefix=prefix,Bucket=bucket)
        if "Contents" in response:
            for obj in response["Contents"]:
                print(f"{obj['Key']} - {obj['Size']}bytes")
        else:
            print("No models found")
    except ClientError as e:
        print(e)
     
# You can add your credentials later or test with Localstack or Moto
