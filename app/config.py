import os

AWS_SERVER_PUBLIC_KEY = os.getenv('AWS_SERVER_PUBLIC_KEY', 'default_public_key')
AWS_SERVER_SECRET_KEY = os.getenv('AWS_SERVER_SECRET_KEY', 'default_secret_key')
REGION_NAME = os.getenv('REGION_NAME', 'default_region')
bucket_name = os.getenv('BUCKET_NAME', 'default_bucket')
dynamodb_table_name = os.getenv('DYNAMODB_TABLE_NAME', 'default_table')