#!/usr/bin/python3
"""Displays fake user data using the JSON Placeholder API."""
import requests
from sys import argv

def get_employee_data(employee_id, api_base):
    user_response = requests.get(f"{api_base}users/{employee_id}")
    tasks_response = requests.get(f"{api_base}todos?userId={employee_id}")
    return user_response.json(), tasks_response.json()

def print_completed_tasks(employee_name, tasks):
    completed_tasks = [task for task in tasks if task.get("completed")]
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(completed_tasks), len(tasks)
    ))
    for task in completed_tasks:
        print("\t " + task.get("title"))

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: ./script_name.py <employee_id>")
        exit(1)

    employee_id = argv[1]
    api = 'https://jsonplaceholder.typicode.com/'

    employee, tasks = get_employee_data(employee_id, api)
    employee_name = employee.get("name")

    print_completed_tasks(employee_name, tasks)
