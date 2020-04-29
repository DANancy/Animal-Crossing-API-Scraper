#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# import libs
import requests
import json
import os
import io
from PIL import Image

def api_cal(url):
    result = None
    for i in range(0, 3):  # define retry times
        ok = False
        while True:
            try:
                result = requests.get(url)
                if result.status_code == 200:
                    ok = True
                    break
            except requests.exceptions.Timeout:
                print("Request timeout, retry url: {} times.".format(url, i + 1))
                continue
            except requests.exceptions.TooManyRedirects:
                print("Too Many Redirects, please check url: {}.".format(url))
                break
            except requests.exceptions.RequestException as err:
                raise SystemExit(err)
        if ok:
            break
    return result

def create_folder(folder_path):
    try:
        # Create target Directory
        os.makedirs(folder_path, exist_ok=True)
        print("Directory ", folder_path, " Created.")
    except FileExistsError:
        print("Directory ", folder_path, " already exists.")

def get_info(urlst, folder_path):
    for url in urlst:
        info = api_cal(url)
        if info is None:
            raise ValueError("API Call Failed.")

        type = url.split('/')[-1]
        output_dir = "{}/{}".format(folder_path, type)
        create_folder(output_dir)

        output_file = '{}/{}.json'.format(output_dir, type)
        with open(output_file, 'w', encoding='utf-8') as outfile:
            json.dump(info.json(), outfile, sort_keys=True, indent=4, ensure_ascii=False)
            print("File ", output_file, " Created.")


def get_images(urlst, folder_path):
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            print("Processed {}.".format(filename))
            type = os.path.splitext(os.path.basename(filename))[0]
            with open(os.path.join(root, filename), encoding='utf-8') as json_file:
                data = json.load(json_file)
                for key in data:
                    count = 1
                    id = data[key]['id']
                    for url in urlst:
                        print("Call {}/{}/{}".format(url, type, id))
                        result = api_cal("{}/{}/{}".format(url, type, id))
                        if result is None:
                            raise ValueError("API Call Failed.")

                        subtype = url.split('/')[-1]
                        output_dir = "{}/{}/{}".format(folder_path, type, subtype)
                        create_folder(output_dir)

                        image_name = "{}/{}.png".format(output_dir, id)
                        image = Image.open(io.BytesIO(result.content))
                        image.save(image_name,optimize=True,quality=80)
                        print("{} created.".format(image_name))
                    count += 1
                print("{} Images Created".format(count))

if __name__ == "__main__":
    info_lst = ['http://acnhapi.com/fish',
               'http://acnhapi.com/bugs']

    images_lst = ['http://acnhapi.com/icons',
             'http://acnhapi.com/images']

    get_info(info_lst, 'data')
    get_images(images_lst,'data')

