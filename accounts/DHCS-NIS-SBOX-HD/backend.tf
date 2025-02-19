terraform {
  backend "remote" {
    hostname     = "app.terraform.io"
    organization = "DHCS"
    workspaces {
      name = "__REPLACE_ME__"
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