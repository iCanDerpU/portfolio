# Personal Website/Portfolio

This is my personal website/portfolio hosted at [vkaramoutas.xyz](https://vkaramoutas.xyz). The website will be used to showcase my projects, skills, and experiences. It is built using AWS services and infrastructure as code principles.

## Overview

The project utilizes various AWS services to host and manage the website. Key services include:

- **EC2**: Used for hosting WordPress and MariaDB.
  
- **CloudFront**: Content Delivery Network (CDN) for faster content delivery and improved website performance.
  
- **Route 53**: Domain Name System (DNS) service for routing traffic to the website.
  
- **API Gateway**: Used for creating the API to handle contact form submissions.
  
- **Lambda**: Executes the serverless function to process contact form submissions.
  
- **Simple Email Service (SES)**: Sends email notifications for contact form submissions.

## Infrastructure as Code

The infrastructure is defined and managed using CloudFormation templates. Here are the YAML file descriptions:

1. `ec2-cloudfront.yaml`: Defines the infrastructure for EC2 instance hosting WordPress and MariaDB, and sets up CloudFront for CDN.
   
2. `mailer.yaml`: Sets up API Gateway, Lambda function, and SES for handling contact form submissions.
   
3. `main.yaml`: Contains the definition of the two stacks, including the resources defined in `ec2-cloudfront.yaml` and `mailer.yaml`.
   
4. `.github/workflows/Deploy-Portfolio-Website.yaml`: CI/CD workflow for automatically deploying the project on AWS whenever changes are committed to the repository.

## Deployment

To deploy the project locally or on AWS, follow these steps:

1. Clone the repository:
git clone https://github.com/iCanDerpU/portfolio.git

2. Navigate to the project directory:
cd portfolio

3. Modify the CloudFormation templates or any other files as needed.

4. Commit your changes:
git add .
git commit -m "Your commit message"

5. Push changes to the repository:
git push origin master

6. The CI/CD pipeline will automatically trigger a deployment on AWS.

## Local Setup

For local development and testing:

1. Set up a local development environment with WordPress and MariaDB.

2. Configure API Gateway, Lambda, and SES locally using AWS SAM (Serverless Application Model) or equivalent tools.
