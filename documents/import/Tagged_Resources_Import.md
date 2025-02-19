# How to Import Resources via Import Tag

This guide provides detailed instructions for importing AWS resources tagged with a unique identifier to signify they should be imported. This process is used for both console-provisioned and CloudFormation-provisioned resources.

## Steps for Importing Resources via Unique Tag
### Identify and Tag the Resources to Import

1. **Determine Resources to Import**: Gather the following details for each resource:
   - **Resource type** (e.g., VPC, EC2 instance, S3 bucket)
   - **AWS Region** where the resource resides
   - **Resource identifiers** (e.g., instance IDs, bucket names)

   **NOTE**: While Terraform workspaces can manage resources across accounts and regions, this process currently supports only single-account, single-region imports. Future enhancements may allow for multi-account/region imports.
   

### Tagging Resources for Import

Two tags are required for this process:

1. **Import Tag**: A unique tag to identify resources for import. Terraformer uses this tag to filter and select the resources.
2. **Name Tag**: The value of this tag will be used to name the imported resource in the generated Terraform configuration.

#### Steps to Tag Resources for Import:

1. **Choose a Unique Import Tag**:  
   Select a distinctive tag key (e.g., `IMPORT_10302024`) to identify the resources for import. Ensure it’s specific to avoid unintended imports.

2. **Apply Tags to Resources**:  
   In the AWS Console:
   - Add the **Import Tag** to each resource:
     - **Key**: `IMPORT_10302024`
     - **Value**: Optional but can be descriptive.
   - Add a **Name Tag** with a meaningful value for each resource.
     
### Open a Pull Request and Update the Import Log

1. **Create a new branch**
	
	```bash
	git branch -b <branch_name>
	```
1. **Update the Import Log**:  
   Update the [Import Log](./IMPORT_LOG.md) with details of the resources to be imported. Follow the [Import Log Instructions](./IMPORT_LOG_INSTRUCTIONS.md).
  
1. **Commit the changes and push to central repository**
	
	```bash
	git add .
	git commit -m "Updated import log for <TAG_NAME>"
	git	 push origin <branch_name>
	```
1. **Open a Pull Request (PR)**:  
   Open a new PR in GitHub targeting the main branch.

### Trigger the Import Workflow

1. **Navigate to GitHub Actions**:  
   In your GitHub repository, go to the **Actions** tab and locate the [1 - Import Tagged Resources Workflow](../../.github/workflows/import_tagged_resources.yml).

2. **Choose the Correct Branch**:  
   When triggering the workflow, ensure you select the branch associated with your pull request. This ensures the workflow operates on the intended changes.

3. **Provide Workflow Inputs**:  
   When prompted, provide the following inputs:
   - **Workspace Path**:  
     Select the Terraform workspace path corresponding to the resource’s environment. This is a dropdown list—choose the correct value based on the account and environment for the resources being imported.
   - **Resources**:  
     Provide a comma-separated list of resource types to import (e.g., `vpc,s3`).  
     **Important**:  
       - Do not include spaces in the list (e.g., use `vpc,s3`, not `vpc, s3`).
       - Avoid using the `*` wildcard due to a known Terraformer bug.
   - **AWS Region**:  
     Specify the AWS region where the resources are located (e.g., `us-west-2`).

	**Note**: Double-check the following before starting the workflow:
	
	- You’ve selected the correct branch.
	- The workspace path matches the resource’s environment.
	- The resource list is accurate and formatted correctly (comma-separated, no spaces).
	- The AWS region is correct for the resources being imported.

5. **What the Workflow Does**:  
   The workflow will perform the following actions:
   - **Plan Import with Terraformer**:  
     Runs Terraformer to generate a `plan.json` file for the specified resources.
   - **Run `cook_plan.py`**:  
     Processes the `plan.json` file to:
     - Ensure each resource has a `Name` tag.
     - Update resource names using the `Name` tag for more meaningful identifiers.
     - Exit with an error if any resource lacks a `Name` tag, requiring you to add it in AWS.
   - **Generate Configuration Files**:  
     Creates `.tf` files for the imported resources in the following format:
     - State file: `<Workspace_Path>/terraform_<TAG_NAME>.tfstate`
     - Configuration files: `<Workspace_Path>/<Resource_Type>_<TAG_NAME>.tf`
   - **Commit Files to the PR**:  
     Pushes the generated state and configuration files to the branch associated with the PR.
   - **Run Terraform Plan**:  
     Executes a `terraform plan` to detect potential issues in the generated configuration. Note that due to how Terraform separates state and configuration, you may need to manually fix the `.tf` files to resolve issues.

6. **Monitor Workflow Logs**:  
   Check the workflow logs for any errors or warnings. Address issues as needed before proceeding to the next step.

---

### Common Workflow Errors and Resolutions

- **Error: Missing `Name` Tag**  
  - **Cause**: A resource does not have a `Name` tag, which is required for the `cook_plan.py` script to process the plan.  
  - **Solution**: Add a `Name` tag to the resource in the AWS Console and re-trigger the workflow.

- **Error: Invalid Resource List Format**  
  - **Cause**: The resource list input is incorrectly formatted (e.g., includes spaces or uses `*`).  
  - **Solution**: Ensure the list is comma-separated with no spaces (e.g., `vpc,s3`) and avoid using the wildcard (`*`).

- **Error: Workflow Did Not Execute**  
  - **Cause**: The workflow was triggered without an active pull request or on the wrong branch.  
  - **Solution**: Ensure the workflow is triggered within an open PR and that the correct branch is selected.

---

**Next Steps After Workflow Completion**:  
- If the workflow completes successfully, proceed to [Fix Configuration](#fix-configuration) to address any issues in the generated Terraform configuration.
- If the workflow fails, review the logs and address any reported errors (e.g., missing `Name` tags or invalid inputs).

### Fix configuration

If the initial terraform plan detects issues, resolve them as follows:

1. **Pull the latest changes**
 
 ```bash
	git pull --rebase origin <branch_name>
	cd <Workspace_Path>
 ```

1. **Make Changes**  

   Update the generated .tf files to address configuration issues.
      
1. **Local Validation and Planning**

   Developers can optionally run validation and planning locally to ensure their changes are syntactically correct and do not introduce unintended changes:

   ```bash
   terraform init
	terraform validate
	terraform plan -var-file="env/prod.tfvars"
	```
1. **Push Fixed Configuration**

   Once the configuration issues are resolved:
   
   ```bash
git add .
git commit -m "Fixed Terraform configuration for <TAG_NAME>"
git push origin <branch_name>
	```

1. **Request Peer Review**

	Request a peer review for the PR to ensure the changes meet standards and requirements.   

1. **Sync and Plan**

	Manually trigger the [2 - Sync state and plan](../../.github/workflows/sync_and_plan.yml) Workflow in GitHub Actions. Provide the following input:

	•	**Workspace Path:** Select the Terraform workspace path corresponding to the resource’s environment.

	**Workflow Actions**:

	•	Sync the new state with Terraform Cloud.

	•	Run a terraform plan to verify the imported state.  
  
1. **Merge the Pull Requset**

Once all workflows pass and the review is approved, merge the PR into the main branch to finalize the import process.

