import requests, json
import os
from dotenv import load_dotenv

load_dotenv(os.getcwd() + "/.env.orangeHRM")

test_api_url = os.getenv("BASE_URL")
token_url = os.getenv("TOKEN_URL")
client_id = os.getenv("ClientID")
client_secret = os.getenv("ClientSecret")

# step I, J - turn the authorization code into a access token, etc
data = {'grant_type': 'client_credentials'}
print("requesting access token")
access_token_response = requests.post(token_url, data=data, verify=False, allow_redirects=False, auth=(client_id, client_secret))

print("response")
print(access_token_response.headers)
print('body: ' + access_token_response.text)

# we can now use the access_token as much as we want to access protected resources.
tokens = json.loads(access_token_response.text)
access_token = tokens['access_token']
print ("access token: " + access_token)

api_call_headers = {'Authorization': 'Bearer ' + access_token}
api_call_response = requests.get(test_api_url+'organization', headers=api_call_headers, verify=False)

print(api_call_response.text)