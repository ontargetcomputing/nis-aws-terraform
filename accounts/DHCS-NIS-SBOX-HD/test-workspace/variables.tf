// Define your infrastructure here
// some examples are below
variable "aws_region" {
  description = "The AWS region to deploy resources in"
  type        = string
  default     = "us-west-2"
}

variable "semver" {
  description = "The version of the infrastructure deployed ( see github tags )"
  type        = string
}


