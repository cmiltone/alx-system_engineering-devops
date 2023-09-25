#!/usr/bin/python3
"""
script that, using this REST API,
for a given employee ID,
returns information about his/her TODO list progress
"""


if __name__ == "__main__":
    import requests
    import sys


    id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
    emp = requests.get(url).json()
    uname = emp.get('name')
    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(id)
    tasks = requests.get(url).json()

    total = len(tasks)
    done = 0
    for task in tasks:
        if task.get('completed') is True:
            done += 1

    print('Employee {} is done with tasks({}/{}):'.format(uname, done, total))
    for task in tasks:
        print("\t {}".format(task.get('title')))
