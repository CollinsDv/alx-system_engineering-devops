"""
Get all dashboard lists returns "OK" response
"""
import requests
import os

API_KEY = os.getenv('DD_API_KEY')
APPLICATION_KEY = os.getenv('DD_APP_KEY')

url = "https://api.datadoghq.com/api/v1/dashboard"

headers = {
    "DD-API-KEY": API_KEY,
    "DD-APPLICATION-KEY": APPLICATION_KEY,
}

response = requests.get(url, headers=headers)
dashboards = response.json()

# Print all dashboards and their IDs
for dashboard in dashboards['dashboards']:
    print(f"Name: {dashboard['title']}, ID: {dashboard['id']}")

# Find and print your specific dashboard ID
# dashboard_name = "Your Dashboard Name"
# for dashboard in dashboards['dashboards']:
#     if dashboard['title'] == dashboard_name:
#         print(f"Dashboard ID: {dashboard['id']}")
