import requests
import boto3
from botocore.exceptions import NoCredentialsError

def download_and_upload_to_s3(url, bucket, s3_key):
    """
    Downloads a file from a URL and uploads it directly to S3.
    
    :param url: URL of the file to download
    :param bucket: Name of the S3 bucket
    :param s3_key: S3 object key (path in bucket)
    """
    try:
        print(f"Downloading: {url}")
        response = requests.get(url, stream=True)
        response.raise_for_status()

        s3 = boto3.client("s3")
        print(f"Uploading to s3://{bucket}/{s3_key}")
        s3.upload_fileobj(response.raw, bucket, s3_key)

        print("Upload complete.")

    except requests.exceptions.RequestException as e:
        print("Download failed:", e)
    except NoCredentialsError:
        print("AWS credentials not found.")
    except Exception as e:
        print("Something went wrong:", e)

if __name__ == "__main__":
    url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet"
    bucket = "strath-nyc-taxi"
    s3_key = "raw/2023/01/yellow_tripdata_2023-01.parquet"

    download_and_upload_to_s3(url, bucket, s3_key)
