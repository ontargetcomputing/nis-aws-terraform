# Importing CloudFormation-Managed Resources

This guide provides instructions for importing AWS resources that are managed by CloudFormation stacks into Terraform. The process includes identifying resources, tagging them for import, and using the [Import Resources via Import Tag](./Tagged_Resources_Import.md) guide to bring them under Terraform management.

---

## Steps for Importing CloudFormation-Managed Resources

### 1. Identify Resources to Import

To import resources from a CloudFormation stack:

1. **List the Resources in the Stack**:  
   Use the AWS Management Console, CLI, or SDK to identify the resources managed by the stack:
   - In the AWS Console, navigate to the **CloudFormation** service.
   - Select the stack and review the **Resources** tab for a detailed list of all managed resources.

   Example CLI command to list stack resources:
   ```bash
   aws cloudformation describe-stack-resources --stack-name <stack-name>
   ```
   
1. **Prioritize Resources**:  
 Decide which resources to import based on their importance and complexity. Avoid importing dependent resources all at once to reduce the risk of errors.
 
1. **Confirm Permissions**:  
 Ensure you have the necessary permissions to modify or delete the CloudFormation stack and its resources. Lack of permissions may lead to errors during the import process.
 
### 2. Plan the Transition

1. **Evaluate Stack Dependencies**:  
   CloudFormation resources are often interdependent. Review the stack’s outputs and inputs to identify dependencies that may need special handling during the import process. Ensure you understand how these dependencies affect other resources.

2. **Decide the Scope**:  
   Determine whether you are importing the entire stack or specific resources:
   - **Entire Stacks**: Importing an entire stack is rarely recommended due to its complexity and potential for risk. Proceed cautiously and only if the stack has minimal dependencies.
   - **Individual Resources**: Importing specific resources is more manageable and reduces risk. This is the preferred method for most use cases.

3. **Choose a Unique Import Tag**:  
   Select a unique tag key to identify the resources for import. For example:
   - `IMPORT_CF_YYYYMMDD` where `YYYYMMDD` represents the date.
   - Ensure the tag key is distinct to avoid including unintended resources.

4. **Document the Transition Plan**:  
   Create a transition plan that includes:
   - The resources being imported.
   - Any known dependencies or relationships.
   - A rollback plan in case issues arise during the import process.
   - This should be completed in the [Import Log](./IMPORT_LOG.md).

   
### 3. Tag Resources for Import

To tag the resources managed by the CloudFormation stack:

1. **Use the AWS Console or CLI**:  
   Apply the following tags to each resource:
   - **Import Tag**: A unique tag to identify resources for import (e.g., `IMPORT_CF_20231212`).
   - **Name Tag**: A descriptive name for the resource, which will be used to generate the Terraform configuration.

2. **Example CLI Command to Tag Resources**:  
   Use the following command to tag resources programmatically:
   
   ```bash
   aws resourcegroupstaggingapi tag-resources \
     --resource-arn-list <arn1> <arn2> \
     --tags ImportTag=IMPORT_CF_20231212 Name=<ResourceName>
  ```
  
3. **Verify Tags**:  
   Ensure all resources to be imported have both the Import Tag and Name Tag applied before proceeding. Resources missing these tags will not be included in the import process.
   
### 4. Use the Tagging Import Process

Once the resources are tagged, follow the steps outlined in the [Import Resources via Import Tag](./Tagged_Resources_Import.md) document to complete the import process.

### 5. Validate and Clean Up

After successfully importing the resources into Terraform, follow these steps to ensure the process is complete and accurate:

1. **Run Terraform Plan**:  
   Verify that all imported resources are correctly added to the Terraform state and that no unexpected changes are detected:
   
   ```bash
   terraform plan
   ```
   
   - Review the plan output to ensure all resources are accounted for.
	- Confirm that no existing resources are being modified or deleted unintentionally.
	- Address any errors or issues in the configuration files as needed.

1. **Test Resource Behavior**:  
   Confirm that the imported resources function as expected in their environment:
   
	- Check Resource Dependencies: Ensure dependencies like linked security groups, VPCs, IAM roles, or other connected resources are intact.
	- Verify Application Functionality: If the imported resources are part of a running application, confirm that the application behaves as expected.
   
#### 3. Clean Up the CloudFormation Stack

Once the imported resources are fully managed by Terraform, follow these steps to safely clean up the original CloudFormation stack:

1. **Review Dependencies**:  
   Before deleting the CloudFormation stack, ensure that no critical dependencies rely on it. Review the stack’s outputs, parameters, and resources to verify that:
   - All dependencies have been successfully transitioned to Terraform management.
   - No other stacks, applications, or services are dependent on the resources managed by the stack.

2. **Delete or Retain the Stack**:  
	**<span style="color:red">To Be Determined.  Should we delete the stack or retain?  Need to work this out.</span>**
	
   
#### Document the Cleanup

After cleaning up the CloudFormation stack, update the [Import Log](./IMPORT_LOG.md) to reflect the changes. This step ensures transparency and provides a clear record for future reference.

1. **Record the Stack Removal**:  
   Include details about the stack that was removed:
   - **Stack Name**: The name of the deleted CloudFormation stack.
   - **Date of Removal**: The date when the stack was deleted.
   - **Notes**: Any relevant notes, including issues encountered or special considerations during the deletion process.

2. **Update the Resource Inventory**:  
   Ensure the resource inventory or Terraform documentation includes:
   - Resources transitioned from the stack to Terraform management.
   - The Terraform workspace managing the resources.
   - Any specific configurations or dependencies that were addressed.

3. **Share the Documentation**:  
   Notify relevant stakeholders (e.g., application teams, cloud administrators) about the stack removal and provide them with links to the updated documentation.

---

**Example Documentation Entry:**
	
	•	Stack Name: MyAppStack
	•	Deleted On: 2023-12-12
	•	Notes:
		•	Successfully transitioned all resources to Terraform management.
		•	No issues encountered during the stack deletion process.
		•	Verified that no dependencies remained tied to the CloudFormation stack.
	•	Resources Transferred:
		•	RDS Instance:
			•	Name: MyDatabase
			•	Terraform Workspace: prod-database
		•	Security Group:
			•	Name: MyDBSecurityGroup
			•	Terraform Workspace: prod-database