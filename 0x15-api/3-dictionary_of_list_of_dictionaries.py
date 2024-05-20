#!/usr/bin/python3
"""module: 3-dictionary_of_list_of_dictionaries"""
# Using what you did in the task #0,
# extend your Python script to export data in the JSON format.

# Requirements:

#   Records all tasks from all employees
#   Format must be: { "USER_ID": [ {"username":
#                       "USERNAME", "task": "TASK_TITLE",
#                       "completed": TASK_COMPLETED_STATUS},
#                           {"username": "USERNAME", "task": "TASK_TITLE",
#                           "completed": TASK_COMPLETED_STATUS}, ... ],
#                     "USER_ID": [ {"username":
#                           "USERNAME", "task": "TASK_TITLE",
#                           "completed": TASK_COMPLETED_STATUS},
#                           {"username": "USERNAME", "task": "TASK_TITLE",
#                           "completed": TASK_COMPLETED_STATUS}, ... ]}
#   File name must be: todo_all_employees.json
import json
import requests


def fetch_all_todo_list():
    """Fetches data from a URL and exports
    all tasks of all employees to a JSON file."""
    todos_url = 'https://jsonplaceholder.typicode.com/todos'
    users_url = 'https://jsonplaceholder.typicode.com/users'

    # Fetch user information
    user_response = requests.get(users_url)
    if user_response.status_code != 200:
        print("User data not found.")
        return

    users = user_response.json()

    all_tasks = {}

    # Fetch todo list information for each user
    for user in users:
        user_id = user.get('id')
        employee_name = user.get('username')

        todo_response = requests.get(f'{todos_url}?userId={user_id}')
        todos = todo_response.json()

        tasks = []
        for item in todos:
            tasks.append({
                'username': employee_name,
                'task': item.get('title'),
                'completed': item.get('completed')
            })

        all_tasks[str(user_id)] = tasks

    filename = 'todo_all_employees.json'

    with open(filename, mode='w') as file:
        json.dump(all_tasks, file)


if __name__ == "__main__":
    fetch_all_todo_list()
