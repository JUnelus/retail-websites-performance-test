import requests
import time
import yaml
from random import uniform


def performance_test(url):
    """
    Performs a basic performance test on a given URL.

    Args:
        url (str): The URL of the website to test.

    Returns:
        float: The time taken to load the website in seconds.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    start_time = time.monotonic()
    response = requests.get(url, headers=headers)
    end_time = time.monotonic()

    response.raise_for_status()  # Raise an exception for bad status codes

    load_time = end_time - start_time
    return load_time


def load_urls_from_yaml(file_path):
    """
    Loads a list of URLs from a YAML file.

    Args:
        file_path (str): Path to the YAML file containing the URLs.

    Returns:
        list: List of URLs from the YAML file.
    """
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
        return data.get('Websites', [])


if __name__ == "__main__":
    # Load URLs from the YAML file
    urls_file = "urls.yaml"  # Path to your YAML file
    websites = load_urls_from_yaml(urls_file)

    # Perform performance test on each URL
    for url in websites:
        try:
            # Ensure the URL starts with http or https
            if not url.startswith("http"):
                url = f"https://{url}"

            load_time = performance_test(url)
            print(f"{url} loaded in {load_time:.2f} seconds")

            # Add a delay between requests to avoid getting blocked
            time.sleep(uniform(2, 5))  # Random delay between 2 and 5 seconds

        except requests.exceptions.RequestException as e:
            print(f"Error loading {url}: {e}")
