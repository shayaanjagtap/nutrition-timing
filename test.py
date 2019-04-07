#!/usr/bin/env python

import json
import requests

data = {'state':'blue',
        'data':[1,2,3]}

r = requests.post('http://127.0.0.1:5000/recommend_nutrition', json=data)
print(r.text)
