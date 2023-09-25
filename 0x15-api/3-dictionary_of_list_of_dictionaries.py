#!/usr/bin/python3
"""
script to export data in JSON format
for all employees
"""


if __name__ == "__main__":
    import requests
    import json

    url = 'https://jsonplaceholder.typicode.com/users/'
    emps = requests.get(url).json()
    obj = {}
    for emp in emps:
        obj[emp.get('id')] = []

    for emp in emps:
        id = emp.get('id')
        uname = emp.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(id)
        tasks = requests.get(url).json()

        for task in tasks:
            obj[id].append({
                "username": uname,
                "completed": task.get('completed'),
                "task": task.get('title')
            })

        with open('todo_all_employees.json', "w") as f:
            w = json.dump(obj, f)
