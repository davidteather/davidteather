import requests
import datetime

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

            # LinkedIn Stats
            linkedin_stats = requests.get(WORKER_BASE_URL + "/linkedin").json()
            connection_count = to_human_readable(linkedin_stats["learnerCount"])

            # YouTube Stats
            youtube_stats = requests.get(WORKER_BASE_URL + "/youtube").json()
            subscriber_count = to_human_readable(int(youtube_stats["subscriberCount"]))
            view_count = to_human_readable(int(youtube_stats["viewCount"]), round_to=0)

            success = True
        except Exception as e:
            continue

    # Last updated, human readable
    last_updated_str = datetime.datetime.now().strftime("%B %d, %Y")

    # Read in the template, and replace the placeholders with the actual stats
    with open("README.template.md", "r") as file:
        readme = file.read()
        readme = readme.replace("{{ GITHUB_STARS }}", star_count)
        readme = readme.replace("{{ LINKEDIN_LEARNERS }}", connection_count)
        readme = readme.replace("{{ YOUTUBE_SUBSCRIBERS }}", subscriber_count)
        readme = readme.replace("{{ YOUTUBE_VIEWS }}", view_count)
        readme = readme.replace("{{ LAST_UPDATED }}", last_updated_str)

    # Write the final README
    with open("README.md", "w") as file:
        file.write(readme)

if __name__ == "__main__":
    main()