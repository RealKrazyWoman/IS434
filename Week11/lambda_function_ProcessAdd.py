import json
import boto3
import datetime

def lambda_handler(message, context):
    # 1. Log input message
    print("Received message from Step Functions:")
    print(message)
    
    # 2. Perform Operation (Add)
    num1 = message['num1']
    num2 = message['num2']
    result = num1 + num2
    
    # 3. Construct response object
    response = {}
    response['Timestamp'] = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    response['Name'] = message['Name']
    response['Type'] = message['Type']
    response['Result'] = result
    
    return response