import configparser
import os
from ast import parse

parser = configparser.ConfigParser()

# parser.read(os.path.join(os.path.dirname(os.path.dirname(__file__))), '../config/config.conf')

parser.read(
    "/Users/samdesai/PythonProjects/DataEngineering-af/pythonProject/config/config.conf"
)

# SECRET = parser.get('api_keys', 'reddit_secret_key')
# CLIENT_ID = parser.get('api_keys', 'reddit_client_id')
SECRET = "U29r4ZSAehPoJMAqxasvhXQrp4RSkA"
CLIENT_ID = "GBPXCbHf-qO6Mon76cgo4w"
#
# DATABASE_HOST = parser.get('database', 'database_host')
# DATABASE_NAME = parser.get('database', 'database_name')
# DATABASE_PORT = parser.get('database', 'database_port')
# DATABASE_USERNAME = parser.get('database', 'database_username')
# DATABASE_PASSWORD = parser.get('database', 'database_password')

# INPUT_PATH = parser.get('file_paths', 'input_path')
# OUTPUT_PATH = parser.get('file_paths', 'output_path')
OUTPUT_PATH = "/opt/airflow/data/output"

AWS_ACCESS_KEY_ID = parser.get("aws", "aws_access_key_id")
AWS_SECTRET_ACCESS_KEY = parser.get("aws", "aws_secret_access_key")
AWS_SESSION_TOKEN = parser.get("aws", "aws_session_token")
AWS_REGION = parser.get("aws", "aws_region")
AWS_BUCKET_NAME = parser.get("aws", "aws_bucket_name")


POST_FIELDS = {
    "id",
    "title",
    "selftext",
    "score",
    "num_comments",
    "author",
    "created_utc",
    "url",
    "upvote_ratio",
    "over_18",
    "edited",
    "spoiler",
    "stockied",
}
print(
    f"path of constant file: --> {os.path.join(os.path.dirname(os.path.dirname(__file__))), '../config/config.conf'}"
)
print(f"SECRET: --> {SECRET}")
