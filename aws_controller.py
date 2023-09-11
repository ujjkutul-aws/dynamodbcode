import boto3

dynamodbclient = boto3.client('dynamodb')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('products')
def get_items():
    return dynamodbclient.scan(TableName='products')

def create_product(product_id,product_name,product_qty,store_location):

    response = table.put_item(Item={
        'product_id': product_id,
        'product_name': product_name,
        'product_qty': product_qty,
        'store_location': store_location,
    })
    return response

def delete_product(product_id,product_name):

    table.delete_item(
        Key={
        'product_id': product_id,
        'product_name': product_name
        },
    )

def update_product(product_id,product_name,product_qty,store_location):
    table.update_item(
        Key={
        'product_id': product_id,
        'product_name': product_name
        },
        UpdateExpression="SET #ts = :val1, #ts2 = :val2",
        ExpressionAttributeValues={
            ':val1': store_location,
            ':val2': product_qty
        },
        ExpressionAttributeNames={
            "#ts": "store_location",
            '#ts2': "product_qty"
        }
    )