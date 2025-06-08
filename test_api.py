import requests

response = requests.post(
    "http://127.0.0.1:5000/generate-persona",
    json={"text": "I’m a busy working mom looking for healthier frozen meals that my kids will actually eat."}
)

print(response.json())

