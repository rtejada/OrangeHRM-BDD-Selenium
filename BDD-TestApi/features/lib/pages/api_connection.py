import requests, json
import os
from dotenv import load_dotenv


class ApiConnection:

    load_dotenv(os.getcwd() + "/BDD-TestApi/features/lib/data/.env.orangeHRM")
    test_api_url = os.getenv("BASE_URL")
    token_url = os.getenv("TOKEN_URL")
    client_id = os.getenv("ClientID")
    client_secret = os.getenv("ClientSecret")

    data = {'grant_type': 'client_credentials'}

    def get_token(self):

        access_token_response = requests.post(self.token_url, data=self.data, verify=False, allow_redirects=False,
                                              auth=(self.client_id, self.client_secret))

        # we can now use the access_token as much as we want to access protected resources.
        tokens = json.loads(access_token_response.text)
        access_token = tokens['access_token']
        return access_token

    def get_url_base(self):

        return self.test_api_url
