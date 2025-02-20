# Contributing to Terraform Repository

Thank you for contributing to this repository! To ensure high-quality changes and maintain stability, we enforce a **Pull Request (PR) workflow** where all changes must be reviewed and approved before merging into the `main` branch.

---

## 🏗️ **Creating a new works**



## 🔄 **Branching Strategy**
- The **`main` branch is protected** and **direct commits are not allowed**.
- Contributors should **create branches** from `main` and submit a **Pull Request (PR)** for review.
- Use the following branch naming conventions:
  - **Feature Branches**: `feature/<short-description>`
  - **Bug Fixes**: `fix/<short-description>`
  - **Hotfixes** (urgent fixes in `main`): `hotfix/<short-description>`
  - **Documentation Updates**: `docs/<short-description>`

---

## 🛠️ **Workflow for Making Changes**
### 1️⃣ **Clone the Repository** 
```sh
git clone https://github.com/dhcs-ets/nis-aws-terraform.git
cd nis-aws-terraform
```

### 2️⃣ **Create a New Branch**
 ```sh
  git checkout -b feature/my-new-feature
 ```

  Replace feature/my-new-feature with a meaningful branch name.

### 3️⃣ **Make Your Changes**

  * If you are creating a new Terraform workspace, first follow the directions in [.terraform/README.md](.terraform/README.md).

  * Modify Terraform files.
  * Ensure changes do not break existing functionality.
  * Run terraform fmt to format the code.

### 4️⃣ **Commit Your Changes**
```sh
  git add .
  git commit -m "Added a new feature for XYZ"
```

### 5️⃣ **Push Your Branch to GitHub**
```sh
  git push origin feature/my-new-feature
```

### 6️⃣ **Open a Pull Request**

  1. Go to GitHub → Repository → Pull Requests.
  
  1. Click “New Pull Request”.
	
  3.	Select main as the base branch and your branch as the compare branch.
	
  4.	Fill in the PR title and description.
	
  5.	Request a reviewer.

### 7️⃣ **Automated GitHub Action Checks**
After opening a Pull Request, GitHub Actions will run the following checks **automatically** to validate your changes:

| Check | Description |
|-------|------------|
| **Terraform Format (`fmt`)** | Ensures all Terraform files are formatted correctly (`terraform fmt`). |
| **Terraform Linter (`tflint`)** | Identifies style and best practice violations (`tflint`). |
| **Terraform Security Scan (`tfsec`)** | Scans Terraform configurations for security vulnerabilities (`tfsec`). |
| **Terraform Plan (`plan`)** | Runs `terraform plan` to preview changes before applying them. |

If any of these checks **fail**, you must fix the errors before a reviewer will review or you can merge.

 🔍 Running These Checks Locally
Before pushing, you can run these checks locally:

```sh
cd <workspace_path>
terraform fmt -recursive
tflint --recursive
tfsec .
terraform plan
```

🛑 If Checks Fail:
	
1.	Fix the reported issues.
2.	Run the checks again locally.
3.	Commit and push the updated changes:
4. Once all checks pass, the Pull Request will be ready for review.

### 8️⃣ **Code Review Process**

* A team member will review your PR for:
	
* Correctness
    
* Security best practices
    
* Code quality and style
	
1. If changes are requested, update your branch:

```sh
git add .
git commit --amend --no-edit
git push --force
```

### 9️⃣ **Merge the PR**

  * Once approved, merge the PR.
	
  * The PR must pass all automated checks (GitHub Actions, Terraform validation).
	
  * The PR should follow the “Squash and Merge” policy.


---

🛑 Protected Branches

The main branch has the following protections:

✅ Direct pushes are blocked – All changes must go through a PR.

✅ At least 1 approval is required before merging.

✅ Status checks (Terraform validation, linting) must pass before merging.

✅ Best Practices

* Write clear commit messages describing the changes.
* Test Terraform changes using:
```sh
  terraform plan
```
* Format code before pushing:
```sh
  terraform fmt
```  
* Use descriptive PR titles and detailed descriptions.
* Do not commit sensitive information (secrets, AWS credentials, API keys).