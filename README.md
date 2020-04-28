# API-Scraper-Starter
### Overview
This project is built to extract jsons and images from animal crossing API, and upload to Cloud Service or send to emails automatically. 

### Support Service
* Google Drive
* Amzon S3
* SMTP Server

### Setup
1. Clone this whole project
```
$ git clone https://github.com/DANancy/API-Scraper-Starter.git
```
2. Add Self-Defined Module -> cloud_verification.py
```python
import pandas
# get package folder
print(pandas.__file__)
# copy this module to the package folder
```
3. Setup Cloud Server/SMTP Server
* [Setup Google Drive API](https://medium.com/@annissouames99/how-to-upload-files-automatically-to-drive-with-python-ee19bb13dda)
* Amzon S3
* SMTP Server

4.Run API Extractor
5.Run Uploader

### References
* [PyDrive](https://gsuitedevs.github.io/PyDrive/docs/build/html/index.html)