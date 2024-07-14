#!/usr/bin/python3
"""Creates a CSV from fake user data using the JSON Placeholder API."""
import csv
import requests
from sys import argv


def fetch_data(url):
    response = requests.get(url)
    return response.json()


def main():
    if len(argv) != 2:
        print("Usage: ./script_name.py <employee_id>")
        exit(1)

    employee_id = argv[1]
    api = 'https://jsonplaceholder.typicode.com/'

    user_url = f"{api}users/{employee_id}"
    todos_url = f"{api}todos?userId={employee_id}"

    employee = fetch_data(user_url)
    tasks = fetch_data(todos_url)

    username = employee.get("username")

    csv_headers = [
        "USER_ID",
        "USERNAME",
        "TASK_COMPLETED_STATUS",
        "TASK_TITLE"
    ]

    data_dicts = [
        {
            "USER_ID": employee_id,
            "USERNAME": username,
            "TASK_COMPLETED_STATUS": task.get("completed"),
            "TASK_TITLE": task.get("title")
        } for task in tasks
    ]

    filename = f"{employee_id}.csv"
    with open(filename, "w", newline='') as file:
        writer = csv.DictWriter(file, 
        fieldnames=csv_headers, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        writer.writerows(data_dicts)


if __name__ == "__main__":
    main()
