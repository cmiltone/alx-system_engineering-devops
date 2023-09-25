#!/usr/bin/python3
"""
script that, using this REST API,
for a given employee ID,
returns information about his/her TODO list progress
"""


if __name__ == "__main__":
    import requests
    import sys
    import csv

    id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
    emp = requests.get(url).json()
    uname = emp.get('username')
    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(id)
    tasks = requests.get(url).json()

    completed = []
    for task in tasks:
        completed.append({
            "id": id,
            "username": uname,
            "completed": task.get('completed'),
            "task": task.get('title')
        })

    with open('{}.csv'.format(id), "w") as f:
        w = csv.DictWriter(
            f,
            fieldnames=["id", "username", "completed", "task"],
            quotechar='"',
            quoting=csv.QUOTE_ALL
        )
        for task in completed:
            w.writerow(task)
