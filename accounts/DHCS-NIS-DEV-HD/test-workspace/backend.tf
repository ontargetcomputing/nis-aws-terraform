terraform {
  backend "remote" {
    hostname     = "app.terraform.io"
    organization = "DHCS"
    workspaces {
      name = "dddd"
    }
  }
  required_providers {
    aws = {
      source = "hashicorp/aws"
    }
    local = {
      source = "hashicorp/local"
    }
  }
}