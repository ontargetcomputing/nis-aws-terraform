# Importing Existing Resources

Integrating existing resources into a new or consolidated Terraform workspace requires a tailored approach for each type of resource. This document provides an overview of the import process and guides users to detailed instructions based on the original management source of the resources.

## Background

NIS AWS currently supports cloud resources deployed through various tools and processes, including:

- **Terraform-managed resources**: Resources tracked by other Terraform workspaces.
- **CloudFormation-managed resources**: Resources provisioned and managed through AWS CloudFormation stacks.
- **Console-provisioned resources**: Resources created manually via the AWS Management Console and not managed by Infrastructure as Code (IaC).

Standardizing these resources under Terraform management ensures consistent configuration, centralized control, and improved automation. The import process involves:

1. Identifying the original management tool or source.
2. Handling dependencies and relationships between resources.
3. Accurately mapping each resource's state to Terraform to avoid conflicts or disruptions.


## Import Guidelines

The process for importing resources varies depending on how they were originally managed. Follow the appropriate guide for step-by-step instructions:

- **[Terraform-Managed Resources](./Terraform_Managed_Import.md)**  
  Resources currently managed by other Terraform workspaces must be migrated carefully to avoid state conflicts.

- **[CloudFormation-Managed Resources](./CloudFormation_Managed_Import.md)**  
  Resources provisioned using AWS CloudFormation stacks require special attention to avoid disrupting existing stack dependencies.

- **[Console-Provisioned Resources](./Console_Provisioned_Import.md)**  
  Resources created manually in the AWS Console can be imported directly into Terraform but require accurate configuration mapping to prevent issues.
  

## General Tips for Importing

- **Backup State Files**:  
  Always back up the existing Terraform state files or relevant resource configurations before starting the import process. This ensures you have a recovery point if issues arise.

- **Accurate Configuration Mapping**:  
  Ensure your Terraform configurations match the attributes of the resources being imported. Inaccuracies can lead to errors or mismatches during the import process.

- **Use a Test Environment**:  
  Validate the import process in a non-production environment before applying changes to production resources. This minimizes the risk of impacting critical systems.

- **Document Dependencies**:  
  Record dependencies and relationships between resources to avoid breaking integrations during the import process. Proper documentation helps ensure a smooth transition.

- **Incremental Imports**:  
  Import resources incrementally, focusing on one resource or a small group of related resources at a time. This approach makes troubleshooting easier and reduces the likelihood of errors.

By following these tips, you can streamline the import process, reduce risks, and ensure reliable infrastructure management under Terraform.


## Common Challenges and Solutions

- **Missing Attributes**:  
  Ensure all required attributes for a resource are defined in your Terraform configuration before importing. Refer to the [Terraform Resource Documentation](https://registry.terraform.io/) for details on required and optional attributes.

- **Circular Dependencies**:  
  If resources have circular dependencies, break the dependencies temporarily during the import process and restore them after successful import.

- **State Conflicts**:  
  When importing into an existing workspace, use `terraform state rm` to remove conflicting resources from the state before re-importing them.
  
## Pre-Import Checklist

Before starting the import process, ensure the following:

- [ ] Backup existing state files.
		To export the state from Terraform Cloud, use:
		  ```bash
		  terraform state pull > backup.tfstate
		  ```
- [ ] Verify Terraform configuration files are complete and accurate.
- [ ] Identify all dependencies for the resource being imported.
- [ ] Test the import process in a non-production environment.
- [ ] Ensure access to the required permissions for managing resources.

## Post-Import Validation

After importing resources, perform the following checks:

- Run `terraform plan` to verify that there are no pending changes or misconfigurations:
  
  ```bash
  terraform plan
  ```