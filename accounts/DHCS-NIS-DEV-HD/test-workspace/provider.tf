provider "aws" {
  region = var.aws_region
  assume_role {
    role_arn     = "arn:aws:iam::582983609964:role/balutbomber-terraform-admin-role"
    session_name = "terraform_cloud"
  }

  default_tags {
    tags = {
      "DHCS:Environment" = var.environment
      "DHCS:IacContext"  = terraform.workspace
    }
  }
}