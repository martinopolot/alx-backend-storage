import requests
import time

# Dictionary to store cached results
cache = {}

# Decorator for caching with an expiration time of 10 seconds
def cache_decorator(func):
    def wrapper(url):
        if url in cache and time.time() - cache[url]['timestamp'] < 10:
            print(f"Cache hit for {url}")
            cache[url]['count'] += 1
            return cache[url]['content']
        
        print(f"Cache miss for {url}, fetching data...")
        content = func(url)
        cache[url] = {
            'content': content,
            'timestamp': time.time(),
            'count': 1
        }
        return content
    return wrapper

@cache_decorator
def get_page(url: str) -> str:
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return f"Error: Failed to fetch {url}"

if __name__ == "__main__":
    url_to_fetch = "http://slowwly.robertomurray.co.uk/delay/1000/url/https://www.example.com"
    
    # Access the same URL multiple times to test caching and count tracking
    for _ in range(5):
        html_content = get_page(url_to_fetch)
        print(f"HTML content of {url_to_fetch}:")
        print(html_content)

    print("Access count for each URL:")
    for url, data in cache.items():
        print(f"{url}: {data['count']} access(es)")

