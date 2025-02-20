// Define your outputs here
// see examples below
output "aws_region" {
  description = "The AWS region used for deployment"
  value       = var.aws_region
}

output "environment" {
  description = "The deployment environment"
  value       = var.environment
}
