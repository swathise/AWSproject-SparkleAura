variable "project_name" {
  description = "Project name prefix"
  type        = string
  default     = "sparkleaura"
}

variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "vpc_cidr" {
  description = "VPC CIDR block"
  type        = string
  default     = "10.0.0.0/16"
}

variable "public_subnet_cidr" {
  description = "Public subnet CIDR block"
  type        = string
  default     = "10.0.1.0/24"
}

variable "private_subnet_cidr" {
  description = "Private subnet CIDR block"
  type        = string
  default     = "10.0.2.0/24"
}

variable "allowed_ssh_cidr" {
  description = "CIDR allowed to SSH into EC2 (your IP)"
  type        = string
  # later we can change this to your IP like "x.x.x.x/32"
  default     = "0.0.0.0/0"
}

variable "public_subnet2_cidr" {
  description = "Second public subnet CIDR block"
  type        = string
  default     = "10.0.4.0/24"
}

variable "private_subnet2_cidr" {
  description = "Second private subnet CIDR block"
  type        = string
  default     = "10.0.3.0/24"
}

