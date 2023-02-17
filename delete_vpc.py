# Delete VPC
import boto3
ec2 = boto3.resource('ec2')
ec2client = ec2.meta.client
ec2client.delete_vpc(VpcId = 'vpc-003f338b009dda24d')