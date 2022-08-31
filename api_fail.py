import requests

post_data = {
    'username': 'm',
    'password': ':)'
}

payload = {"settings": {
    "name": "network scan",
    "text_targets": "127.0.0.1"
}}

response = requests.post(f'https://nessus.osuv.de/session', data=post_data)
if response.status_code == 200:
    token = response.json().get('token')
    header = {
        "X-Cookie":f"token={token}",
        "Content-Type":"application/json"
    }

    response = requests.put(url = f'https://nessus.osuv.de/scans/5', json=payload, headers=header)
    print(response.status_code)
    print(response.text)
