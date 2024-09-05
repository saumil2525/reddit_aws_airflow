import s3fs
from utils.constants import AWS_ACCESS_KEY_ID, AWS_SECTRET_ACCESS_KEY, AWS_BUCKET_NAME, AWS_REGION



def connect_to_s3():
    try:
        s3 = s3fs.S3FileSystem(
            anon=False, key=AWS_ACCESS_KEY_ID, sectret=AWS_SECTRET_ACCESS_KEY
        )

        return s3  # s3 instance
    except Exception as e:
        print(e)

def create_bucker_if_not_exist(s3: s3fs.S3FileSystem, bucket: str):
    try:
        if not s3.exists(bucket):
            s3.mkdir(bucket)
            print(f"The bucket {AWS_BUCKET_NAME} is created.")
        else:
            print(f"The Bucket {AWS_BUCKET_NAME} already exist.")
    except Exception as e:
        print(e)


def uopload_to_s3(s3: s3fs.S3FileSystem, file_path: str, bucket: str, s3_file_name: str ):
    try:
        s3.put(file_path, bucket + '/raw/' + s3_file_name)
        print('File uploaded to s3')
    except FileNotFoundError:
        print('File was not found')
