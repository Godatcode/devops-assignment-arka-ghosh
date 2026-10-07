# Session 18: Terraform and AWS services

[`terraform-s3-demo`](terraform-s3-demo) defines a private, versioned, encrypted S3 bucket. Set a globally unique name in a local `terraform.tfvars`, then use:

```bash
terraform init
terraform fmt -check
terraform validate
terraform plan -out=plan.tfplan
terraform apply plan.tfplan
terraform show
terraform output
terraform destroy
```

Do not commit state, the plan, credentials, or a real tfvars file. AWS credentials and billing access are required for plan/apply; the local files are infrastructure code, not proof that an AWS bucket was created. Service research is organized under [`aws-services`](aws-services).

## Validation result

Terraform 1.9.8 completed `terraform init -backend=false`, `terraform fmt -check`, and `terraform validate` successfully on 7 October 2026. No AWS plan or apply was run because this environment has no approved AWS deployment for the assignment.
