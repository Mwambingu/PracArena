#!/usr/bin/python3

import requests
import random

baseurl = 'https://rickandmortyapi.com/api/'

endpoint = 'character'

r = requests.get(baseurl + endpoint)

print(r)
print(type(r))

data = r.json()

print(type(data))


print(data['info'])
pages = data['info']['pages']

r_characters = requests.get(baseurl + 'character')
r_location = requests.get(baseurl + 'location')
r_episodes = requests.get(baseurl + 'episode')

print(r_characters)
print(r_location)
print(r_episodes)

chars = r_characters.json()
lctn = r_location.json()
eps = r_episodes.json()

for key in chars.keys():
    print(f"{key}: {type(key)}")

char_info = chars['info']
char_results = chars['results']

print(char_info)
print(type(char_results))

#print(char_results[0])
char_list = []
for char_obj in char_results:
    char_list.append(char_obj['name'])

for char in char_list:
    print(char)
    
#print("Found {}!".format(char_obj['name']))
rnm_char = char_obj

for k, v in rnm_char.items():
    if k not in ['location', 'images', 'episode', 'type', 'created']:
        print("{}: {}".format(k, v))
