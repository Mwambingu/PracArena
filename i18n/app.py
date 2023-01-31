#!/usr/bin/env python3

from flask import Flask, jsonify

app = Flask(__name__)


posts = [
    {
        "id": 1,
        "title_en": "Title in English",
        "description_en": "Description in English",
        "title_de": "Title in German",
        "description_de": "Description in German",
    },
    {
        "id": 2,
        "title_en": "Title in English",
        "description_en": "Description in English",
        "title_de": "Title in German",
        "description_de": "Description in German",
    }
]


@app.route('/')
def index():
    lang = 'de'

    p = list(map(lambda post: translate(post, lang), posts ))
    
    return jsonify(p)


def translate(post, lang):
    return {
        "id": post['id'],
        "title": post['title_' + lang],
        "description": post['description_' + lang]
    }


app.run(port=5000)
