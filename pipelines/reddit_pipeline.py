from utils.constants import  CLIENT_ID, SECRET, OUTPUT_PATH
from etls.reddit_etl import connect_reddit, extract_posts, load_data_to_csv, transform_data
import pandas as pd

def reddit_pipeline(filename: str, subreddit: str, time_filer: str = 'day', limit=None):

    # connecting to reddit instance
    # SECRET = 'U29r4ZSAehPoJMAqxasvhXQrp4RSkA'
    # CLIENT_ID = 'GBPXCbHf-qO6Mon76cgo4w'
    instance = connect_reddit(CLIENT_ID, SECRET, 'Airscholar Agent')
    # extraction
    posts = extract_posts(instance, subreddit, time_filer, limit)
    # transformation
    post_df = pd.DataFrame(posts)
    post_df = transform_data(post_df)
    # loading to csv
    file_path = f'{OUTPUT_PATH}/{filename}.csv'
    load_data_to_csv(post_df, f'{OUTPUT_PATH}/{filename}.csv')

    return file_path

