# CI/CD Pipeline with GitHub Actions

Automated deployment pipeline that deploys a static website to AWS S3 on every push to the main branch.

## 🚀 Live Demo

**Website:** http://my-github-actions-site.s3-website-us-east-1.amazonaws.com/

The site automatically updates when code is pushed to GitHub!

## 🛠️ Technologies

- **GitHub Actions** - CI/CD automation
- **AWS S3** - Static website hosting
- **AWS IAM** - Secure credential management
- **YAML** - Workflow configuration

## 📋 What This Demonstrates

### CI/CD Pipeline
- Automated deployment on git push
- GitHub Actions workflow configuration
- AWS integration with GitHub secrets

### AWS Services
- S3 static website hosting
- S3 bucket policy configuration
- IAM user and access key management

### DevOps Best Practices
- Infrastructure as Code workflows
- Secrets management
- Automated deployment pipelines

## 🔄 How It Works

1. **Developer pushes code** to main branch
2. **GitHub Actions triggered** automatically
3. **Workflow runs** on GitHub-hosted runner
4. **AWS credentials configured** from GitHub secrets
5. **Files synced to S3** using AWS CLI
6. **Website updated** instantly

## 📁 Project Structure
```
.
├── .github/
│   └── workflows/
│       └── deploy-to-s3.yml    # CI/CD workflow
├── index.html                   # Website content
└── README.md                    # This file
```

## ⚙️ Workflow Configuration

The deployment workflow (`.github/workflows/deploy-to-s3.yml`) includes:

- **Trigger:** Runs on push to main branch
- **Checkout:** Gets latest code from repository
- **AWS Authentication:** Uses GitHub secrets for secure credential access
- **Deploy:** Syncs files to S3 bucket
- **Cleanup:** Removes files deleted from repository

## 🔐 Security

- AWS credentials stored as GitHub secrets (never in code)
- S3 bucket configured for public read (website hosting)
- IAM user has minimal required permissions

## 📚 What I Learned

- Setting up GitHub Actions workflows
- Configuring AWS S3 for static website hosting
- Managing secrets in GitHub
- Implementing automated deployment pipelines
- AWS CLI commands for S3 sync
- YAML syntax for workflow configuration

## 🎯 Future Improvements

- [ ] Add Terraform to manage S3 infrastructure
- [ ] Implement CloudFront CDN for faster delivery
- [ ] Add automated testing before deployment
- [ ] Set up staging environment
- [ ] Add deployment notifications

## 🚀 How to Use This Project

### Prerequisites
- AWS Account
- GitHub Account
- AWS CLI installed (optional, for local testing)

### Setup Steps

1. **Fork this repository**

2. **Create S3 bucket** for static website hosting

3. **Create IAM user** with S3 permissions

4. **Add GitHub Secrets:**
   - `AWS_ACCESS_KEY_ID`
   - `AWS_SECRET_ACCESS_KEY`

5. **Update workflow** with your bucket name

6. **Push to main branch** → automatic deployment!

## 📝 Notes

This project demonstrates a complete CI/CD workflow for static site deployment. While simple, it showcases key DevOps concepts: automation, cloud integration, and continuous deployment.

---

**Built as part of my DevOps learning journey** 🚀

**Contact:** semensabov42@gmail.com
