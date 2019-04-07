#!/usr/bin/env python
from flask import Flask, request, abort

app = Flask(__name__)

from recommend_nutrition import recommend_nutrition

@app.route('/')
def say_hi():
    return "hello"

@app.route('/recommend_nutrition', methods=["POST"])
def get_nutrition_recommendation():

    try:
        content = request.get_json()

        state = content['state'] if 'state' in content.keys() else ''
        data  = content['data']

        nutrition_recommendation = recommend_nutrition(state=state, watch_data=data)
        return nutrition_recommendation

    except:
        abort(404)


if __name__ == '__main__':
    app.run()
