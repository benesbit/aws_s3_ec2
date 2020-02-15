import boto3
from botocore.exceptions import NoCredentialsError

keys_file = open('./rootkey.csv')
lines = keys_file.readlines()
ACCESS_KEY = lines[0].rstrip()
SECRET_KEY = lines[1].rstrip()
BUCKET = "nesbit-music-app"


def upload_to_aws(local_file, s3_file):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)

    try:
        s3.upload_file(local_file, BUCKET, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False


uploaded = upload_to_aws('local_file', 's3_file_name')