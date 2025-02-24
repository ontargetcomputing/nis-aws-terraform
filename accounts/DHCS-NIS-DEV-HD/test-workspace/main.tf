resource "aws_ssm_parameter" "example" {
  name        = "/myapp/database/password"
  description = "Database password for Mddddddddppaaaa"
  type        = "SecureString"
  value       = "MySuperSecretPassword"

  tags = {
    Environment = "Sandbox1"
  }
}