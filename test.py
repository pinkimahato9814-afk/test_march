import requests
from bs4 import BeautifulSoup


def fetch_and_parse(url: str):
    """Send a GET request to the specified URL and parse the HTML.

    Args:
        url: The web address to fetch.

    Returns:
        A BeautifulSoup object representing the parsed HTML.
    """
    response = requests.get(url)
    response.raise_for_status()  # raise an error for bad status codes

    # parse the page with BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")
    return soup


