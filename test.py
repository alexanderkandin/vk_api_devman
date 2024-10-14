import requests
import os
from urllib.parse import urlparse
token = '038c5c27038c5c27038c5c2787009271650038c038c5c27656b8adcdc9828846e2a2091'

def shorten_link(token, url):
    url_src = 'https://api.vk.ru/method/utils.getShortLink'
    payload = {
        'url': url,
        "access_token": token,
        'v': '5.131'

    }
    try:
        response = requests.get(f'{url_src}', params=payload)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.HTTPError:
        print('HTTPError')
        return None


print(shorten_link(token,"https://mail"))
# https://mail.ru