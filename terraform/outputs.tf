output "vpc_id" {
  description = "ID of the main VPC"
  value       = aws_vpc.main.id
}

output "public_subnet_id" {
  description = "ID of the public subnet"
  value       = aws_subnet.public_subnet.id
}

output "private_subnet_id" {
  description = "ID of the private subnet"
  value       = aws_subnet.private_subnet.id
}

output "alb_sg_id" {
  description = "Security group ID for ALB"
  value       = aws_security_group.alb_sg.id
}

output "ec2_sg_id" {
  description = "Security group ID for EC2"
  value       = aws_security_group.ec2_sg.id
}

output "rds_sg_id" {
  description = "Security group ID for RDS"
  value       = aws_security_group.rds_sg.id
}

output "private_subnet2_id" {
  description = "ID of the second private subnet"
  value       = aws_subnet.private_subnet2.id
}

output "public_subnet2_id" {
  description = "ID of the second public subnet"
  value       = aws_subnet.public_subnet2.id
}

