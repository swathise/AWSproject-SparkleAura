🌟 SparkleAura – Scalable AWS Cloud Architecture



A cloud-based e-commerce architecture for a jewelry brand



This project builds a fully scalable, fault-tolerant AWS architecture for the fictional jewelry brand SparkleAura. It demonstrates professional-level cloud engineering skills using Terraform, CloudFormation, EC2, ALB, RDS, S3, Lambda, Auto Scaling, Boto3, and GitHub version control.



The implementation meets all requirements for the course project:

✔ Infrastructure as Code (Terraform + CloudFormation)

✔ Scalable 2-tier architecture

✔ Auto Scaling + Load Balancing

✔ S3 upload event logging using Lambda

✔ Boto3 scripts for AWS automation

✔ EC2 metadata retrieval

✔ Full documentation + screenshots



📁 Folder Structure

sparkleaura-aws-project/

│

├── terraform/

│   ├── main.tf

│   ├── variables.tf

│   ├── outputs.tf

│   └── provider.tf

│

├── cloudformation/

│   └── sparkleaura-stack.yaml

│

├── boto3/

│   ├── create\_bucket\_upload.py

│   ├── list\_ec2.py

│   ├── lambda\_invoke.py

│   ├── metadata.py   (runs on EC2)

│   └── README\_boto3.txt

│

└── README.md



1. Architecture Overview

The architecture includes:



VPC



2 Public subnets



2 Private subnets



Internet Gateway



Route tables



Compute Layer



Auto Scaling Group



Launch Template



EC2 instances hosting a simple website



Application Load Balancer (ALB)



Database Layer



Amazon RDS (MySQL)



Storage Layer



S3 bucket for images, backups, and logs



Serverless Logging



Lambda triggered on S3 upload



Logs events to CloudWatch



IaC



Terraform → networking



CloudFormation → compute + RDS + Lambda



Automation with Boto3



Create S3 bucket and upload file



List EC2 instances



Invoke Lambda function



Retrieve EC2 metadata



 2. Terraform – Networking Deployment

Files:



main.tf



variables.tf



outputs.tf



provider.tf



Resources created:



✔ VPC

✔ Public + Private Subnets

✔ Security Groups

✔ Route Tables

✔ Outputs exported for CloudFormation



Commands to deploy:

cd terraform

terraform init

terraform apply





Outputs include:



vpc\_id = "vpc-xxxx"

public\_subnet\_id = "subnet-xxx"

public\_subnet2\_id = "subnet-xxx"

private\_subnet\_id = "subnet-xxx"

private\_subnet2\_id = "subnet-xxx"



 3. CloudFormation – Compute, RDS, and Lambda

File:



sparkleaura-stack.yaml



Resources deployed:



✔ Application Load Balancer

✔ Target Group

✔ Launch Template

✔ Auto Scaling Group

✔ EC2 Instances

✔ RDS MySQL instance

✔ S3→Lambda trigger

✔ IAM Role for Lambda



Commands:

aws cloudformation deploy \\

&nbsp; --stack-name sparkleaura-stack \\

&nbsp; --template-file sparkleaura-stack.yaml \\

&nbsp; --capabilities CAPABILITY\_NAMED\_IAM



 4. Python Boto3 Scripts

✔ 4.1 Create S3 Bucket + Upload File



create\_bucket\_upload.py



Runs on your laptop.

Creates a unique bucket and uploads a test file.



python create\_bucket\_upload.py



✔ 4.2 List Running EC2 Instances



list\_ec2.py



Lists all running EC2 instances with type, ID, AZ, and tags.



python list\_ec2.py



✔ 4.3 Invoke Lambda Manually



lambda\_invoke.py



Invokes sparkleaura-s3-logger, sends a test payload.



python lambda\_invoke.py





CloudWatch verifies the Lambda ran successfully.



✔ 4.4 EC2 Metadata Script (runs inside EC2)



metadata.py (uses urllib, no dependencies)



python3 metadata.py





Outputs:



SparkleAura EC2 Metadata:

\- Instance ID: i-xxxx

\- Availability Zone: us-east-1b

\- AMI ID: ami-xxxx



 5. S3 → Lambda Logging



S3 bucket triggers Lambda when files are uploaded.



Lambda prints event data to CloudWatch Logs.



To test:



Upload a file to your S3 bucket.



Check logs:



CloudWatch → Log groups → /aws/lambda/sparkleaura-s3-logger





You will see an entry like:



"eventName": "ObjectCreated:Put"



 6. Accessing the Website (ALB)



After CloudFormation deploys successfully:



Go to EC2 → Load Balancers



Copy ALB DNS → paste in browser



You'll see the SparkleAura welcome page served by EC2 instances.



 7. How to Reproduce the Entire Deployment

1\. Deploy networking (Terraform)

cd terraform

terraform apply



2\. Deploy compute + DB + Lambda (CloudFormation)

aws cloudformation deploy \\

&nbsp; --stack-name sparkleaura-stack \\

&nbsp; --template-file sparkleaura-stack.yaml \\

&nbsp; --capabilities CAPABILITY\_NAMED\_IAM



3\. Run Boto3 scripts

cd boto3

python create\_bucket\_upload.py

python list\_ec2.py

python lambda\_invoke.py



4\. Connect to EC2 \& run metadata script

ssh -i MyNewKeyPair.pem ec2-user@<public-ip>

python3 metadata.py



5\. Validate S3→Lambda trigger



Upload any file → check CloudWatch.



 8. Screenshots Included



The screenshots/ folder contains:



Terraform apply output



CloudFormation stack success



ALB homepage



RDS instance



Lambda CloudWatch logs



Output of all Boto3 scripts



EC2 metadata output



 9. Technologies Used



AWS VPC, Subnets, IGW, Route Tables



EC2 + Launch Templates + Auto Scaling



Application Load Balancer



RDS MySQL



S3 Storage



Lambda (Python 3.9)



CloudWatch Logs



Terraform



CloudFormation



Python Boto3



GitHub


 Final Notes



This project demonstrates production-grade AWS deployment using modern IaC practices and automation.

It also simulates a real-world cloud architecture for an e-commerce jewelry brand.



If you found this helpful, ⭐ star the repo!

