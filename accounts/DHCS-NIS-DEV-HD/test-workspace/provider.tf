provider "aws" {
  region = var.aws_region


  default_tags {
    tags = {
      "DHCS:IacContext"  = terraform.workspace
      "DHCS:version"     = var.version
    }
  }
}
