import requests
import base64

client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_CLIENT_SECRET'
auth = requests.auth.HTTPBasicAuth(client_id, client_secret)

headers = {'User-Agent': 'your_app_name/0.1 by your_reddit_username'}

data = {
    'grant_type': 'password',
    'username': 'REDDIT_USERNAME',
    'password': 'REDDIT_PASSWORD'
}

response = requests.post(
    'https://www.reddit.com/api/v1/access_token',
    auth=auth, data=data, headers=headers
)

token = response.json().get('access_token')

print(f'Access Token: {token}')
