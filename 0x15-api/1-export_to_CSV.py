#!/usr/bin/python3
"""module 1-export_to_CSV"""
# Using what you did in the task #0,
# extend your Python script to export data in the  format.

#   Records all tasks that are owned by this employee
#   Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
#   File name must be: USER_ID.csv
import csv
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

    for item in todos:
        if item.get('userId') == employee_id:
            tasks.append([
                employee_id,
                employee_name,
                item.get('completed'),
                item.get('title')
            ])

    # Write to CSV
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerows(tasks)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
    else:
        fetch_todo_list(sys.argv[1])
