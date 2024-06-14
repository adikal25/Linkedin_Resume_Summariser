import os
import requests
from dotenv import load_dotenv


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """Scrape info from LinkedIn profile"""

    if mock:
        # Use mock data from a predefined URL for testing purposes
        linkedin_profile_url = "https://gist.githubusercontent.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/raw/fad4d7a87e3e934ad52ba2a968bad9eb45128665/eden-marco.json"
        response = requests.get(linkedin_profile_url, timeout=10)
    else:
        # Load the API key from environment variables
        load_dotenv()
        api_key = os.environ.get('PROXYCURL_API_KEY')
        if not api_key:
            raise ValueError(
                "PROXYCURL_API_KEY is not set in environment variables")

        api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
        headers = {
            "Authorization": f"Bearer {api_key}"
        }
        response = requests.get(api_endpoint, params={
                                "url": linkedin_profile_url}, headers=headers, timeout=10)

    if response.headers.get("Content-Type") == "application/json":
        try:
            return response.json()
        except ValueError as e:
            raise ValueError("Failed to parse JSON response") from e
    else:
        raise ValueError(
            f"Expected JSON response but got {response.headers.get('Content-Type')}")


if __name__ == "__main__":
    # Example usage
    profile_data = scrape_linkedin_profile(
        linkedin_profile_url='https://www.linkedin.com/in/adikal25', mock=True)
    print(profile_data)
