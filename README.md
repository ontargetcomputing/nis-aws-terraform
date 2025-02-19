# nis-aws-terraform

## Overview

This repository contains Terraform configurations for deploying and managing infrastructure across multiple AWS accounts. By leveraging Terraform’s modular design, this setup ensures consistent deployment of cloud resources while maintaining separation of environments (e.g., development, staging, production) across different AWS accounts.


## ✅ Prerequisites
Before using this repository, ensure the following prerequisites are met:

- **Terraform Installed**  
  Install the latest version of Terraform. Refer to the [Terraform installation guide](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli).

- **Terraform Cloud Access**  
  Ensure you have access to the Terraform Cloud workspace(s) used for managing state. See the [Terraform Cloud documentation](https://developer.hashicorp.com/terraform/cloud).

- **Git Installed**  
  Ensure Git is installed for managing this repository. Download it from the [Git website](https://git-scm.com/).

## 📂 Repository Structure

The repository is organized as follows:

```
├── .github/            				# GitHub-specific configurations
│   └── workflows/      				# CI/CD pipelines for automated processes
├── accounts/           				# Separate folders for each AWS account
│   ├── <account_name>/
│   │   ├── infrastructure/         # Terraform managed by the NIS-AWS team
│   │   │   └── <infra_workspace>/  	# First workspace for baseline configurations
│   │   │   └── <another_infra_workspace>/  # Second workspace for baseline configurations
│   │   │   └── …                   	  # Additional infrastructure workspaces as needed
│   │   └── applications/   # GitHub submodule for app dev team Terraform code
│   ├── <account_name_2>/       # Example Account 1
│   │   ├── infrastructure/   # Terraform managed by the NIS-AWS team
│   │   └── applications/  # GitHub submodule for app dev team Terraform code
│   └── <account_name_3>/       # Example Account 2
│       ├── infrastructure/   # Terraform managed by the NIS-AWS team
│       └── applications/    # GitHub submodule for app dev team Terraform code
├── documents/ 
│   └── imports/        # Guides and information on importing resources into Terraform
├── modules/            # Custom Terraform modules
└── README.md           # Start here
```
### Folder Details
- **`.github/workflows/`**  
  Contains CI/CD pipeline configurations for automating workflows. Common use cases include:
  - Linting and validating Terraform code.
  - Running automated tests.
  - Applying Terraform changes via pull requests.
- **`accounts/`**  
  Each folder corresponds to a specific AWS account. Within each account folder:
  - **`infrastructure/`**: Contains Terraform configurations managed by the NIS-AWS team. These configurations define foundational resources and account-level infrastructure.
    	- **`infra_workspace/`**: Allows the NIS-AWS team to organize baseline configurations into multiple Terraform workspaces if needed.
  - **`applications/`**: A GitHub submodule used by the application development team. This folder houses Terraform configurations for workloads specific to the applications deployed in that account.
- **`documents/`**  
  Contains documentation related to the repository, processes, and workflows.
  - **`imports/`**: Provides detailed guides and instructions for importing existing AWS resources into the Terraform workspaces. Use these resources to standardize infrastructure management.
- **`modules/`**  
  Contains reusable Terraform modules for common infrastructure patterns. Use these modules to define and deploy shared components across multiple environments.
- **`README.md`**  
  This file provides an overview of the repository, usage instructions, and best practices for managing infrastructure across multiple AWS accounts.
- **`modules/`**  
  Contains reusable Terraform modules for common infrastructure patterns. Use these modules to define and deploy shared components across multiple environments.

---
## 📖 Contributing

Please read the [Contributing Guide](./CONTRIBUTING.md) before submitting a Pull Request.

---

## 🏗️➡️📝 Importing Existing Resources

In cases where resources already exist in your AWS accounts, you can import them into Terraform for consistent management. Resources may be:

	•	Managed by Terraform in different workspaces.
	•	Created through CloudFormation stacks.
	•	Provisioned directly via the AWS Management Console or CLI.

Follow the steps outlined in the [Importing Existing Resources Guide](./documents/import/README.md) to consolidate these resources into this Terraform configuration.

---

## 💡General Tips
- Check logs for detailed error messages in GitHub Actions or Terraform Cloud.
- Validate and test your changes locally before pushing to a branch.
- Use `terraform plan` regularly to preview changes and catch potential issues early.
- Regularly sync your branch with the main branch to reduce the likelihood of conflicts:

  ```sh
  git pull --rebase origin main
  ```