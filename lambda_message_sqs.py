# Send Message to SQS from Lambda
import json
import boto3
from datetime import datetime

def lambda_handler(event, context):
 
    now = datetime.now()
    current_time = now.strftime('%m/%d/%Y, %H:%M:%S')
    
    sqs = boto3.client('sqs')
    sqs.send_message(
        QueueUrl = 'https://sqs.us-east-1.amazonaws.com/972840112273/Test_Queue_ChanelJ',
        MessageBody = current_time)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Success')
    }
