#!/usr/bin/python3
"""module to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """returns the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 404:
        return 0
    json = res.json().get("data")
    return json.get("subscribers")
