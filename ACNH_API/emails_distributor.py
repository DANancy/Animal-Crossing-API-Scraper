#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# load .env libs
from pathlib import Path
from dotenv import load_dotenv

# import libs
from flask import Flask
from flask_mail import Mail, Message
import os
import json
import zipfile

# load .evn variables
env_path = Path('..') / '.env'
load_dotenv(dotenv_path=env_path)

def zip_dir(folder_path):
    output_folder = '{}.zip'.format(folder_path)

    # define zip handler
    zip_handle = zipfile.ZipFile(output_folder, 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            zip_handle.write(os.path.join(root, file))
    zip_handle.close()

    # return folder name
    return output_folder

def distributor(folder):
    app = Flask(__name__)

    mail_settings = {
        "MAIL_SERVER": os.getenv("MAIL_SERVER"),
        "MAIL_USE_TLS": os.getenv("MAIL_USE_TLS"),
        "MAIL_USE_SST": os.getenv("MAIL_USE_SST"),
        "MAIL_PORT": os.getenv("MAIL_PORT"),
        "MAIL_USERNAME": os.getenv("MAIL_USERNAME"),
        "MAIL_PASSWORD": os.getenv("MAIL_PASSWORD")
    }

    app.config.update(mail_settings)
    mail = Mail(app)
    with app.app_context():
        msg = Message(subject= "This is info from ACNH API Call",
                     body = "This is awesome",
                     html=""" <img src="animal_crossing.png" width="800" height="600" />""",
                     sender=app.config.get("MAIL_USERNAME"),
                     recipients=json.loads(os.getenv("Recipients")))

        with app.open_resource(folder) as fp:
            msg.attach(folder, "folder/zip", fp.read())

        mail.send(msg)

if __name__ == "__main__":
    folder = zip_dir('data')
    distributor(folder)
