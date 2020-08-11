#!/usr/bin/env python
'''
Echo service as a Lambda function
'''

import json
import boto3
region = 'us-west-2'
instances = ['i-04daed54a56ba8dc9']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    # TODO implement
    ec2.stop_instances(InstanceIds=instances)
    print('stopped your instances: ' + str(instances))
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }