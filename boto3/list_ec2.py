import boto3

def main():
    ec2 = boto3.client("ec2")

    response = ec2.describe_instances(
        Filters=[
            {"Name": "instance-state-name", "Values": ["running"]}
        ]
    )

    print("Running EC2 instances:")
    for reservation in response.get("Reservations", []):
        for instance in reservation.get("Instances", []):
            instance_id = instance["InstanceId"]
            instance_type = instance.get("InstanceType")
            state = instance["State"]["Name"]
            az = instance["Placement"]["AvailabilityZone"]
            name = None
            for tag in instance.get("Tags", []):
                if tag["Key"] == "Name":
                    name = tag["Value"]
                    break

            print(f"- {instance_id} | {instance_type} | {state} | {az} | Name={name}")

if __name__ == "__main__":
    main()
