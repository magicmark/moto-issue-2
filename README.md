# moto-issue-2

### Repro instructions 

```bash
$ git clone https://github.com/magicmark/moto-issue-demo-2.git
$ cd moto-issue-2
$ poetry install
$ poetry run pytest -vvv
```

### Output

```
=========================================================================== test session starts ============================================================================
platform linux -- Python 3.8.13, pytest-7.4.3, pluggy-1.3.0
rootdir: /nail/home/markl/pg/moto-issue-demo
collected 1 item                                                                                                                                                           

tests/yikes_test.py F                                                                                                                                                [100%]

================================================================================= FAILURES =================================================================================
________________________________________________________________________________ test_yikes ________________________________________________________________________________

dynamodb = dynamodb.ServiceResource()

    def test_yikes(dynamodb):
        dynamodb.Table("meal-orders").put_item(
            Item={
                "customer": "mark",
                "mealtime": "breakfast",
            }
        )
    
>       assert 'Item' not in dynamodb.Table("meal-orders").get_item(
            Key={
                "customer": "mark",
                "mealtime": "lunch",
            }
        )
E       AssertionError: assert 'Item' not in {'Item': {'customer': 'mark', 'mealtime': 'breakfast'}, 'ResponseMetadata': {'HTTPHeaders': {'date': 'Mon, 30 Oct 2023...eit'}, 'HTTPStatusCode': 200, 'RequestId': '77j7t488VZMp0LEtqw77cGXhTRPnS9W5Eu98ryU2drVYruC7veit', 'RetryAttempts': 0}}
E        +  where {'Item': {'customer': 'mark', 'mealtime': 'breakfast'}, 'ResponseMetadata': {'HTTPHeaders': {'date': 'Mon, 30 Oct 2023...eit'}, 'HTTPStatusCode': 200, 'RequestId': '77j7t488VZMp0LEtqw77cGXhTRPnS9W5Eu98ryU2drVYruC7veit', 'RetryAttempts': 0}} = <bound method ResourceFactory._create_action.<locals>.do_action of dynamodb.Table(name='meal-orders')>(Key={'customer': 'mark', 'mealtime': 'lunch'})
E        +    where <bound method ResourceFactory._create_action.<locals>.do_action of dynamodb.Table(name='meal-orders')> = dynamodb.Table(name='meal-orders').get_item
E        +      where dynamodb.Table(name='meal-orders') = <bound method ResourceFactory._create_class_partial.<locals>.create_resource of dynamodb.ServiceResource()>('meal-orders')
E        +        where <bound method ResourceFactory._create_class_partial.<locals>.create_resource of dynamodb.ServiceResource()> = dynamodb.ServiceResource().Table

tests/yikes_test.py:32: AssertionError
========================================================================= short test summary info ==========================================================================
FAILED tests/yikes_test.py::test_yikes - AssertionError: assert 'Item' not in {'Item': {'customer': 'mark', 'mealtime': 'breakfast'}, 'ResponseMetadata': {'HTTPHeaders': {'date': 'Mon, 30 Oct 2023...eit'}, 'H...
```
