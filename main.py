import argparse
import os
import sys
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("user_url")
    return parser

def is_shorten_links(url):
    short_domain = "vk.cc"
    parcel_url = urlparse(url).netloc
    return parcel_url == short_domain


def get_shorten_url(token,url):
        url_src= 'https://api.vk.ru/method/utils.getShortLink'
        payload = {
            'url' : url,
            "access_token" : token,
            'v': '5.131'

        }
        response = requests.get(f'{url_src}', params=payload)
        response.raise_for_status()
        short_url = response.json()
        return short_url['response']['short_url']


def get_click_counter(token,url):
    url_src= 'https://api.vk.com/method/utils.getLinkStats'
    payload = {
        'key': url.split('/')[-1],
        'access_token': token,
        'v': '5.131'
    }
    response = requests.get(url_src, params=payload)
    click_count= response.json()
    if click_count['response']['stats']:
        return click_count['response']['stats'][0]['views']
    else:
        return 0




def main():
    load_dotenv()
    access_token = os.getenv("VK_TOKEN")
    parser = create_parser()
    user_input = parser.parse_args(sys.argv[1:])
    try:
        if is_shorten_links(user_input.user_url):
            print(get_click_counter(access_token, user_input.user_url))
        else:
            print(get_shorten_url(access_token, user_input.user_url))
    except requests.exceptions.RequestException as err:
        print(f'Ошибка при выполнении запроса: {err}')


if __name__ == "__main__":
    main()





