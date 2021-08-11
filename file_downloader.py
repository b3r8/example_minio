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

    # Search for 'myBucket' bucket.
    found = client.bucket_exists("myBucket")
    if not found:
        print("Bucket 'myBucket' doesn't exists")
        return
    
    # Download object 'uploaded_requs.txt' from bucket
    # 'myBucket' as file 'downloaded_requs.txt'.
    client.fget_object(
        "myBucket", "uploaded_requs.txt", "downloaded_requs.txt",
    )
    print(
        "object 'uploaded_requs.txt' was successfully downloaded as file 'downloaded_requs.txt' from bucket 'myBucket'"
    )

if __name__ == "__main__":
    try:
        main()
    except S3Error as exc:
        print("error occurred", exc)
