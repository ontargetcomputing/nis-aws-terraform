# Import Log Overview and Instructions

The **Import Log** is a critical document that records details about each AWS resource imported into Terraform, providing a central history of all imported resources, environments, and workspace destinations. This log helps maintain clarity over which resources are managed in Terraform, streamlines tracking, and aids in auditing changes over time.

## How to Set Up the Import Log

1. **Create the Import Log File**:  
   Add a file named `documents/import/IMPORT_LOG.md` to your repository. This file will store entries for each import action performed.

2. **Organize Entries by Date**:  
   Each import should include a date-stamped entry with relevant details. Use headers or sections to group imports by date for quick reference.

3. **Provide Descriptive Details**:  
   For each import, include key details like the resource type, destination workspace, AWS region, and any relevant descriptions.

## Import Log Template

Below is a recommended template for recording import details. You can copy this structure for each new entry:

```markdown
# Import Log

## Entries

### Import Entry - YYYY-MM-DD

- **Resource**: [Resource Type - Resource Identifier]
  - **Example**: VPC - `vpc-12345`, EC2 Instance - `i-1234567890abcdef`
- **Destination Workspace**: `[Path to Terraform Workspace]`
  - **Example**: `accounts/SBOX-9394/baseline/baseline-workspace`
- **Region**: `[AWS Region]`
  - **Example**: us-west-2
- **Import Tag**: The unique tag on the resource if imported console provisioned
- **Workspace**: The Terraform workspace if importing from an existing workspace.
- **Stack**: CloudFormation stack if importing from an existing ClougFormation Stack.
- **Description**: `[Brief description of the import purpose or context]`
  - **Example**: Initial import of VPC for development environment.