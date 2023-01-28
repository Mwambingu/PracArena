#!/usr/bin/python3
import requests

def add(a, b):
    return a + b

def len_joke():
    joke = get_joke()
    return len(joke)

def get_joke():
    url = 'https://v2.jokeapi.dev/joke/Any'
    joke = []

    response = requests.get(url)

    if response.status_code == 200:
        r = response.json()
        if 'setup' in r:
            joke = r['setup'], r['delivery']
        else:
            joke = 'No setup'
    else:
        joke = 'No Jokes'

    return joke

if __name__ == '__main__':
    print(get_joke())
