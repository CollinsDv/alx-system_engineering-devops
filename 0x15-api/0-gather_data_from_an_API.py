#!/usr/bin/python3
"""module 0-gather_data_from_an_api"""
# uses 'https://jsonplaceholder.typicode.com/' to search
# for a given employee ID, returns their TODO information
#   You must use urllib or requests module
#   The script must accept an integer as a parameter, which is the employee ID
#   The script must display on the standard output the employee
#       TODO list progress in this exact format:
#   First line: Employee EMPLOYEE_NAME is done with
#       tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
#   EMPLOYEE_NAME: name of the employee
#   NUMBER_OF_DONE_TASKS: number of completed tasks
#   TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum
#   of completed and non-completed tasks
# Second and N next lines display the title of completed tasks:
# TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)
import requests
import sys


def fetch_todo_list(employee_id):
    """fetch url that uses REST API"""
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
    employee_name = user.get('name')

    # Fetch todo list information
    todo_response = requests.get(todos_url)
    todos = todo_response.json()

    tasks_completed = 0
    total_tasks = 0
    tasks_completed_list = []

    for item in todos:
        if item.get('userId') == employee_id:
            if item.get('completed'):
                tasks_completed += 1
                tasks_completed_list.append(item.get('title'))
            total_tasks += 1

    print(f"Employee {employee_name} is done with "
          f"tasks({tasks_completed}/{total_tasks}):")

    for task in tasks_completed_list:
        print(f'\t {task}')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
    else:
        fetch_todo_list(sys.argv[1])
