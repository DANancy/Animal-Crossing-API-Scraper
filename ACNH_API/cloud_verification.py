#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# import pandas
# print(pandas.__file__)
# copy this module to the package folder

# import libs for google driver
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def google_verify():
    g_login = GoogleAuth()
    # Try to load saved client credentials
    g_login.LoadCredentialsFile("mycreds.txt")

    if  g_login.credentials is None:
        # Authenticate if they're not there
        g_login.LocalWebserverAuth()
    elif  g_login.access_token_expired:
        # Refresh them if expired
        g_login.Refresh()
    else:
        # Initialize the saved creds
        g_login.Authorize()
    # Save the current credentials to a file
    g_login.SaveCredentialsFile("mycreds.txt")

    g_login.LocalWebserverAuth()
    drive = GoogleDrive(g_login)
    return drive
