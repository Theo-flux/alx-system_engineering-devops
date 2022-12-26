#!/usr/python3
"""
a recursive function that queries the Reddit API and
returns a list containing the titles of all hot articles
for a given subreddit. If no results are found for the given subreddit,
the function should return None.
"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    if subreddit is None or type(subreddit) is not str:
        return None

    base_url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    headers = {'User-Agent': '0x16-api_advanced_project'}
    params = {"after": after, "count": count, "limit": 100}
    r = requests.get(
        base_url,
        headers=headers,
        params=params,
        allow_redirects=False
        ).json()

    if r.get('data') is None:
        return None

    after = r.get('data').get('after')
    count += r.get('data').get('dist')
    children = r.get('data').get('children')

    for child in children:
        hot_list.append(child.get('title'))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    else:
        return hot_list
