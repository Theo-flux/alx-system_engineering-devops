#!/usr/bin/python3
"""
To-do list information for a given employee ID.
export data in the CSV format.
"""
from sys import argv
import csv
import requests

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    user_id = argv[1]
    user = requests.get(base_url + "users/{}".format(user_id)).json()
    user_name = user.get("username")
    todos = requests.get(base_url + "todos", params={"userId": user_id}).json()

    completed = [t.get("title") for t in todos if t.get("completed") is True]
    with open('{}.csv'.format(user_id), 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, user_name, t.get("completed"), t.get("title")]
         ) for t in todos]
