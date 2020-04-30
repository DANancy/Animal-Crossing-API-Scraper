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

def zip_dir(local_folder):
    output_folder = '{}.zip'.format(local_folder)

    # define zip handler
    zip_handle = zipfile.ZipFile(output_folder, 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk(local_folder):
        for file in files:
            zip_handle.write(os.path.join(root, file))
    zip_handle.close()

    # return folder name
    return output_folder

def distributor(local_folder):
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
        # setup basic info, write complex html to customize if you want
        msg = Message(subject= "This is info from ACNH API Call",
                     body = "This is awesome",
                     html=""" <img src="https://github.com/DANancy/Animal-Crossing-API-Scraper/blob/master/Images/animal-crossing.jpg" width="800" height="600" />""",
                     sender=app.config.get("MAIL_USERNAME"),
                     recipients=json.loads(os.getenv("Recipients")))

        # add attachment to the email
        with app.open_resource(local_folder) as fp:
            msg.attach(local_folder, "folder/zip", fp.read())
        mail.send(msg)

if __name__ == "__main__":
    local_folder = zip_dir('data')
    distributor(local_folder)
