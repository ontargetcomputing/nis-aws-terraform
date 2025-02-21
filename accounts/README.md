# Accounts Directory

## Overview
The `accounts/` directory organizes infrastructure configurations by AWS account. Each subfolder corresponds to a specific AWS account and is further divided into directories for managing baseline infrastructure and application-specific workloads. RDB

## Directory Structure

```
├── accounts/           				# Separate folders for each AWS account
│   ├── <account_name>/
│   │   ├── infrastructure/         # Terraform managed by the NIS-AWS team
│   │   │   └── <infra_workspace>/  	# First workspace for baseline configurations
│   │   │   └── <another_infra_workspace>/  # Second workspace for baseline configurations
│   │   │   └── …                   	  # Additional infrastructure workspaces as needed
│   │   └── applications/   # GitHub submodule for app dev team Terraform code
```

### Subfolder Details
- **`<Account-Name>/`**  
  Each subfolder represents an AWS account, identified by a folder with the same name of the account as seen in the **AWS access portal**:

  Inside each account folder:

  - **`infrastructure/`**:  
    Contains Terraform configurations managed by the NIS-AWS team. These configurations define foundational infrastructure such as networking, IAM roles, logging, and monitoring.

    - **`infra-workspace-*/`**:  
      Each `infra-workspace` directory represents a separate Terraform workspace for managing a distinct set of baseline resources. For example:
      - `infra-workspace-networking/` for VPC, subnets, and networking resources.
      - `infra-workspace-logging/` for CloudWatch, logs, and monitoring configurations.
      - `infra-workspace-security/` for IAM roles, security groups, and related resources.

      This structure allows the NIS-AWS team to divide baseline configurations into logical units, enabling better scalability and easier management.

  - **`applications/`**:  
    A GitHub submodule for Terraform configurations managed by the application development team. This is where app-specific workloads and resources are defined.

## Best Practices
- **Organize Baseline Configurations**: Divide baseline infrastructure into logical workspaces within the `infrastructure/` directory. Each workspace should focus on a specific aspect of the account’s foundational setup (e.g., networking, security, monitoring).
- **Use Descriptive Names**: Name the `infra-workspace-*` directories based on their purpose (e.g., `infra-workspace-networking`, `infra-workspace-security`) to ensure clarity and ease of navigation.
- **Single Workspace per Branch**:  
  Limit changes in a single branch or pull request to a single workspace. This ensures focused, manageable changes, reduces conflicts, and simplifies reviews and deployments.
- **Branching Strategy**: Use feature branches for changes and follow the repository's pull request and CI/CD processes.
- **Keep Workspaces Isolated**: Maintain clear boundaries between workspaces to prevent interdependencies that complicate deployments.

## Workflow Notes
1. **Baseline Changes**:  
   Baseline configurations are managed by the NIS-AWS team. Changes are made in individual `infra-workspace-*` directories, following the standard process of branch creation, CI/CD validation, peer review, and manual apply approval via Terraform Cloud.

2. **Multiple Workspaces**:  
   Each `infra-workspace-*` directory operates as a standalone Terraform workspace. This structure allows for isolated state management and simplifies the deployment process for large, complex accounts.

3. **Customer Changes**:  
   Customer workload configurations are managed by the application development team and housed in the `applicatons/` directory as a GitHub submodule.

## Contact
For any questions or issues related to the `accounts/` directory structure, please contact the NIS-AWS team.