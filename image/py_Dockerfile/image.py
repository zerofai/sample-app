from flask import Flask, jsonify
import os
import boto3
import random

app = Flask(__name__)

@app.route('/v1/image', methods=['GET'])
def get_random_image():
    s3 = boto3.client('s3')
    bucket_name = os.getenv('IMAGE_S3')
    if not bucket_name:
        return jsonify(message="S3 bucket name not provided")

    response = s3.list_objects_v2(Bucket=bucket_name)
    objects = response['Contents']

    if len(objects) == 0:
        return jsonify(message="No images found in the S3 bucket")

    random_object = random.choice(objects)
    image_url = f"https://{bucket_name}.s3.amazonaws.com/{random_object['Key']}"

    return jsonify(image_url=image_url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
