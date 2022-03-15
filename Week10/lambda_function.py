import json
import urllib.parse
import boto3

REGION = "us-east-1"
MAX_LABELS = 10
MIN_CONFIDENCE = 80

def lambda_handler(event, context):
    print("Hello from YOUR_NAME_GOES_HERE")
    #print(event)
    
    rekognition_client = boto3.client('rekognition', REGION)
    
    # 1) Use the below 2 lines for internal testing
    # s3_bucket = "is434-supreme"
    # s3_object = "justin1.jpg"
    
    # 2) Use the below 2 lines for production
    s3_bucket = event['Records'][0]['s3']['bucket']['name']
    s3_object = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    print("S3 Bucket: ", s3_bucket)
    print("S3 Object: ", s3_object)
    
    response = rekognition_client.detect_labels(
      Image = {
          "S3Object": {
            "Bucket": s3_bucket,
            "Name": s3_object,
          }
		},
		MaxLabels = MAX_LABELS,
		MinConfidence = MIN_CONFIDENCE
	)
	
	# This will log 'labels' part of the response to CloudWatch logs
    print(response['Labels'])
    
    # Let's write 'labels' part of the response to S3 bucket
    # For input "justin1.jpg", the output file will be "justin1.jpg.json"
    # Verify in S3 bucket
    s3_resource = boto3.resource('s3', REGION)
    s3_output_object = s3_resource.Object(s3_bucket, s3_object + ".json")
    s3_output_object.put(
        Body=(
            bytes(
                json.dumps(response['Labels']).encode('UTF-8')
            )
        )
    )
    
    return response['Labels']
   