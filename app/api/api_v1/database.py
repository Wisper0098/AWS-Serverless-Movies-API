from boto3 import Session

import requests
import io
import csv
import os

from ...config import *

session = Session(aws_access_key_id=AWS_SERVER_PUBLIC_KEY, aws_secret_access_key=AWS_SERVER_SECRET_KEY, region_name=REGION_NAME)

s3 = session.client('s3') # S3 client

def get_image_binary(imgurl):
    return io.BytesIO(requests.get(imgurl).content)


def upload_image_to_s3(binary, filename):
    s3.upload_fileobj(binary, bucket_name, f'images/{filename}')
    return f"https://{bucket_name}.s3.amazonaws.com/images/{filename}"
    
# DynamoDB Stuff

dynamodb = session.client('dynamodb')


def insert_items_to_dynamodb(itemdict: dict):
    print('Inserting item to database...')

    response = dynamodb.put_item(
        TableName=dynamodb_table_name,
        Item={
            'title':{ 'S': itemdict['title'] },
            'releaseYear':{ 'N': str(itemdict['releaseYear']) },
            'genre':{ 'S': itemdict['genre'] },
            'coverUrl':{ 'S': itemdict['coverUrl'] }
        }
    )
    print(f'Insert response {response}')


def upload_items_from_csv_to_dynamodb(count):

    current_directory = os.path.dirname(os.path.realpath(__file__))
    parent_directory_api_v1 = os.path.abspath(os.path.join(current_directory, os.pardir))
    parent_directory_app = os.path.abspath(os.path.join(parent_directory_api_v1, os.pardir))
    csv_file_path = os.path.join(parent_directory_app, 'movies.csv')
    
    if count <= 100:
        with open(csv_file_path) as cvf:
            reader = csv.DictReader(cvf)
            i = 0
            for row in reader:
                if i < count:
                    #print(row)
                    img_link = row['Poster_Link']
                    filepath = upload_image_to_s3(get_image_binary(img_link), row['Series_Title'] + '.jpg') # Uploading image to S3 bucket and getting image location
                    insert_items_to_dynamodb({'title':row['Series_Title'], 'releaseYear':row['Released_Year'], 'genre':row['Genre'], 'coverUrl':filepath})
                    i += 1
                else:
                    break
            cvf.close()
    else:
        print("No more than 100 items are allowed")


def initiate_db():
    response = dynamodb.scan(
        TableName=dynamodb_table_name,
        Select='COUNT'
    )
    if response['Count'] == 0:
        print("Database is empty. Adding 100 new items...")
        upload_items_from_csv_to_dynamodb(100)


def get_all_movies():
    items = []
    last_evaluated_key = None

    while True:
        if last_evaluated_key:
            response = dynamodb.scan(
                TableName=dynamodb_table_name,
                ExclusiveStartKey=last_evaluated_key
            )
        else:
            response = dynamodb.scan(
                TableName=dynamodb_table_name
            )

        items.extend(response['Items'])

        last_evaluated_key = response.get('LastEvaluatedKey')
        if not last_evaluated_key:
            break
    
    return items


def get_movie_by_year(year):
    result = []
    try:
        # Perform the scan operation
        response = dynamodb.scan(
            TableName=dynamodb_table_name,
            FilterExpression='releaseYear = :year',
            ExpressionAttributeValues={':year': {'N': str(year)}}
        )

        # Check if any items are returned
        items = response.get('Items', [])
        if items:
            for item in items:
                result.append({
                    'title': item['title']['S'],
                    'releaseYear': str(item['releaseYear']['N']),
                    'genre': item['genre']['S'],
                    'coverUrl': item['coverUrl']['S']
                })
            return result
        else:
            print("No items found for release year:", year)
            return None
    except Exception as e:
        print("Error:", e)
        return None


def get_movie_by_name(name):
    result = []
    try:
        # Perform the scan operation
        response = dynamodb.scan(
            TableName=dynamodb_table_name,
            FilterExpression='title = :name',
            ExpressionAttributeValues={':name': {'S': str(name)}}
        )

        # Check if any items are returned
        items = response.get('Items', [])
        if items:
            for item in items:
                result.append({
                    'title': item['title']['S'],
                    'releaseYear': str(item['releaseYear']['N']),
                    'genre': item['genre']['S'],
                    'coverUrl': item['coverUrl']['S']
                })
            return result
        else:
            print("No items found for release year:", year)
            return None
    except Exception as e:
        print("Error:", e)
        return None



