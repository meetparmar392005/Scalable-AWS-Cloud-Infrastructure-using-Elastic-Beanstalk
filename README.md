# 🚀 Scalable AWS Cloud Infrastructure using Elastic Beanstalk

A production-grade, scalable cloud infrastructure built on AWS using Elastic Beanstalk with a custom VPC architecture, Auto Scaling, Load Balancing, and CloudWatch monitoring.

---

## 📌 Project Overview

This project demonstrates a real-world AWS cloud deployment of a Python Flask web application using industry-standard practices including network isolation, auto scaling, load balancing, monitoring, and CI/CD automation.

---

## 🏗️ Architecture

```
Internet
    │
    ▼
┌─────────────────────────────────────────┐
│              AWS VPC (10.0.0.0/16)      │
│                                         │
│  ┌──────────────────────────────────┐   │
│  │     Public Subnet (10.0.1.0/24)  │   │
│  │   ┌─────────┐   ┌─────────────┐ │   │
│  │   │   ELB   │   │ NAT Gateway │ │   │
│  │   └────┬────┘   └─────────────┘ │   │
│  └────────│─────────────────────────┘   │
│           │                             │
│  ┌────────│────────────────────────┐    │
│  │   Private Subnet (10.0.2.0/24) │    │
│  │   ┌────▼────┐   ┌───────────┐  │    │
│  │   │  EC2 #1 │   │  EC2 #2   │  │    │
│  │   │ (Flask) │   │  (Flask)  │  │    │
│  │   └─────────┘   └───────────┘  │    │
│  └─────────────────────────────────┘   │
└─────────────────────────────────────────┘
```

---

## ☁️ AWS Services Used

| Service | Purpose |
|---------|---------|
| **IAM** | Role-based access control for EC2 and Elastic Beanstalk |
| **VPC** | Custom network with public & private subnets |
| **EC2** | Compute instances running the Flask application |
| **ELB** | Application Load Balancer for traffic distribution |
| **Auto Scaling** | Automatically scales instances based on CPU utilization |
| **CloudWatch** | Monitoring, alarms, and log management |
| **S3** | Application storage and log retention |

---

## 📁 Project Structure

```
Scalable-AWS-Cloud-Infrastructure-using-Elastic-Beanstalk/
├── application.py              # Main Flask application
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore rules
├── README.md                   # Project documentation
├── .ebextensions/
│   └── python.config           # Elastic Beanstalk configuration
├── .github/
│   └── workflows/
│       └── deploy.yml          # CI/CD pipeline
└── screenshots/
    ├── iam.png
    ├── vpc.png
    ├── elastic-beanstalk.png
    ├── cloudwatch.png
    ├── s3.png
    └── ec2.png
```

---

## 🧱 Infrastructure Setup

### Step 1 — IAM Configuration
- Created `aws-elasticbeanstalk-ec2-role` for EC2 instances
- Created `aws-elasticbeanstalk-service-role` for Elastic Beanstalk service
- Attached required AWS managed policies for secure access

### Step 2 — Custom VPC Setup
- VPC CIDR: `10.0.0.0/16`
- **Public Subnet 1:** `10.0.1.0/24` (ap-south-1a) → ELB + NAT Gateway
- **Public Subnet 2:** `10.0.3.0/24` (ap-south-1b) → ELB (Multi-AZ)
- **Private Subnet:** `10.0.2.0/24` (ap-south-1b) → EC2 instances
- Internet Gateway attached to VPC
- NAT Gateway in public subnet for private EC2 internet access

### Step 3 — S3 Bucket
- Stores application deployment packages
- Stores application logs from CloudWatch
- Versioning enabled for deployment history

### Step 4 — Elastic Beanstalk
- Platform: Python 3.11 on 64-bit Amazon Linux 2023
- Environment type: Load Balanced
- EC2 instances deployed in **private subnet**
- Load Balancer deployed in **public subnets**

### Step 5 — Auto Scaling
- Minimum instances: 1
- Maximum instances: 2
- Scale out when CPU > 70%
- Scale in when CPU < 30%

### Step 6 — CloudWatch Monitoring
- Enhanced health reporting enabled
- CPU utilization alarm configured
- Log streaming enabled
- SNS email notifications configured

---

## 🔐 Security Design

```
Internet → ELB (Port 80)
                │
                ▼ (only ELB traffic allowed)
          EC2 in Private Subnet
                │
                ▼ (via NAT Gateway)
            Internet (outbound only)
```

- EC2 instances have **no public IP** — never directly exposed
- Security groups allow EC2 traffic **only from ELB**
- NAT Gateway handles outbound internet for private EC2s
- IAM roles follow **least privilege** principle

---

## 🔄 CI/CD Pipeline

GitHub Actions automatically deploys to Elastic Beanstalk on every push to `main`:

```
Push to main
     │
     ▼
GitHub Actions triggered
     │
     ▼
Zip application files
     │
     ▼
Deploy to Elastic Beanstalk ✅
```

---

## 🚀 Local Setup

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/Scalable-AWS-Cloud-Infrastructure-using-Elastic-Beanstalk.git

# Navigate to project
cd Scalable-AWS-Cloud-Infrastructure-using-Elastic-Beanstalk

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Mac/Linux
# venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Run locally
python application.py


## 📝 Resume Description

> Designed and deployed a scalable AWS cloud infrastructure using Elastic Beanstalk within a custom VPC architecture featuring public and private subnets across multiple Availability Zones. Implemented Auto Scaling, Application Load Balancing (ELB), and CloudWatch monitoring for high availability and performance optimization. Configured IAM roles, security groups, and NAT Gateway for secure access and network isolation. Integrated S3 for application storage and logging. Automated deployments using GitHub Actions CI/CD pipeline.

---

## 🎯 Key Concepts Demonstrated

- ✅ Public vs Private subnet design
- ✅ NAT Gateway for secure outbound access
- ✅ Multi-AZ deployment for high availability
- ✅ Auto Scaling based on CPU metrics
- ✅ Load Balancer health checks
- ✅ IAM role-based security 
- ✅ Infrastructure monitoring with CloudWatch
- ✅ CI/CD automation with GitHub Actions

---

