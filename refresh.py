import requests
import datetime
import json
from jinja2 import Environment, FileSystemLoader

WORKER_BASE_URL = "https://dteather-portfolio.dteather.workers.dev"
CACHED_STATS_FILE = "cached_stats.json"

def to_human_readable(num, round_to=1):
    """
    Converts a large number into a human-readable format
    """
    num = int(num)
    if num < 1_000:
        return str(num)
    elif num < 1_000_000:
        return f"{round(num / 1_000, round_to)}K"
    elif num < 1_000_000_000:
        return f"{round(num / 1_000_000, round_to)}M"
    else:
        return f"{round(num / 1_000_000_000, round_to)}B"

def save_to_cache(k, v):
    try:
        with open(CACHED_STATS_FILE, "r") as file:
            cache = json.load(file)
    except FileNotFoundError:
        cache = {}

    cache[k] = v

    with open(CACHED_STATS_FILE, "w") as file:
        json.dump(cache, file, indent=4)

def load_from_cache(k):
    try:
        with open(CACHED_STATS_FILE, "r") as file:
            cache = json.load(file)
            return cache.get(k)
    except FileNotFoundError:
        return None
    
def wrap_function_with_cache_and_retry(func):
    def wrapper(*args, **kwargs):
        # If not in cache, call the function
        success = False
        tries = 0
        while not success and tries < 3:
            try:
                value = func(*args, **kwargs)
                success = True
            except Exception as e:
                tries += 1
                continue

        cache_key = func.__name__
        if not success:
            # Try to load from cache
            cached_value = load_from_cache(cache_key)
            if cached_value:
                return cached_value

        # Save to cache
        save_to_cache(cache_key, value)

        return value
    return wrapper

@wrap_function_with_cache_and_retry
def get_github_stats():
    return requests.get(WORKER_BASE_URL + "/github").json()

@wrap_function_with_cache_and_retry
def get_github_sponsor_stats():
    return requests.get(WORKER_BASE_URL + "/github/sponsors").json()

@wrap_function_with_cache_and_retry
def get_linkedin_stats():
    return requests.get(WORKER_BASE_URL + "/linkedin").json()

@wrap_function_with_cache_and_retry
def get_youtube_stats():
    return requests.get(WORKER_BASE_URL + "/youtube").json()


def main():
    github_stats = get_github_stats()
    star_count = to_human_readable(github_stats["starCount"])

    sponsor_stats = get_github_sponsor_stats()
    sponsor_count = to_human_readable(sponsor_stats["sponsorCount"])

    linkedin_stats = get_linkedin_stats()
    connection_count = to_human_readable(linkedin_stats["learnerCount"])

    youtube_stats = get_youtube_stats()
    subscriber_count = to_human_readable(youtube_stats["subscriberCount"])
    view_count = to_human_readable(youtube_stats["viewCount"], round_to=None)

    # Last updated, human readable
    last_updated_str = datetime.datetime.now().strftime("%B %d, %Y")

    # Load the Jinja2 template
    env = Environment(loader=FileSystemLoader('.'), autoescape=True)
    template = env.get_template('README.template.md')

    # Read in the template, and replace the placeholders with the actual stats
    readme = template.render(
        GITHUB_STARS=star_count,
        GITHUB_SPONSORS=sponsor_count,
        LINKEDIN_LEARNERS=connection_count,
        YOUTUBE_SUBSCRIBERS=subscriber_count,
        YOUTUBE_VIEWS=view_count,
        LAST_UPDATED=last_updated_str,
    )

    # Write the final README
    with open("README.md", "w") as file:
        file.write(readme)

if __name__ == "__main__":
    main()