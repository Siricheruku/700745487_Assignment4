import boto3
import configparser

# Reading the config file
config = configparser.ConfigParser()
config.read('config.ini')

# Initialize the SNS client
sns_client = boto3.client('sns')

# Creati the SNS topic
topic_name = config['SNS']['topic_name']
topic_response = sns_client.create_topic(Name=topic_name)

# Get the topic ARN from the response
topic_arn = topic_response['TopicArn']

# Subscribe an email address to the topic
email_address = config['SNS']['email_address']
subscribe_response = sns_client.subscribe(
    TopicArn=topic_arn,
    Protocol='email',
    Endpoint=email_address
)

# Print the subscription ARN from the response
subscription_arn = subscribe_response['SubscriptionArn']
print(f'Successfully subscribed {email_address} to topic {topic_arn} with subscription ARN {subscription_arn}')


