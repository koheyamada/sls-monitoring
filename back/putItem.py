import boto3
from boto3.dynamodb.conditions import Key, Attr
import json
import datetime
import sys

args = sys.argv

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('S-Users')

#def lambda_handler(event, context):
table.put_item(
  Item = {
    "name": args[1],
    "slack": args[2]
  }
)

#return jsonData
