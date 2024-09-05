from etls.aws_etl import connect_to_s3


def upload_s3_pipeline(task_id):
    file_path = task_id.xcom_pull(task_ids="reddit_extraction", keys="return_value")
    s3 = connect_to_s3()
    create_bucker_if_not_exist(s3, AWS_BUCKET_NAME)
    uopload_to_s3(s3, file_path, AWS_BUCKET_NAME, file_path.split("/")[-1])
