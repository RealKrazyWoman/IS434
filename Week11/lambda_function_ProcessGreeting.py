import json
import boto3
import datetime

def lambda_handler(message, context):
    # 1. Log input message
    print("Received message from Step Functions:")
    print(message)
    
    # 2. Publish to SNS Topic
    sns_client = boto3.client('sns')

    ##########################
    # UPDATE THE BELOW LINE
    ##########################
    sns_topic_arn = 'YOUR_OWN_TelegramNotifier_SNS_TOPIC_ARN'

    response = sns_client.publish(
        TargetArn = sns_topic_arn,
        Message = json.dumps(
            {
                'default': json.dumps(message)
            }
        ),
        Subject = 'IS434 Step Functions Greeting',
        MessageStructure = 'json'
    )