# Importing Console-Provisioned Resources

This guide outlines the process for importing AWS resources that were manually provisioned through the AWS Management Console. The steps include identifying resources to import and leveraging the tagging-based import process described in the [Import Resources via Import Tag](./Tagged_Resources_Import.md) document.

---

## Steps for Importing Console-Provisioned Resources

### 1. Identify Resources to Import

Before importing resources, gather detailed information about the resources provisioned through the AWS Console. This includes:

- **Resource type** (e.g., EC2 instance, S3 bucket, VPC, RDS database).
- **Resource identifiers** (e.g., instance IDs, bucket names, VPC IDs).
- **AWS Region** where the resources are located.
- **Environment and account** associated with the resources.

#### Best Practices for Identification

- Use the **AWS Resource Groups** or **AWS Tag Editor** to filter and list resources. This can help you identify resources across the account and region efficiently.
- Check existing tags on resources to understand their purpose and whether they belong to the environment being imported.
- Confirm with stakeholders or application teams to ensure the correct resources are identified for import.

---

### 2. Prepare Resources for Import

Once the resources have been identified:

1. **Review Existing Tags**:  
   - Check if the resources already have a **Name** tag. If they don’t, add one with a meaningful value, as this tag is critical for the import process.
   - Ensure no existing tags conflict with the unique **Import Tag** you will apply.

2. **Apply Import Tag**:  
   Follow these steps:
   - Choose a unique tag key to identify the resources for import (e.g., `IMPORT_YYYYMMDD`).
   - Add the tag to all identified resources. You can do this manually in the AWS Console or programmatically using the AWS CLI:
     ```bash
     aws resourcegroupstaggingapi tag-resources \
       --resource-arn-list <arn1> <arn2> \
       --tags <TAG_KEY>=<TAG_VALUE>
     ```
   - Ensure that each resource has a **Name** tag, as this will be used for naming in the Terraform configuration.

---

### 3. Use the Tagging Import Process

After tagging the resources, use the [Import Resources via Import Tag](./Tagged_Resources_Import.md) guide to complete the import process. This involves:

- Opening a pull request to track the import.
- Triggering the import workflow via GitHub Actions.
- Reviewing and fixing any issues in the generated Terraform configuration.

---

### 4. Validate the Import

Once the resources are imported into Terraform:

- Run `terraform plan` to verify that all resources have been correctly added to the state and that there are no unexpected changes.
- Confirm that resource attributes (e.g., tags, configurations) match their settings in AWS.
- Check the state file to ensure all intended resources are represented.

---

## Example Workflow

1. Identify an EC2 instance (`i-1234567890abcdef`) and an S3 bucket (`my-bucket`) in the `us-west-2` region.
2. Tag both resources:
   - Import Tag: `IMPORT_20231212`
   - Name Tag: Use a descriptive value (e.g., `WebServer` for the EC2 instance and `AppBucket` for the S3 bucket).
3. Follow the steps in [Import Resources via Import Tag](./Tagged_Resources_Import.md) to:
   - Trigger the import workflow.
   - Review and fix the generated Terraform configuration.
   - Sync the state with Terraform Cloud.
4. Merge the pull request to finalize the import.

---

### Key Notes

- **Accuracy is Crucial**: Ensure all resources are tagged correctly and that the import includes only the intended resources.
- **Test in Non-Production**: Perform imports in a test or staging environment first to validate the process before applying to production resources.
- **Iterative Imports**: Import resources incrementally to simplify troubleshooting and reduce the risk of errors.

