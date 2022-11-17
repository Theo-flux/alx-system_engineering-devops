#!/usr/bin/python3
"""
python script that returns todo list progress from
an api
"""
from sys import argv
import requests

if __name__ == "__main__":

    id = argv[1]
    baseUrl = 'https://jsonplaceholder.typicode.com'
    urlForTodo = '{}/todos?userId={}'.format(baseUrl, id)
    urlForUser = '{}/users?id={}'.format(baseUrl, id)
    name = ""
    completed_tasks = []
    total_tasks = 0

    with requests.get(urlForUser) as res:
        result = res.json()
        name = result[0].get('name')

    with requests.get(urlForTodo) as res:
        result = res.json()
        total_tasks = len(result)

        for k in range(0, len(result)):
            if result[k].get('completed') is True:
                completed_tasks.append(result[k].get('title'))

    def format_output(name, completed, total):
        print('Employee {} is done with tasks({}/{}):'
              .format(name, len(completed), total))

        for i in completed:
            print('\t {}'.format(i))

    format_output(name, completed_tasks, total_tasks)
