import boto3
import os

def create_dynamodb_table():
    # Define IAM access key and secret key
    aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
    aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')

    # Define the AWS region
    region_name = 'ap-south-1'   

    # Create a DynamoDB client
    dynamodb = boto3.client('dynamodb', 
                            aws_access_key_id=aws_access_key_id,
                            aws_secret_access_key=aws_secret_access_key,
                            region_name=region_name)

    # Define table schema
    table_name = 'Car'
    key_schema = [
        {
            'AttributeName': 'brand',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'model',
            'KeyType': 'RANGE'  #Sort key
        }
    ]
    attribute_definitions = [
        {
            'AttributeName': 'brand',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'model',
            'AttributeType': 'S'
        }

    ]
    provisioned_throughput = {
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }

    # Create DynamoDB table
    try:
        response = dynamodb.create_table(
            TableName=table_name,
            KeySchema=key_schema,
            AttributeDefinitions=attribute_definitions,
            ProvisionedThroughput=provisioned_throughput
        )
        print(f"DynamoDB table '{table_name}' created successfully.")
    except Exception as e:
        print(f"Failed to create DynamoDB table '{table_name}': {e}")

# Example usage
if __name__ == "__main__":
    create_dynamodb_table()
