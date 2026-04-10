import requests
from pprint import pprint

host = "127.0.0.1"
port = "5000"

url = f"http://{host}:{port}/api/jobs"
response = requests.get(url=url)

if response:
    pprint(response.json())
else:
    print(f"Http status: {response}, reason: {response.reason}")
    
url = f"http://{host}:{port}/api/jobs/1"
response = requests.get(url=url)

if response:
    print()
    pprint(response.json())
else:
    print(f"Http status: {response}, reason: {response.reason}")

url = f"http://{host}:{port}/api/jobs/99"
response = requests.get(url=url)

if response:
    print()
    pprint(response.json())
else:
    print(f"Http status: {response}, reason: {response.reason}")

url = f"http://{host}:{port}/api/jobs/test"
response = requests.get(url=url)

if response:
    print()
    pprint(response.json())
else:
    print(f"Http status: {response}, reason: {response.reason}")