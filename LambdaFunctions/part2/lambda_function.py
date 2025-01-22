import json
import base64
import boto3
import os
import uuid
from botocore.exceptions import ClientError

s3 = boto3.client('s3')

def lambda_handler(event, context):
    print("Environment Variables:", os.environ)
    bucket_name = os.environ.get('S3_BUCKET_NAME', 'Not Set')
    print("Bucket Name:", bucket_name)
    
    try:
        bucket_name = os.environ['S3_BUCKET_NAME']
        
        file_content = event.get('file_content')  
        file_name = event.get('file_name', f"{uuid.uuid4()}.pdf")  
        
        file_data = base64.b64decode(file_content)
        
        s3.put_object(
            Bucket=bucket_name,
            Key=file_name,
            Body=file_data,
            ContentType='application/pdf' 
        )
        
        file_url = f"https://{bucket_name}.s3.amazonaws.com/{file_name}"
        
        return {
            'statusCode': 200,
            'body': {
                'message': 'File uploaded successfully',
                'file_url': file_url
            }
        }
    
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': {
                'message': 'Error uploading file',
                'error': str(e)
            }
        }
    except Exception as e:
        return {
            'statusCode': 400,
            'body': {
                'message': 'Invalid request',
                'error': str(e)
            }
        }
