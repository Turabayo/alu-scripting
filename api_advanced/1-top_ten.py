#!/usr/bin/python3
""" prints the titles of the first 10 hot posts listed"""


import json
import requests
import sys


def top_ten(subreddit):
    """Top ten hot post"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "Linux:MyRedditApp:1.0 (by /u/Few-Area5580)"
    }

    response = requests.get(url, headers=headers, timeout=10)
    if response.status_code == 200:
        data = response.json()["data"]["children"]
        for i in range(10):
            return data[i]["data"]["title"]
    else:
        return "None"