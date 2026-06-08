# AWS Bill Processing System

## Project Overview

This project demonstrates a serverless bill processing workflow using AWS services.

When a bill image is uploaded to Amazon S3, AWS Lambda is triggered automatically. Lambda sends the image to Amazon Rekognition to extract text and identifies the total amount from the bill. The extracted information is then stored in Amazon DynamoDB.

## Architecture

S3 → Lambda → Rekognition → DynamoDB

## AWS Services Used

* Amazon S3
* AWS Lambda
* Amazon Rekognition
* Amazon DynamoDB
* Amazon CloudWatch
* IAM

## Workflow

1. Upload bill image to S3
2. S3 triggers Lambda
3. Lambda calls Rekognition DetectText
4. Total amount is extracted
5. Data is stored in DynamoDB

## Technologies

* Python
* Boto3
* AWS Cloud Services

## Learning Outcomes

* Event-driven architecture
* Serverless computing
* OCR using Amazon Rekognition
* DynamoDB integration
* IAM permissions management
* CloudWatch debugging
