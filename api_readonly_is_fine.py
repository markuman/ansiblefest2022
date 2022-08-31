import requests

post_data = {
    'username': 'm',
    'password': ':)'
}

response = requests.post(f'https://nessus.osuv.de/session', data=post_data)
if response.status_code == 200:
    token = response.json().get('token')
    header = {
        "X-Cookie":f"token={token}",
        "Content-Type":"application/json"
    }
    
    # read is fine
    response = requests.get(f'https://nessus.osuv.de/scans', headers=header)
    print(response.status_code)
    print(response.text)

