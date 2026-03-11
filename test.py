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


if __name__ == "__main__":
    # Example usage
    target = "https://example.com"
    print(f"Fetching {target}...\n")

    soup = fetch_and_parse(target)

    # print some elements from the page
    title = soup.title.string if soup.title else "(no title)"
    print(f"Page title: {title}")

    h1 = soup.find("h1")
    if h1:
        print(f"First <h1> text: {h1.get_text(strip=True)}")
    else:
        print("No <h1> tag found.")




