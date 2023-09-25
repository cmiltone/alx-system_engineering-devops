#!/usr/bin/python3
"""
script to export data in JSON format
"""


if __name__ == "__main__":
    import requests
    import sys
    import json

    id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
    emp = requests.get(url).json()
    uname = emp.get('username')
    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(id)
    tasks = requests.get(url).json()

    completed = []
    obj = {id: []}
    for task in tasks:
        obj[id].append({
            "username": uname,
            "completed": task.get('completed'),
            "task": task.get('title')
        })

    with open('{}.json'.format(id), "w") as f:
        w = json.dump(obj, f)
