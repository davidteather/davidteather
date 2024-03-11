import requests
import datetime
from jinja2 import Environment, FileSystemLoader

WORKER_BASE_URL = "https://dteather-portfolio.dteather.workers.dev"

def to_human_readable(num, round_to=1):
    """
    Converts a large number into a human-readable format
    """
    if num < 1_000:
        return str(num)
    elif num < 1_000_000:
        return f"{round(num / 1_000, round_to)}K"
    elif num < 1_000_000_000:
        return f"{round(num / 1_000_000, round_to)}M"
    else:
        return f"{round(num / 1_000_000_000, round_to)}B"

def main():
    tries = 0
    success = False
    while tries < 3 and not success:
        tries += 1

        try:
            # GitHub Stats
            github_stats = requests.get(WORKER_BASE_URL + "/github").json()
            star_count = to_human_readable(github_stats["starCount"])

            # GitHub Sponsor Stats
            github_sponsor_stats = requests.get(WORKER_BASE_URL + "/github/sponsors").json()
            sponsor_count = to_human_readable(github_sponsor_stats["sponsorCount"])

            # LinkedIn Stats
            linkedin_stats = requests.get(WORKER_BASE_URL + "/linkedin").json()
            connection_count = to_human_readable(linkedin_stats["learnerCount"])

            # YouTube Stats
            youtube_stats = requests.get(WORKER_BASE_URL + "/youtube").json()
            subscriber_count = to_human_readable(int(youtube_stats["subscriberCount"]))
            view_count = to_human_readable(int(youtube_stats["viewCount"]), round_to=None)

            success = True
        except Exception as e:
            continue

    if not success:
        print("Failed to fetch stats")
        return

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