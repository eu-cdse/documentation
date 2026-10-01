# Change the access key, secret_key and bucket_name
from pprint import pprint
import boto3
import json

access_key = <your-access-key>  # OpenStack access key
secret_key = <your-secret-key>  # OpenStack secret key
bucket_name = <your-bucket-name>  # bucket name
host = "https://s3.waw3-1.cloudferro.com/"

s3 = boto3.client(
    "s3",
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    endpoint_url=host,
)

# share a bucket
share_to = "ddf4c98b5e6647f0a246f0624c8341d9" # SH principal

bucket_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Sentinel Hub permissions",
            "Effect": "Allow",
            "Principal": {"AWS": f"arn:aws:iam::{share_to}:root"},
            "Action": [
                "s3:*",
            ],
            "Resource": [
                f"arn:aws:s3:::{bucket_name}",
                f"arn:aws:s3:::{bucket_name}/*",
            ],
        }
    ],
}

# Convert the policy from JSON dict to string
bucket_policy = json.dumps(bucket_policy)

# Set the new policy
s3.put_bucket_policy(
    Bucket=bucket_name,
    Policy=bucket_policy,
)

result = s3.get_bucket_policy(Bucket=bucket_name)
pprint(result["Policy"])
