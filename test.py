import requests
import datetime
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

json = {
  "team_leader": 1,
  "job": "Fix critical bug in auth module",
  "work_size": 8,
  "collaborators": "2, 3, 5",
  "start_date": datetime.datetime.now().isoformat(),
  "end_date": datetime.datetime.now().isoformat(),
  "is_finished": False
}
print(requests.post('http://localhost:5000/api/jobs', json=json).reason)