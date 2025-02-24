terraform {
  backend "remote" {
    hostname     = "app.terraform.io"
    organization = "balutbomber"
    workspaces {
      name = "dhcs-nis-dev-hd-test-workspace"
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