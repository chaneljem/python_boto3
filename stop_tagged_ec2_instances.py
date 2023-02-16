# Stop All EC2 Instances

import boto3

# Define variables to be used in the script
region = 'us-east-1'
ec2 = boto3.resource('ec2', region_name=region)

# Find the running instances with a specific tag
instances = ec2.instances.filter(
    Filters = [{'Name': 'instance-state-name', 'Values': ['running']},
    {'Name':'tag:Environment', 'Values':['Dev']}]
)

# Stop running instances with a for loop
for instance in instances:
    try:
        instance.stop()
        print(f'{instance} stopped')
    except:
        print(f'Error stopping {instance}')
