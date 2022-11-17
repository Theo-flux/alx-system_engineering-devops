#!/usr/bin/python3
"""
To-do list information for a given employee ID.
export data in the json format.
"""
from sys import argv
import json
import requests

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    user_id = argv[1]
    user = requests.get(base_url + "users/{}".format(user_id)).json()
    user_name = user.get("username")
    todos = requests.get(base_url + "todos", params={"userId": user_id}).json()

    completed = [t.get("title") for t in todos if t.get("completed") is True]
    with open('{}.json'.format(user_id), 'w', newline='') as jsonfile:
        json.dump({user_id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": user_name
            } for t in todos]}, jsonfile)
