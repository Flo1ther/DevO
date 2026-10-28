
import json
import os
import boto3

s3 = boto3.client("s3")

def lambda_handler(event, context):
    bucket = os.environ["BUCKET_NAME"]

    try:
        response = s3.list_objects_v2(Bucket=bucket)

        files = [
            obj["Key"]
            for obj in response.get("Contents", [])
        ]

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "status": "success",
                "count": len(files),
                "files": files
            })
        }

    except Exception as e:
        print(f"S3 error: {e}")

        return {
            "statusCode": 500,
            "body": json.dumps({
                "status": "error",
                "message": "Internal server error"
            })
        }
