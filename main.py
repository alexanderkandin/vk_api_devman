import requests
from dotenv import load_dotenv
import os
from urllib.parse import urlparse


def is_shorten_links(url):
    short_domain = "vk.cc"
    parcel_url = urlparse(url).netloc
    return parcel_url == short_domain


def shorten_link(token,url):
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


def click_counter(token,url):
    url_src= 'https://api.vk.com/method/utils.getLinkStats'
    payload = {
        'key': url.split('/')[-1],
        'access_token': access_token,
        'v': '5.131'
    }
    response = requests.get(url_src, params=payload)
    click_count= response.json()
    if click_count['response']['stats']:
        return click_count['response']['stats'][0]['views']
    else:
        return 0




if __name__ == "__main__":
    load_dotenv()
    access_token = os.getenv("VK_TOKEN")
    user_input = input("Введите ссылку: ")
    try:
        if is_shorten_links(user_input):
            print(click_counter(access_token, user_input))
        else:
            print(shorten_link(access_token, user_input))
    except requests.exceptions.RequestException as err:
        print(f'Ошибка при выполнении запроса: {err}')





