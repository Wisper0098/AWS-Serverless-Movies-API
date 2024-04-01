# AWS-Serverless-Movies-API

## Cloning repository
```
git clone https://github.com/Wisper0098/AWS-Serverless-Movies-API
cd AWS-Serverless-Movies-API/
```
## Creating virtual environment and installing required libraries
```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```
## AWS Setup
```
- Create IAM User called MoviesAPI
- Create S3 Bucket
- Turn off blocking public access
- In policy generator create 2 statemants for S3
  - First statement
    - Principal: `MoviesAPI` - IAM user
    - Actions: `ListBucket`
    - Resource: bucket arn adress
  - Second statement
    - Principal: `MoviesAPI` - IAM user
    - Actions: `Put/Get/Delete Object`
    - Resource: bucket arn adress + `/*`; Example: `arn:aws:s3:::mybucket/*`
```
