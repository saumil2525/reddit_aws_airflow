from operator import index

import pandas as pd
import praw
import sys
from praw import Reddit
from utils.constants import POST_FIELDS
import numpy as np

def connect_reddit(client_id: str, client_secret: str, user_agent:str) -> Reddit:
    try:
        reddit = praw.Reddit(client_id=client_id,
                             client_secret=client_secret,
                             user_agent=user_agent)
        print("Connected to Reddit")
        return reddit

    except Exception as e:
        print(e)
        sys.exit(1)


def extract_posts(reddit_instance: Reddit, subreddit: str, time_filer: str, limit=None):
    sureddit = reddit_instance.subreddit(subreddit)
    posts = subreddit.top(time_filer=time_filer, limit=limit) # this will return array of the posts

    post_lists = []

    for post in posts:
        post_dict = vars(post)
        post = { key: post[key] for key in POST_FIELDS}
        post_lists.append(post)

    return post_lists

def transform_data(post_df):
    post_df['created_utc'] = pd.to_datetime(post_df['created_utc'], unit='s')
    post_df['over_18'] = np.where(post_df['over_18'] == True, True, False)
    post_df['author'] = post_df['author'].astype(str)
    edited_mode = post_df['edited'].mode()
    post_df = np.where(post_df['edited'].isin([True, False]), post_df['edited'], edited_mode).astype(bool)
    post_df['num_comments'] = post_df['num_comments'].astype(int)
    post_df['score'] = post_df['score'].astype(int)
    post_df['upvote_ratio'] = post_df['upvote_ratio'].astype(int)
    post_df['title'] = post_df['title'].astype(str)

    return post_df


def load_data_to_csv(data: pd.DataFrame, path: str):
    data.to_csv(path, index=False)
    return data


