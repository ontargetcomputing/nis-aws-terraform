import argparse
import json
import os
import sys

# ArgumentParser to require the path to the plan file
parser = argparse.ArgumentParser(description="Cook the terraformer plan, replacing names")
parser.add_argument('file_path', type=str, help='Path to the terraformer plan JSON file')

args = parser.parse_args()

# make sure the plan exits
if not os.path.exists(args.file_path):
    print(f"Error: The file at {args.file_path} does not exist.")
    exit(1)

# let's parse the plan
with open(args.file_path, 'r') as file:
    try:
        data = json.load(file)
    except json.JSONDecodeError as e:
        print(f"Error: Failed to decode JSON - {e}")
        exit(1)

# Check for the resources to import.  If there are none, let's just exit
if 'ImportedResource' not in data:
    print("Error: 'ImportedResource' key not found in the JSON file.")
    exit(1)

resources_without_name_tag = []

imported_resources = data['ImportedResource']
for resource_type, resources in imported_resources.items():
    for resource in resources:
        # Check for Name tag in Item['tags']
        item_tags = resource.get('Item', {}).get('tags', {})
        name_tag = item_tags.get('Name', None)
       
        # Collect all the resources without a Name tag, we want the Name for our TF resource name
        if not name_tag:
            print(f"Unable to find 'Name' tag on {resource['ResourceName']}")
            resources_without_name_tag.append(resource['ResourceName'])
 
        # Modify the ResourceName to the name tag value to rid us of the goofy terraformer name given
        else:
            print(f"Renaming {resource['ResourceName']} to {name_tag}")
            resource['ResourceName'] = name_tag
 
# exit if any of the resources are missing the name tag.  should be fixed and run again.
if resources_without_name_tag:
    print(f"Error: The following resources do not have a 'Name' tag:")
    for resource_name in resources_without_name_tag:
        print(f"  - {resource_name}")
    
    print(f"Error: Please ensure each of the above resources has a 'Name' tag and rerun.")
    sys.exit(1)
 
# output the updated plan json to a new file cooked_plan.json
input_directory = os.path.dirname(args.file_path)
output_file = os.path.join(input_directory, 'cooked_plan.json')
with open(output_file, 'w') as outfile:
    json.dump(data, outfile, indent=4)
 
print(f"Cooked plan has been written to {output_file}")


