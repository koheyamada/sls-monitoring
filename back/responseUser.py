import boto3
from boto3.dynamodb.conditions import Key, Attr
import json
import datetime

dynamodb = boto3.resource('dynamodb')
check_table = dynamodb.Table('urlcheck')
status_table = dynamodb.Table('urlcheck')

#def lambda_handler(event, context):
scan = check_table.scan()
jsonData = scan['Items']
list = len(jsonData)

for i in range(0,list):
  result = jsonData[i]
  print(result)

#return jsonData
