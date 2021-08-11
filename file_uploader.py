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
    found = client.bucket_exists(myBucket)
    if not found:
        client.make_bucket("myBucket")
    else:
        print("Bucket 'myBucket' already exists")
    
    # Upload file 'requirements.txt' to bucket
    # 'myBucket' as object 'uploaded_requs.txt'.
    client.fput_object(
        "myBucket", "uploaded_requs.txt", "requirements.txt",
    )
    print(
        "file 'requirements.txt' was successfully uploaded as object 'uploaded_requs.txt' to bucket 'myBucket'"

    )

if __name__ == "__main__":
    try:
        main()
    except S3Error as exc:
        print("error occurred", exc)
