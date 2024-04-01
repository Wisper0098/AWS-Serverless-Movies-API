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
### IAM User and Credentials
1. Create an IAM User called `MoviesAPI`.
2. Save the user's credentials into a `.csv` file.

### S3 Bucket Setup
1. Create an S3 Bucket.
2. Turn off blocking public access.
3. In the policy generator, create 2 statements for S3:
- **First Statement:**
  - Principal: MoviesAPI IAM user
  - Actions: ListBucket
  - Resource: Bucket ARN address
- **Second Statement:**
  - Principal: MoviesAPI IAM user
  - Actions: Put/Get/Delete Object
  - Resource: Bucket ARN address + `/*` (e.g., `arn:aws:s3:::mybucket/*`)
4. Copy and paste the generated policy to your bucket's policy.

### S3 Bucket Structure
1. Create 2 folders in your bucket:
- `images`
- `serverless-movies-api`

### DynamoDB Setup
1. Create a DynamoDB database.
2. Press Create Table:
- Table name: `movies-info-db`
- Partition key name: `title` (string)
- Sort key: `releaseYear` (number)
3. Create the table.

### Permissions Setup
1. Create a policy for your IAM user with the following permissions:
- `dynamodb:GetItem`
- `dynamodb:Scan`
- `dynamodb:Query`
- `dynamodb:DeleteItem`
- `dynamodb:PutItem`
- `dynamodb:UpdateItem`
2. Save the policies.
