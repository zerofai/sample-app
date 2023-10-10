import boto3
import random
import os
from flask import Flask, Response, jsonify

app = Flask(__name__)

bucket_url = os.getenv('S3_URL')
bucket_name = os.getenv('S3_BUCKET')
region_name = os.getenv('S3_REGION')
aws_access_key = os.getenv('aws_access_key')
aws_secret_key = os.getenv('aws_secret_key')

# Create MinIO client and ignore SSL certificate errors
s3_client = boto3.client(
    's3',
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    endpoint_url=bucket_url,
    verify=False
)

@app.route('/v1/image')
def get_random_image():
    # List objects in the bucket
    response = s3_client.list_objects(Bucket=bucket_name)
    
    # Get the list of object keys
    object_keys = [obj['Key'] for obj in response['Contents']]

    # Pick a random object key
    random_object_key = random.choice(object_keys)

    # Respose the image
    response = Response(s3_client.get_object(Bucket=bucket_name, Key=random_object_key)['Body'].read(), mimetype='image/jpeg')
    response.headers['Content-Disposition'] = 'inline'
  
    return response

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def fallback(path):
    return jsonify(message="Sorry, please use the right endpoint")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
