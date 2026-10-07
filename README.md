# Cloud Infrastructure & CI/CD Automation Platform

A beginner-friendly Cloud & DevOps project that demonstrates containerization, CI/CD automation, AWS cloud deployment, Infrastructure as Code, reverse proxy configuration, and cloud monitoring.

## 🚀 Project Overview

This project demonstrates the deployment of a Python Flask application on an AWS EC2 Linux server using Docker.

The application is containerized with Docker and deployed automatically through a GitHub Actions CI/CD pipeline.

Nginx is configured as a reverse proxy, Terraform is used for Infrastructure as Code configuration, and AWS CloudWatch is used for EC2 monitoring.

## 🏗️ Architecture

```text
Developer
    │
    ▼
 GitHub Repository
    │
    ▼
GitHub Actions
    │
    ├── Build Docker Image
    │
    └── Deploy to AWS EC2
                │
                ▼
           Docker Container
                │
                ▼
          Flask Application
                │
                ▲
             Nginx
                │
                ▼
          Internet / Users

Terraform → Infrastructure Configuration

CloudWatch → EC2 Monitoring# cloud-infrastructure-cicd
Cloud Infrastructure &amp; CI/CD Automation Platform using AWS, Docker, Terraform and GitHub Actions
```
