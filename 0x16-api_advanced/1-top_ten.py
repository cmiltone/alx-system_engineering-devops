#!/usr/bin/python3
"""module to query hot posts"""
import requests


def top_ten(subreddit):
    """prints titles of first 10 hot posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 10
    }
    res = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if res.status_code == 404:
        print("None")
        return
    json = res.json().get("data")
    [print(c.get("data").get("title")) for c in json.get("children")]
