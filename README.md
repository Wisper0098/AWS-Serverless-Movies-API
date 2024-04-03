# AWS-Serverless-Movies-API

The Serverless Movies API is a FastAPI-based web service designed to interact with a serverless movie database hosted on AWS DynamoDB. This API provides several endpoints:

- **Get All Movies:** Retrieve information about all movies stored in the database. If the database is empty, it automatically initializes it by adding 100 items from a CSV file (`movies.csv`).
- **Get Movies by Year:** Retrieve movies released in a specific year.
- **Get Movie by Name:** Retrieve details about a movie based on its name.

The API leverages FastAPI's capabilities to handle HTTP requests efficiently and responds with JSON data containing movie information such as title, release year, genre, and cover URL.

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

### Environment variables for test
1. Fill `env_vars.bashrc` with your data
2. Run `source env_vars.bashrc` 

### Test API
1. Ensure you activated virtual environment and installed required libraries
2. Run application using command: `uvicorn app.main:app --reload`
3. Go to the `localhost:8000/docs` and check out all API requests
4. If everything is working, stop your application and delete `env_vars.bashrc`

### Zip up site-packages and app folders
1. Change directory: `cd venv/lib/python3.10/site-packages/`
2. Zip libraries using this command: `zip -r9 ../../../../function.zip .`
3. Go back to project root directory and add `app` folder into your `function.zip` using this command:
   - `zip -g ./function.zip app`

### Upload your function.zip to S3 Bucket
1. Go to `serverless-movies-api` folder in your S3 Bucket
2. Upload there your `function.zip` file
3. Copy the Object URL of this file

### Create Lambda function in AWS
1. Name: `MoviesAPI-lambda`
2. Runtime: `Python 3.10`
3. Leave everything else by default, and create function

### Lambda setup
1. Got to the Code Source and click on the `Upload from` button
2. Choose Amazon S3 location and paste link to your `function.zip`
3. After that, go to Runtime settings and change default handler to `app.main.handler`
4. Go to the Configuration and choose Environment variables
5. Add there these variables: `AWS_SERVER_PUBLIC_KEY; AWS_SERVER_SECRET_KEY; BUCKET_NAME; DYNAMODB_TABLE_NAME; REGION_NAME`

### Test Lambda function
1. Create new test event
2. Template: `apigateway-aws-proxy`
3. Change path to `/api/v1/`
4. And change HTTP method to `"GET"`
5. Run test

### Create Function URL
1. Go to Configuration and choose Function URL
2. Click Create function URL
3. In Auth type choose `NONE` and click Save
4. Copy function URL and add `/docs` to check out available requests
5. Example `https://$AWS_ID.lambda-url.$AWS_REGION.on.aws/docs`
6. Congragulations! 
