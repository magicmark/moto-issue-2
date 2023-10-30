import pytest
import boto3
import moto

@pytest.fixture(autouse=True, scope="function")
def dynamodb():
    with moto.mock_dynamodb():
        dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
        dynamodb.create_table(
            TableName="meal-orders",
            KeySchema=[
                {"AttributeName": "customer", "KeyType": "HASH"},
                {"AttributeName": "mealtime", "KeyType": "SORT"},
            ],
            AttributeDefinitions=[
                {"AttributeName": "customer", "AttributeType": "S"},
                {"AttributeName": "mealtime", "AttributeType": "S"},
            ],
            ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
        )
        yield dynamodb


def test_yikes(dynamodb):
    dynamodb.Table("meal-orders").put_item(
        Item={
            "customer": "mark",
            "mealtime": "breakfast",
        }
    )

    assert 'Item' not in dynamodb.Table("meal-orders").get_item(
        Key={
            "customer": "mark",
            "mealtime": "lunch",
        }
    )