import boto3
from boto3.dynamodb.conditions import Key, Attr
import json

# DynamoDB
dynamodb = boto3.resource('dynamodb')
_table_ = dynamodb.Table('S-Status')
_url_ = "https://www.hengjiu.jp"

def lambda_handler(event, context):
  res = _table_.query(
    KeyConditionExpression=Key('url').eq(_url_),
    Limit=10
  )

  print(res)

