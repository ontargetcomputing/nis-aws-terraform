# Terraform Workspace Template

## 📌 Overview
This `.templates` directory contains standard Terraform files to help you quickly set up a new Terraform workspace. Instead of writing Terraform files from scratch, you can copy these templates into a new workspace directory and customize them as needed.

## 📂 Directory Structure
```
.templates/
  │── providers.tf    # Defines Terraform providers (AWS, local, etc.)
  │── variables.tf    # Defines input variables (e.g., region, account number)
  │── outputs.tf      # Defines output values
  │── main.tf         # Example resource to start with
  │── backend.tf      # Defines Terraform Cloud backend (replace workspace name)
```

## 🛠 How to Use These Templates

### 1️⃣ **Create a New Terraform Cloud (TFC) Workspace**
Before using these templates, you must create a **Terraform Cloud workspace**.

#### **Option 1: Create Workspace in Terraform Cloud UI**
1. **Go to Terraform Cloud:**  
   👉 [Terraform Cloud Workspaces](https://app.terraform.io/app/DHCS/workspaces)
2. **Click "New Workspace"**
3. **Choose "CLI-Driven Workflow"** 
4. **Enter the workspace name** (e.g., `NIS-AWS-TF-PowerCenter`)
5. **Click "Create Workspace"**

### 2️⃣ **Set Terraform Cloud Workspace Variables**
To authenticate Terraform Cloud with AWS via OIDC, configure the following **workspace variables**:

1. **Go to Terraform Cloud** → **Your Workspace** → **Variables**
2. **Create Two New Variables:**

| Key (Variable Name)         | Type    | Value                              | 
|-----------------------------|---------|------------------------------------|
| `TFC_AWS_PROVIDER_AUTH`      | **Environment** | `true`                           | 
| `TFC_AWS_RUN_ROLE_ARN`       | **Environment** | `arn:aws:iam::320812455017:role/Terraform-Workspaces-Centralized-IdentityProvider-IAM-Role` |

**🔹 Notes:**  
- These variables allow **Terraform Cloud to assume the IAM role** in AWS using OIDC authentication.


### 3️⃣ **Create a Directory to host files for the New Terraform Workspace**
Navigate to the appropriate account directory and create a new workspace directory:
#### **Using PowerShell**
```powershell
cd accounts\<aws_account_name>
mkdir <new_workspace>
cd <new_workspace>
```

#### **Using Command Prompt**
```cmd
cd accounts\<aws_account_name>
mkdir <new_workspace>
cd <new_workspace>
```

### 4️⃣ **Copy Template Files**
Copy all template files into the new workspace:
#### **Using PowerShell**
```powershell
Copy-Item -Path "..\..\..\.templates\*.tf" -Destination "." -Force
```

#### **Using Command Prompt**
```cmd
copy ..\..\..\.templates\*.tf .
```

### 5️⃣ **Customize Variables**
Modify variables.tf to set the required values:

* aws_region – The AWS region for deployment
*	environment – The deployment environment (e.g., dev, staging, prod)

### 6️⃣ **Set the Terraform Cloud Workspace**
The backend.tf file defines the Terraform Cloud backend.

Edit backend.tf and replace __REPLACE_ME__ with the correct Terraform Cloud workspace name.

**Example backend.tf (Before)**
```hcl
terraform {
  backend "remote" {
    hostname     = "app.terraform.io"
    organization = "DHCS"
    workspaces {
      name = "__REPLACE_ME__"
    }
  }
}
```

**Example backend.tf (After)**
```hcl
terraform {
  backend "remote" {
    hostname     = "app.terraform.io"
    organization = "DHCS"
    workspaces {
      name = "NIS-AWS-TF-PowerCenter"
    }
  }
}
```