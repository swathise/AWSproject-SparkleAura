import boto3
import json

def main():
    lambda_client = boto3.client("lambda")
    function_name = "sparkleaura-s3-logger"  # from CloudFormation

    # This is just a test payload; your Lambda prints it in CloudWatch Logs
    payload = {
        "source": "boto3-manual-invoke",
        "message": "Hello from SparkleAura!"
    }

    print(f"Invoking Lambda function: {function_name}")
    response = lambda_client.invoke(
        FunctionName=function_name,
        InvocationType="RequestResponse",
        Payload=json.dumps(payload).encode("utf-8")
    )

    resp_payload = response["Payload"].read().decode("utf-8")
    print("Lambda response payload:")
    print(resp_payload)

if __name__ == "__main__":
    main()
