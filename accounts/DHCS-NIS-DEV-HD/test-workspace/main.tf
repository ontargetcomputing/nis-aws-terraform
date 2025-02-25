resource "aws_ssm_parameter" "example" {
  name        = "/myapp/database/password"
  description = "Database password for abc2234567890"
  type        = "SecureString"
  value       = "MySuperSecretPassword"

  tags = {
    Environment = "Sandbox1"
  }
}