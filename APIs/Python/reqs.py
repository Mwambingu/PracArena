#!/usr/bin/python3

import requests

baseurl = 'https://rickandmortyapi.com/api/'
endpoint = 'character'

def main_request(baseurl, endpoint, x):
    r = requests.get(baseurl + endpoint + f'?page={x}')
    return r.json()

def get_pages(response):
    return response['info']['pages']

def parse_json(response):
    charlist = []
    for item in response['results']:
        char = {"name": item['name'], "no_eps": len(item['episode'])}
        charlist.append(char)
    return charlist

data = main_request(baseurl, endpoint, 2)
print(type(get_pages(data)))
print(parse_json(data))


def get_all_chars_eps(baseurl, endpoint):
    response = main_request(baseurl, endpoint, 1)
    pages = get_pages(response)
    all_chars_list = []

    for page in range(pages):
        new_response = main_request(baseurl, endpoint, page+1)

        all_chars_list.extend(parse_json(new_response))

    return all_chars_list

all_chars = get_all_chars_eps(baseurl, endpoint)

print(len(all_chars))
for chars in all_chars:
    if "Rick" in chars["name"]:
        print(f'{chars["name"]} Episodes Featured: {chars["no_eps"]}')
