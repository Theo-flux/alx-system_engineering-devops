#!/usr/bin/env python3
"""
python script that returns todo list progress from
an api
"""

if __name__ == "__main__":
    from sys import argv
    import requests

    id = argv[1]
    baseUrl = 'https://jsonplaceholder.typicode.com'
    urlForTodo = '{}/todos?userId={}'.format(baseUrl, id)
    urlForUser = '{}/users?id={}'.format(baseUrl, id)
    EMPLOYEE_NAME = ""
    NUMBER_OF_DONE_TASKS = []
    TOTAL_NUMBER_OF_TASKS = 0

    with requests.get(urlForUser) as res:
        result = res.json()
        EMPLOYEE_NAME = result[0].get('name')

    with requests.get(urlForTodo) as res:
        result = res.json()
        TOTAL_NUMBER_OF_TASKS = len(result)

        for k in range(0, len(result)):
            if result[k].get('completed') is True:
                NUMBER_OF_DONE_TASKS.append(result[k].get('title'))

    def format_output(name, completed, total):
        print('Employee {} is done with tasks({}/{}):'
              .format(name, len(completed), total))

        for i in completed:
            print('\t{}'.format(i))

    format_output(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS)
