#!/usr/bin/env python
# coding: utf-8
import requests

r = requests.get('https://reqres.in/api/users',verify=False)
if r.status_code != 200:
    print("Error GET /tasks/ {}".format(r.status_code))

names = []

for resp in r.json()['data']:
    p = [resp["first_name"],resp["last_name"]]
    names.append(' '.join(p))

print(names)    #Final Answer
