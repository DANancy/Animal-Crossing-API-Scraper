#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# import libs
import glob
import os

# import customized module
import cloud_verification as cv

def get_files(folder_path):
    # create a list of file and sub directories
    # names in the given directory
    file_lst = os.listdir(folder_path)
    all_files = []
    for entry in file_lst:
        # Create full path
        full_path = os.path.join(folder_path, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(full_path):
            all_files = all_files + get_files(full_path)
        else:
            all_files.append(full_path)

    return all_files

def get_parent_id(drive_folder):
    parent_folder.Upload()
    parent_id = parent_folder['id']

    return folder_id

def upload_files(inpout_folder):

    parent_folder = drive.CreateFile({'title': inpout_folder,'mimeType': 'application/vnd.google-apps.folder'})
    parent_folder.Upload()
    parent_id = parent_folder ['id']

    for root,dirs,files in os.walk(inpout_folder):
        if len(dirs) != 0:
            for i in dirs:
                folders = {}
                folders['parent'] = root.split('\\')[-1]
                folders['children'] = i


    # Create the folder
    # If no parent ID is provided this will automatically go to the root or My Drive 'directory'
    top_level_folder = drive.CreateFile({'title': input_folder,'mimeType': 'application/vnd.google-apps.folder'})
    # Upload the folder to your drive
    top_level_folder.Upload()
    # Grab the ID of the folder we just created
    parent_id = top_level_folder['id']

    # Create a sub-directory
    # Make sure to assign it the proper parent ID
    child_folder1 = drive.CreateFile({'title': 'fish', 'parents': [{'id': parent_id}]})
    child_folder1.Upload()

# def upload_files(input_folder,output_folder):
#     drive = google_verify()
#     # Login to Google Drive and create drive object
#     files_lst = get_files(input_folder)
#
#
#     # Create the folder
#     # If no parent ID is provided this will automatically go to the root or My Drive 'directory'
#     top_level_folder = drive.CreateFile({'title': input_folder, 'mimeType': 'application/vnd.google-apps.folder'})
#     # Upload the folder to your drive
#     top_level_folder.Upload()
#     # Grab the ID of the folder we just created
#     parent_id = top_level_folder['id']
#
#     # Create a sub-directory
#     # Make sure to assign it the proper parent ID
#     child_folder1 = drive.CreateFile({'title': 'fish', 'mimeType': 'application/vnd.google-apps.folder','parents': [{'id': parent_id}]})
#     child_folder1.Upload()
#     child_id1 = child_folder1['id']
#
#     child_folder2 = drive.CreateFile({'title': 'fish', 'mimeType': 'application/vnd.google-apps.folder','parents': [{'id': parent_id}]})
#     child_folder1 = drive.CreateFile({'title': 'fish', 'parents': [{'id': parent_id}]})
#
#     for file in files_lst:
#         file_drive = drive.CreateFile({'title': file})
#         file_drive.SetContentFile(file)
#         file_drive.Upload()
#         file_drive = None
#         print("{} file has been uploaded to Google Drive".format(file))
#
#     child_folder2 = drive.CreateFile({'title': 'bugs', 'parents': [{'id': parent_id}]})
#     child_id2 = child_folder2['id']
#     child_folder2.Upload()
#
#     for file in files_lst:
#         file_drive = drive.CreateFile({'title': file})
#         file_drive.SetContentFile(file)
#         file_drive.Upload()
#         file_drive = None
#         print("{} file has been uploaded to Google Drive".format(file))
#
# def create_folder(title):
#


if __name__ == "__main__":
    files = get_files('data')
    print(files)
    folders = get_folders_structure(files)
    print(folders)
    # google_verify()
    # upload_to_server('data')
