provider "aws" {
  region = var.aws_region
  assume_role {
    role_arn     = "arn:aws:iam::320812455017:role/Terraform-Workspaces-Centralized-IdentityProvider-Target-Role"
    session_name = "terraform_cloud"
  }

  default_tags {
    tags = {
      "DHCS:IacContext"  = terraform.workspace
      "DHCS:version"     = var.semver
    }
  }
}