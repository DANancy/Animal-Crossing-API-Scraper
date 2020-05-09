#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# import libs
import os

# import customized module
import cloud_verification as cv

# add Google Drive
drive = cv.google_verify()

def upload_files(local_folder):
    # create root folder on Google Drive
    parent_folder = drive.CreateFile({'title': local_folder, 'mimeType': 'application/vnd.google-apps.folder'})
    parent_folder.Upload()
    print("{} folder has been created on Google Drive".format(local_folder))

    # create folder info to store folder ID
    folders_info = {}
    folders_info[local_folder] = parent_folder['id']

    for root, dirs, files in os.walk(local_folder):
        parent_folder = root.split('\\')[-1]
        parent_id = ""
        if parent_folder in folders_info.keys():
            parent_id = folders_info[parent_folder]

        while True:
            if dirs:  # if dirs list is not empty
                for i in dirs:
                    if i in folders_info.keys():
                        break
                    children_drive = drive.CreateFile(
                        {'title': i, 'mimeType': 'application/vnd.google-apps.folder',
                         'parents': [{'id': parent_id}]})
                    children_drive.Upload()
                    print("{} folder has been created on Google Drive".format(i))
                    folder_id = children_drive['id']
                    folders_info[i] = folder_id

            if files:  # if files list is not empty
                count = 0
                for file in files:
                    file_drive = drive.CreateFile({'title': file, 'mimeType': 'json/png',
                                                   "parents": [
                                                       {"kind": "drive#fileLink", 'id': folders_info[parent_folder]}]})
                    file_drive.SetContentFile(os.path.join(root, file))
                    file_drive.Upload()
                    count += 1
                print("{} files has been uploaded to Google Drive under {}".format(count, root))
            break


if __name__ == "__main__":
    upload_files('data')
