variable "aws_region" {
  type    = string
  default = "ap-south-1"
}

variable "project_name" {
  type    = string
  default = "devops-assignment"
}

variable "bucket_name" {
  type        = string
  description = "Globally unique S3 name"
}
