# Animal-Crossing-API-Scraper
This project is built to extract jsons and images for fish & bugs from animal crossing API, and upload to Cloud Service or send emails automatically. 


### Support Service
* Google Drive
* Amazon S3
* SMTP Server

### ACNH API Scraper Architecture
![Image of Diagram](images/API_Scraper_Diagram.png)


### Project Overview
```text
.
├── ACNH_API                   # Project files for ANCH API
│   ├── cloud_verification     # self-defined module
│   ├── api_extractor          # spider for ACNH API
│   ├── google_drive_uploader  # upload all files to Google Drive automatically
│   ├── amazon_s3_cli          # upload all files to Amazon S3 automatically using CLI tool 
│   ├── emails_distributor     # zip all files and distribute emails automatically
│   └── api_sample.json        # animal crossing api call sample
├── images                     # images for diagram 
├── .env-sample                # Rename to .env to setup environmental variables             
├── LICENSE
├── .gitignore
├── requirements.txt
└── README.md
```


### Setup
1.Clone the whole project
```shell script
$ git clone https://github.com/DANancy/API-Scraper-Starter.git
```

2.Add Self-Defined Module -> cloud_verification.py (only for Google)
```python
import pandas
# get package folder
print(pandas.__file__)
# copy this module to the package folder
```

3.Create .env File
```text
# SMTP Server Setup
MAIL_SERVER=smtp.gmail.com
MAIL_USE_TLS=True
MAIL_USE_SST=False
MAIL_PORT=587
MAIL_USERNAME=example@gmail.com
MAIL_PASSWORD=*****
RECIPIENTS=["example@gmail.com","example1@gmail.com","example2@gmail.com"]

# AWS Setup
AWS_ACCESS_KEY_ID=*****
AWS_SECRET_ACCESS_KEY=*****
AWS_DEFAULT_REGION=ap-southeast-2
LocalFolder=data
AWSBucket=data
```

4.Setup Cloud Server/SMTP Server
* [Setup Google Drive API](https://medium.com/@annissouames99/how-to-upload-files-automatically-to-drive-with-python-ee19bb13dda)
* [Get Amazon Access Key](https://medium.com/@shamnad.p.s/how-to-create-an-s3-bucket-and-aws-access-key-id-and-secret-access-key-for-accessing-it-5653b6e54337)
* [Setup SMTP Server](https://www.siteground.com/kb/google_free_smtp_server/)

4.Run API Extractor
```shell script
$ python ACNH_API/api_extractor.py
```

5.Run Uploader based on your needs
```shell script
$ python ACNH_API/google_drive_uploader.py
```
```shell script
$ python ACNH_API/amzon_s3_cli.py
```
```shell script
$ python ACNH_API/emails_distributor.py
```


### References
* [PyDrive](https://gsuitedevs.github.io/PyDrive/docs/build/html/index.html)
* [Flask-Mail](https://pythonhosted.org/Flask-Mail/)
* [subprocess](https://docs.python.org/3/library/subprocess.html)
* [AWS Sync](https://docs.aws.amazon.com/cli/latest/reference/s3/sync.html)
* [awscil](https://pypi.org/project/awscli/)
* [WatchDog](https://python-watchdog.readthedocs.io/en/v0.10.2/)

### Credits
* [Mutoo](https://github.com/mutoo) - Wash dishes and take care of baby while I am programming :D
