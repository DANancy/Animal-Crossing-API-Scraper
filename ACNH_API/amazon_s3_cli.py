#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# load .env libs
from pathlib import Path
from dotenv import load_dotenv

# import system libs
import subprocess
import os

# import watchdog libs
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

# load .env
env_path = Path('..') / '.env'
load_dotenv(dotenv_path=env_path)


def on_event(event):
    if event.event_type in ['created', 'deleted', 'move']:
        # Take any action here when a file is first created.
        sync_data()
        print("{} - {}.".format(event.event_type, event.src_path))


def create_event_handler():
    patterns = "*"
    ignore_patterns = ""
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
    my_event_handler.on_moved = on_event
    my_event_handler.on_created = on_event
    my_event_handler.on_deleted = on_event

    return my_event_handler


def folder_watcher(local_folder, my_event_handler):
    go_recursively = True
    my_observer = Observer()
    my_observer.schedule(my_event_handler, local_folder, recursive=go_recursively)

    my_observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()


def sync_data():
    local_folder = os.getenv('LocalFolder')
    aws_bucket = os.getenv('AWSBucket')
    region = os.getenv('AWS_DEFAULT_REGION')
    process = subprocess.Popen('aws s3api head-bucket --bucket {}'.format(aws_bucket), stdout=subprocess.PIPE,
                               shell=True)
    if len(process.stdout.readlines()) != 0:
        subprocess.call(
            'aws s3api create-bucket --bucket {} --region {} --create-bucket-configuration LocationConstraint={}'.format(
                aws_bucket, region, region), shell=True)
    subprocess.call('aws s3api wait bucket-exists --bucket {}'.format(aws_bucket), shell=True)

    subprocess.call('aws s3 sync {} {}'.format(local_folder, 's3://' + aws_bucket), shell=True)


if __name__ == '__main__':
    my_event_handler = create_event_handler()
    folder_watcher('data', my_event_handler)
