# Uploading a File to AWS S3 Bucket Using Boto3
import boto3
s3 = boto3.resource('s3')
s3.Bucket('mypythons3buck3t').upload_file('/home/ec2-user/environment/python_boto3/s3_sample_file.html', 'sample.html')