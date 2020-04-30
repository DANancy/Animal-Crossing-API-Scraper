#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# load .env libs
from pathlib import Path
from dotenv import load_dotenv

# import system libs
import subprocess
import os

# load .env
env_path = Path('..') / '.env'
load_dotenv(dotenv_path=env_path)


def sync_data():
    local_folder = os.getenv('LocalFolder')
    aws_bucket = os.getenv('AWSBucket')
    region = os.getenv('AWS_DEFAULT_REGION')
    subprocess.call(
        'aws s3api create-bucket --bucket {} --region {} --create-bucket-configuration LocationConstraint={}'.format(
            aws_bucket, region, region), shell=True)
    subprocess.call('aws s3api wait bucket-exists --bucket {}'.format(aws_bucket), shell=True)
    subprocess.call('aws s3 sync {} {}'.format(local_folder, 's3://' + aws_bucket), shell=True)


if __name__ == '__main__':
    sync_data()
