#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0.

Hint: No authentication is necessary for most features of the Reddit API.
If you're getting errors related to Too Many Requests,
ensure you're setting a custom User-Agent.
"""
import requests


def number_of_subscribers(subreddit):
    '''
    Return number of subreddit subscribers
    '''
    url = f'https://www.reddit.com/r/{subreddit}.json'
    user_agent = 'reddit_user'

    headers = {'User-Agent': user_agent}

    req = requests.get(url, headers=headers, allow_redirects=False)

    if req.status_code != 200:
        return 0

    data = req.json()['data']
    page_list = data['children']
    page_data = page_list[0]['data']

    return page_data['subreddit_subscribers']

if __name__ == '__main__':
    number_of_subscribers()