# Create SQS Queue
import boto3

sqs = boto3.resource('sqs', region_name='us-east-1')

# Create the Queue
queue = sqs.create_queue(QueueName='Test_Queue_ChanelJ', Attributes={'DelaySeconds': '5'})
print(queue.url)