import json
import boto3
import os

USER = os.environ.get("USER_ENV", "dev")


def post_data(payload):
    data = json.loads(payload).get("greetPerson")
    dynamodb_client = boto3.client('dynamodb')
    dynamodb_client.put_item(TableName=f'{USER}-UserData', Item={'id': {'S': data}})
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": f"hello {data}",
        }),
    }


def lambda_handler(event, context):
    print(event)
    return post_data(event.get("body"))


if __name__ == '__main__':
    post_data("{\n  \"record\": \"iiiiiii\"\n}")
