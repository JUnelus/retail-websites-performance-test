import requests
import time

def performance_test(url):
  """
  Performs a basic performance test on a given URL.

  Args:
      url (str): The URL of the website to test.

  Returns:
      float: The time taken to load the website in seconds.
  """
  start_time = time.monotonic()
  response = requests.get(url)
  end_time = time.monotonic()

  response.raise_for_status()  # Raise an exception for bad status codes

  load_time = end_time - start_time
  return load_time

if __name__ == "__main__":
  websites = [
      "https://www.walmart.com",
      "https://www.target.com",
      # Add more websites here
  ]

  for url in websites:
      try:
          load_time = performance_test(url)
          print(f"{url} loaded in {load_time:.2f} seconds")
      except requests.exceptions.RequestException as e:
          print(f"Error loading {url}: {e}")