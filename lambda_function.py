import json
import boto3

sns = boto3.client('sns')

def lambda_handler(event, context):
    body = json.loads(event['body'])
    message = body['message']
    notification_type = body['type']
    
    if notification_type == 'sms':
        sns_response = sns.publish(
            PhoneNumber='1234567890',  # Replace with your phone number
            Message=message
        )
    elif notification_type == 'email':
        sns_response = sns.publish(
            TopicArn='arn:aws:sns:region:account-id:MessageAppTopic',  # Replace with your topic ARN,
            Message=message,
            Subject="Notification"
        )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Notification sent successfully!')
    }
