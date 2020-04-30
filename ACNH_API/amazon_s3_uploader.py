#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# load .env libs
from pathlib import Path
from dotenv import load_dotenv

# load libs
import boto3
from botocore.exceptions import NoCredentialsError
import os

# load .env variables
env_path = Path('..')/'rootkey.csv'
load_dotenv(dotenv_path=env_path)

def upload_to_aws():
    s3 = boto3.client(
        's3',
        aws_access_key_id = os.getenv('AWSAccessKeyId'),
        aws_secret_access_key = os.getenv('AWSSecretKey')
    )

    s3.create_bucket(Bucket='letmedoatesting3',CreateBucketConfiguration={
    'LocationConstraint': 'ap-southeast-2'})
    # s3.Object('letmedoatesting2', 'bugs.json').put(Body=open('data/bugs/bugs.json', 'rb'))

    # try:
    #     s3.upload_file(local_file,bucket,s3_file)
    #     print("Uploaded {} Successful.".format(local_file))
    # except FloatingPointError:
    #     print("The file {} was not found.".format(local_file))
    #     return False
    # except NoCredentialsError:
    #     print("Credentials not available")
    #     return False

upload_to_aws()