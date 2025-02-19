import boto3

def get_stack_resources(stack_name):
    """
    Get all resources from a CloudFormation stack.
    """
    cf_client = boto3.client('cloudformation')
    try:
        response = cf_client.describe_stack_resources(StackName=stack_name)
        return response['StackResources']
    except Exception as e:
        print(f"Error fetching stack resources: {e}")
        return []



def fetch_resource_arn(resource_id, resource_type):
    """
    Fetch the ARN of a resource using specific AWS service APIs.
    Handles various AWS services such as IAM, Lambda, SNS, SSM, etc.
    """
    arn_prefix = "arn:aws"
    region = boto3.session.Session().region_name
    account_id = boto3.client('sts').get_caller_identity()['Account']

    try:
        if resource_type.startswith("AWS::IAM::Role"):
            return f"{arn_prefix}:iam::{account_id}:role/{resource_id}"
        elif resource_type.startswith("AWS::IAM::Policy"):
            return f"{arn_prefix}:iam::{account_id}:policy/{resource_id}"
        elif resource_type.startswith("AWS::IAM::User"):
            return f"{arn_prefix}:iam::{account_id}:user/{resource_id}"
        elif resource_type.startswith("AWS::Lambda::Function"):
            lambda_client = boto3.client('lambda')
            response = lambda_client.get_function(FunctionName=resource_id)
            return response['Configuration']['FunctionArn']
        elif resource_type.startswith("AWS::SNS::Topic"):
            return f"{arn_prefix}:sns:{region}:{account_id}:{resource_id}"
        elif resource_type.startswith("AWS::SSM::Parameter"):
            return f"{arn_prefix}:ssm:{region}:{account_id}:parameter/{resource_id}"
        elif resource_type.startswith("AWS::Events::Rule"):
            return f"{arn_prefix}:events:{region}:{account_id}:rule/{resource_id}"
        elif resource_type.startswith("AWS::Logs::LogGroup"):
            return f"{arn_prefix}:logs:{region}:{account_id}:log-group:{resource_id}"
        elif resource_type.startswith("AWS::CloudWatch::Alarm"):
            return f"{arn_prefix}:cloudwatch:{region}:{account_id}:alarm:{resource_id}"
        elif resource_type.startswith("AWS::DynamoDB::Table"):
            dynamodb_client = boto3.client('dynamodb')
            response = dynamodb_client.describe_table(TableName=resource_id)
            return response['Table']['TableArn']
        elif resource_type.startswith("AWS::KMS::Key"):
            return f"{arn_prefix}:kms:{region}:{account_id}:key/{resource_id}"
        elif resource_type.startswith("AWS::ServiceCatalogAppRegistry::AttributeGroup"):
            appregistry_client = boto3.client('servicecatalog-appregistry')
            response = appregistry_client.get_attribute_group(
                AttributeGroup=resource_id
            )
            return response['Arn']
        elif resource_type.startswith("AWS::ServiceCatalogAppRegistry::Application"):
            appregistry_client = boto3.client('servicecatalog-appregistry')
            response = appregistry_client.get_application(
                Application=resource_id
            )
            return response['Arn']
        elif resource_type.startswith("AWS::KMS::Alias"):
            # resource_id is the alias name (e.g., alias/MyAlias)
            return f"{arn_prefix}:kms:{region}:{account_id}:{resource_id}"
        elif resource_type.startswith("AWS::KMS::Key"):
            return f"{arn_prefix}:kms:{region}:{account_id}:key/{resource_id}"    
        elif resource_type.startswith("AWS::CloudWatch::Dashboard"):
            # resource_id is the dashboard name
            return f"{arn_prefix}:cloudwatch::{region}:{account_id}:dashboard/{resource_id}"
        elif resource_type.startswith("AWS::SSM::Document"):
            # resource_id is the document name
            return f"{arn_prefix}:ssm:{region}:{account_id}:document/{resource_id}"
        elif resource_type.startswith("AWS::ServiceCatalogAppRegistry::Application"):
            appregistry_client = boto3.client('servicecatalog-appregistry')
            response = appregistry_client.describe_application(Application=resource_id)
            return response['Arn']
        elif resource_type.startswith("AWS::CloudWatch::Dashboard"):
            # resource_id is the dashboard name
            return f"{arn_prefix}:cloudwatch::{region}:{account_id}:dashboard/{resource_id}"        
        else:
            print(f"Unsupported or unknown resource type: {resource_type}")
            return None
    except Exception as e:
        print(f"Error fetching ARN for resource {resource_id} of type {resource_type}: {e}")
        return None
    
def tag_resource(resource_arn, tags):
    """
    Tag a single AWS resource if tagging is supported.
    """
    tagging_client = boto3.client('resourcegroupstaggingapi')
    try:
        tagging_client.tag_resources(
            ResourceARNList=[resource_arn],
            Tags=tags
        )
        return True
    except tagging_client.exceptions.InvalidParameterException:
        print(f"Resource does not support tagging: {resource_arn}")
        return False
    except Exception as e:
        print(f"Error tagging resource {resource_arn}: {e}")
        return False

def main():
    # Replace with your stack name and desired tags
    stack_name = "instance-scheduler-stack"
    tags = {
        "IMPORT2": "true"
    }

    # Get resources from the stack
    resources = get_stack_resources(stack_name)
    if not resources:
        print("No resources found for the specified stack.")
        return

    tagged_resources = []  # List of resources successfully tagged
    untagged_resources = []  # List of resources not tagged
    resource_types = set()  # Set of unique resource types (lowercased)

    # Iterate over resources and tag them
    for resource in resources:
        resource_id = resource.get('PhysicalResourceId')
        resource_type = resource.get('ResourceType')

        if resource_type:
            # Add the lowercased resource type to the set
            service_name = resource_type.split("::")[1].lower()
            resource_types.add(service_name)

        if resource_id:
            print(f"Processing resource: {resource_id} of type {resource_type}")
            # Fetch ARN dynamically
            resource_arn = fetch_resource_arn(resource_id, resource_type)
            if resource_arn:
                if tag_resource(resource_arn, tags):
                    tagged_resources.append({"ResourceId": resource_id, "ResourceType": resource_type})
                else:
                    untagged_resources.append({"ResourceId": resource_id, "ResourceType": resource_type})
            else:
                print(f"Resource type does not support tagging or ARN could not be fetched: {resource_type}")
                untagged_resources.append({"ResourceId": resource_id, "ResourceType": resource_type})

    # Print results
    print("\nResources that were successfully tagged:")
    for tagged in tagged_resources:
        print(f"- Resource ID: {tagged['ResourceId']}, Type: {tagged['ResourceType']}")

    print("\nResources that were not tagged:")
    for untagged in untagged_resources:
        print(f"- Resource ID: {untagged['ResourceId']}, Type: {untagged['ResourceType']}")

    print("\nSet of resource types (lowercased):")
    print(", ".join(resource_types))

if __name__ == "__main__":
    main()

