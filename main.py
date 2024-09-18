import requests
import os

access_token = os.getenv("TOKEN_VK")


def is_shorten_links(url):
    try:
        response = requests.head(url, allow_redirects=True)
        check_url = response.url
        if check_url==url+"/":
            data = shorten_link(access_token,url)
        else:
            data = click_counter(access_token,url)
        return data
    except requests.exceptions.HTTPError:
        print('HTTPError')
        return None
    except Exception as err:
        print(f'Произошла ошибка: {err}')
        return None



def shorten_link(token,url):
    url_src= 'https://api.vk.ru/method/utils.getShortLink'
    payload = {
        'url' : url,
        "access_token" : token,
        'v': '5.131'

    }
    try:
        response = requests.get(f'{url_src}', params=payload)
        response.raise_for_status()
        data = response.json()
        # print(f"Сокращенная ссылка: {data['response']['short_url']}")
        return data['response']['short_url']
    except requests.exceptions.HTTPError:
        print('HTTPError')
        return None
    except Exception as err:
        print(f'Произошла ошибка: {err}')
        return None


def click_counter(token,url):
    url_src= 'https://api.vk.com/method/utils.getLinkStats'
    payload = {
        'key': url.split('/')[-1],
        'access_token': access_token,
        'v': '5.131'
    }
    try:
        response = requests.get(url_src, params=payload)
        data = response.json()
        return data['response']['stats'][0]['views']
    except requests.exceptions.HTTPError:
        print('HTTPError')
        return None
    except Exception as err:
        print(f'Произошла ошибка: {err}')
        return None



if __name__ == "__main__":
    user_input = input("Введите ссылку: ")
    print(is_shorten_links(user_input))





