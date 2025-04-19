import json
import boto3
import qrcode
from io import BytesIO
import uuid

# Initialize S3 client
s3 = boto3.client('s3')

# Your bucket name (no typo, no special character)
bucket_name = 'qr-code-generator123456'

def lambda_handler(event, context):
    try:
        # Parse input
        body = json.loads(event['body'])
        data = body.get('text')

        if not data:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'No input provided'})
            }

        # Generate QR code
        img = qrcode.make(data)
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)

        # Upload to S3
        file_name = f"qr_{uuid.uuid4()}.png"
        s3.put_object(
            Bucket=bucket_name,
            Key=file_name,
            Body=buffer,
            ContentType='image/png'
        )

        # Construct public S3 URL (assuming bucket policy allows public access)
        url = f"https://{bucket_name}.s3.amazonaws.com/{file_name}"

        # Return the URL
        return {
            'statusCode': 200,
            'headers': { 'Content-Type': 'application/json' },
            'body': json.dumps({'url': url})
        }

    except Exception as e:
        # If anything goes wrong, return error
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
