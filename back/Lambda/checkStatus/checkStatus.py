import requests
import boto3
from boto3.dynamodb.conditions import Key, Attr
import logging
import json
import datetime

dynamodb = boto3.resource('dynamodb')
check_table = dynamodb.Table('urlcheck')
status_table = dynamodb.Table('urlstatus')
history_table = dynamodb.Table('checkhistory')

def lambda_handler(event, context):
  scan = check_table.scan()
  jsonData = scan['Items']
  list = len(jsonData)

  for i in range(0,list):
    try:
      url = jsonData[i]['url']
      gens = jsonData[i]['gens']
      user = jsonData[i]['user']

      res = status_table.query(
        KeyConditionExpression = Key('url').eq(url),
        FilterExpression=Attr('user').eq(user),
        Limit = int(gens)
      )

      num = 0
      for i in res['Items']:
        if i['status'] == 200:
          num += 1

      if num == gens:
        status = 'healthy'
      else:
        status = 'unhealthy'

      date = str(datetime.datetime.now())
      result = {
        'url':url,
        'date':date,
        'gens':gens,
        'user':user,
        'status':status
      }
      print(result)
      res = history_table.put_item( Item = result )
    except Exception as e:
      print(e)

