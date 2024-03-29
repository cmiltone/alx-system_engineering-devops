#!/usr/bin/python3
"""module to count words in all hot posts of a given Reddit subreddit."""
import requests


def count_words(subreddit, word_list, _dict={}, after="", count=0):
    """function prints counts of given words found
    in hot posts of a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    res = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)
    try:
        json = res.json()
        if res.status_code == 404:
            raise Exception
    except Exception:
        print("")
        return

    json = json.get("data")
    after = json.get("after")
    count += json.get("dist")
    for c in json.get("children"):
        title = c.get("data").get("title").lower().split()
        for word in word_list:
            if word.lower() in title:
                times = len([t for t in title if t == word.lower()])
                if _dict.get(word) is None:
                    _dict[word] = times
                else:
                    _dict[word] += times

    if after is None:
        if len(_dict) == 0:
            print("")
            return
        _dict = sorted(_dict.items(), key=lambda kv: (-kv[1], kv[0]))
        [print("{}: {}".format(k, v)) for k, v in _dict]
    else:
        count_words(subreddit, word_list, _dict, after, count)
