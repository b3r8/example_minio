from minio import Minio
from minio.error import S3Error

def main():
    # Create a client with the MinIO server playground, its access key
    # and secret key.
    client = Minio(
        "play.min.io",
        access_key="Q3AM3UQ867SPQQA43P2F",
        secret_key="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG",
    )

    # Search for 'my-bucket' bucket.
    found = client.bucket_exists("my-bucket")
    if not found:
        print("Bucket 'my-bucket' doesn't exists")
        return
    
    # Download object 'uploaded_requs.txt' from bucket
    # 'my-bucket' as file 'downloaded_requs.txt'.
    client.fget_object(
        "my-bucket", "uploaded_requs.txt", "downloaded_requs.txt",
    )
    print(
        "object 'uploaded_requs.txt' was successfully downloaded as file 'downloaded_requs.txt' from bucket 'my-bucket'"
    )

if __name__ == "__main__":
    try:
        main()
    except S3Error as exc:
        print("error occurred", exc)
