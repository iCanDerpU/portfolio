import boto3

def lambda_handler(event, context):
    # Extracting data from the event
    name = event['name']
    email = event['email']
    content = event['content']
    
    # Constructing the email message
    subject = 'New contact message from {}'.format(name)
    body = 'Name: {}\nEmail: {}\nContent: {}'.format(name, email, content)
    
    # Sending email using Amazon SES
    sender_email = 'Contact Derp <contact@vkaramoutas.xyz>'
    recipient_email = 'vkaramoutas@gmail.com'
    
    ses_client = boto3.client('ses')
    
    try:
        ses_client.send_email(
            Source=sender_email,
            Destination={
                'ToAddresses': [recipient_email]
            },
            Message={
                'Subject': {'Data': subject},
                'Body': {'Text': {'Data': body}}
            }
        )
        return {
            'statusCode': 200,
            'body': 'Email sent successfully'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }
