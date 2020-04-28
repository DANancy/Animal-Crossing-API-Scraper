#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# import libs
import glob
import os

# import customized module
import cloud_verification as cv

# add Google Drive
drive = cv.google_verify()


# def get_files(folder_path):
#     # create a list of file and sub directories
#     # names in the given directory
#     file_lst = os.listdir(folder_path)
#     all_files = []
#     for entry in file_lst:
#         # Create full path
#         full_path = os.path.join(folder_path, entry)
#         # If entry is a directory then get the list of files in this directory
#         if os.path.isdir(full_path):
#             all_files = all_files + get_files(full_path)
#         else:
#             all_files.append(full_path)
#
#     return all_files


def upload_files(input_folder):
    # create root folder on Google Drive
    parent_folder = drive.CreateFile({'title': input_folder, 'mimeType': 'application/vnd.google-apps.folder'})
    parent_folder.Upload()
    print("{} folder has been created on Google Drive".format(input_folder))

    # create folder info to store folder ID
    folders_info = {}
    folders_info[input_folder] = parent_folder['id']

    for root, dirs, files in os.walk(input_folder):
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
