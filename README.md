# Animal-Crossing-API-ScraperAPI-Scraper
This project is built to extract jsons and images from animal crossing API, and upload to Cloud Service or send to emails automatically. 


### Support Service
* Google Drive (Completed)
* Amzon S3
* SMTP Server


### Project Overview
```text
.
├── ACNH_API                   # Project files for ANCH API
│   ├── cloud_verification.py  # self-defined module
│   ├── api_extractor          # spider for ACNH API
│   ├── google_drive_uploader  # upload all files to Google Drive automatically
│   └── api_sample.json        # animal crossing api call sample
├── LICENSE
├── .gitignore
├── requirements.txt
└── README.md
```


### Setup
1. Clone this whole project
```shell script
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
```shell script
$ python ACNH_API/api_extractor.py
```

5.Run Uploader
```shell script
$ python ACNH_API/google_drive_uploader.py
```


### References
* [PyDrive](https://gsuitedevs.github.io/PyDrive/docs/build/html/index.html)


### Credits
* [Mutoo](https://github.com/mutoo) - Wash dishes and take care of baby while I am programming :D
