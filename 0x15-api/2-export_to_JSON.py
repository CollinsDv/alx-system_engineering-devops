#!/usr/bin/python3
"""module 2-export_to_JSON"""
# Using what you did in the task #0,
# extend your Python script to export data in the JSON format.

#   Records all tasks that are owned by this employee
#   Format must be: { "USER_ID": [
#       {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
#           "username": "USERNAME"},
#       {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
#           "username": "USERNAME"}, ... ]}
#   File name must be: USER_ID.json
import json
import requests
import sys


def fetch_todo_list(employee_id):
    """fetches data from a URL and converts to CSV into a file"""
    todos_url = 'https://jsonplaceholder.typicode.com/todos'
    users_url = 'https://jsonplaceholder.typicode.com/users'

    try:
        employee_id = int(employee_id)
    except ValueError:
        print("Please provide a valid employee ID as an integer.")
        return

    # Fetch user information
    user_response = requests.get(f'{users_url}/{employee_id}')
    if user_response.status_code != 200:
        print("User not found.")
        return

    user = user_response.json()
    employee_name = user.get('username')

    # Fetch todo list information
    todo_response = requests.get(todos_url)
    todos = todo_response.json()

    tasks = []
    user_id = todos[0].get('userId')

    for item in todos:
        if item.get('userId') == employee_id:
            tasks.append({
                'username': employee_name,
                'task': item.get('title'),
                'completed': item.get('completed')
            })

    new_json = {str(employee_id): tasks}

    filename = f'{employee_id}.json'

    with open(filename, mode='w') as file:
        json.dump(new_json, file)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
    else:
        fetch_todo_list(sys.argv[1])
