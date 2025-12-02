import boto3
import uuid
import os

def main():
    session = boto3.session.Session()
    region = session.region_name or "us-east-1"
    s3 = session.client("s3")

    # Create a unique bucket name
    bucket_name = f"sparkleaura-boto3-{uuid.uuid4().hex[:8]}"
    print(f"Creating bucket: {bucket_name} in {region}")

    create_params = {"Bucket": bucket_name}
    if region != "us-east-1":
        create_params["CreateBucketConfiguration"] = {
            "LocationConstraint": region
        }

    s3.create_bucket(**create_params)
    print("Bucket created.")

    # Create a local test file
    filename = "sample_upload.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write("Hello from SparkleAura Boto3 script!\n")

    print(f"Uploading {filename} to {bucket_name}...")
    s3.upload_file(filename, bucket_name, filename)
    print("Upload complete.")

    # Optional: clean up local file
    os.remove(filename)
    print("Local test file removed.")
    print(f"Bucket {bucket_name} now contains {filename}.")

if __name__ == "__main__":
    main()
