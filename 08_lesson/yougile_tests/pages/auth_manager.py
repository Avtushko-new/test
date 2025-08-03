import os
import requests
import logging
import pytest

logger = logging.getLogger(__name__)


class AuthManager:
    def __init__(self):
        self.api_key = None
        self.cache_file = ".yougile_api_key"

    def get_api_key(self, base_url, login, password, company_id):
        if self.api_key:
            return self.api_key

        if os.path.exists(self.cache_file):
            with open(self.cache_file, "r") as f:
                cached_key = f.read().strip()
                if cached_key and self.validate_key(base_url, cached_key):
                    self.api_key = cached_key
                    logger.info(f"Using cached API key: {cached_key[:10]}...")
                    return cached_key

        url = f"{base_url}/auth/keys"
        data = {
            "login": login,
            "password": password,
            "companyId": company_id
        }
        logger.info(f"Requesting new API key from: {url}")
        response = requests.post(url, json=data)

        if response.status_code not in [200, 201]:
            if (response.status_code == 403 and
                    "limit exceeded" in response.text.lower()):
                msg = ("API keys limit exceeded (max 30).\n"
                       "Solution:\n"
                       "1. Go to Yougile -> Account Settings\n"
                       "2. Navigate to 'API Keys'\n"
                       "3. Delete unused keys, especially the oldest ones")
                pytest.fail(msg)
            else:
                error_msg = (f"Failed to get API key: {response.status_code}\n"
                             f"Response: {response.text}")
                pytest.fail(error_msg)

        self.api_key = response.json().get('key')
        if not self.api_key:
            pytest.fail("API key not found in response")

        with open(self.cache_file, "w") as f:
            f.write(self.api_key)

        logger.info(f"API key obtained: {self.api_key[:10]}...")
        return self.api_key

    def validate_key(self, base_url, api_key):
        test_url = f"{base_url}/users/me"
        headers = {"Authorization": f"Bearer {api_key}"}
        try:
            response = requests.get(test_url, headers=headers, timeout=5)
            return response.status_code == 200
        except Exception as e:
            logger.warning(f"Key validation error: {str(e)}")
            return False
