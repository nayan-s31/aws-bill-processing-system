import boto3
import re

rekognition = boto3.client('rekognition')
dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('BillDetails')

def lambda_handler(event, context):

    bucket = event['Records'][0]['s3']['bucket']['name']
    file_name = event['Records'][0]['s3']['object']['key']

    response = rekognition.detect_text(
        Image={
            'S3Object': {
                'Bucket': bucket,
                'Name': file_name
            }
        }
    )

    detected_text = []

    for item in response['TextDetections']:
        if item['Type'] == 'LINE':
            detected_text.append(item['DetectedText'])

    print("Detected Text:", detected_text)

    total = "Not Found"

    for i, line in enumerate(detected_text):

        if "total" in line.lower():

            numbers = re.findall(r'\d+\.?\d*', line)

            if numbers:
                total = numbers[-1]
                break

            if i + 1 < len(detected_text):
                next_line = detected_text[i + 1]

                numbers = re.findall(r'\d+\.?\d*', next_line)

                if numbers:
                    total = numbers[-1]
                    break

    print("Total:", total)

    table.put_item(
        Item={
            'BillName': file_name,
            'Total': total
        }
    )

    return {
        'statusCode': 200,
        'body': 'Success'
    }
