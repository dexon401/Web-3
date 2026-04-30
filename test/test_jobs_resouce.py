import requests

print(requests.get("http://127.0.0.1:5000/api/v2/jobs").json())
print(requests.get("http://127.0.0.1:5000/api/v2/jobs/1").json())
print(requests.get("http://127.0.0.1:5000/api/v2/jobs/999").json())

test_data_json = {
  "team_leader": 1,
  "job": "Engineering of an additional module",
  "work_size": 20,
  "collaborators": '2,3'
}

response_json = requests.post(
    "http://127.0.0.1:5000/api/v2/jobs", json=test_data_json
).json()
print(response_json)
print(requests.post("http://127.0.0.1:5000/api/v2/jobs", json={}).json())

print(
    requests.delete(f"http://127.0.0.1:5000/api/v2/jobs/{response_json['id']}").json()
)
print(requests.delete("http://127.0.0.1:5000/api/v2/jobs/999").json())
