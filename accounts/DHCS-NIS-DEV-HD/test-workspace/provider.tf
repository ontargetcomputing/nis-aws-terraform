provider "aws" {
  region = var.aws_region


  default_tags {
    tags = {
      "DHCS:Environment" = var.environment
      "DHCS:IacContext"  = terraform.workspace
    }
  }
}