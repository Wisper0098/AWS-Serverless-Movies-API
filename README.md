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

- Create IAM User called MoviesAPI
- Save user's credentials into .csv file
- 
- Create S3 Bucket
- 
- Turn off blocking public access
- 
- In policy generator create 2 statemants for S3
  - First statement
    - Principal: `MoviesAPI` - IAM user
    - Actions: `ListBucket`
    - Resource: bucket arn adress

   - Second statement
    - Principal: `MoviesAPI` - IAM user
    - Actions: `Put/Get/Delete Object`
    - Resource: bucket arn adress + `/*`; Example: `arn:aws:s3:::mybucket/*`
  - Copy and paste it to policy of your bucket
- Create 2 folders in your bucket: `images`;`serverless-movies-api`;

- Create DynamoDB database
  - Press Create Table
    - Table name: `movies-info-db`
    - Partition key name: `title` (string)
    - Sort key: `releaseYear` (number)
    - Create table.
  - Set up permissions
    - Create policy for your IAM user with those permissions:
        "dynamodb:GetItem",
        "dynamodb:Scan",
        "dynamodb:Query",
        "dynamodb:DeleteItem",
        "dynamodb:PutItem",
        "dynamodb:UpdateItem"
    - Save policies

