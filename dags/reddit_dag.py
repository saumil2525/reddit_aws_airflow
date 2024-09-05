from airflow import DAG
from datetime import datetime
import os
import sys

from airflow.operators.python import PythonOperator

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pipelines.reddit_pipeline import reddit_pipeline
from pipelines.aws_s3_pipeline import upload_s3_pipeline

default_args = {"owner": "Sam", "start_date": datetime(2024, 1, 1)}

file_postfix = datetime.now().strftime("%Y%m%d")
dag = DAG(
    dag_id="etl_pipeline",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,
    tags=["pipeline", "etl", "reddit"],
)

# extration from reddit
extract = PythonOperator(
    task_id="reddit_extraction",
    python_callable=reddit_pipeline,
    op_args={
        "file_name": f"reddit_{file_postfix}",
        "subreddit": "dataengineering",
        "time_filter": "day",
        "limit": 100,
    },
    dag=dag,
)

# upload to s3

upload_s3 = PythonOperator(
    task_id="s3_upload", python_callable=upload_s3_pipeline, dag=dag
)

# dependencies
extract >> upload_s3