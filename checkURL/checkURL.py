import requests
import boto3
from boto3.dynamodb.conditions import Key, Attr
import logging
import json
import datetime

dynamodb = boto3.resource('dynamodb')
check_table    = dynamodb.Table('urlcheck')
status_table    = dynamodb.Table('urlstatus')

def lambda_handler(event, context):
  # tableをスキャン
  scan = check_table.scan()

  jsonData = scan['Items']  # スキャン結果をJsonデータへ変換
  list = len(jsonData)  # 配列数を取得

  for i in range(0,list):
    try:
      url = jsonData[i]['url']
      res = requests.get(jsonData[i]['url'], timeout=3)
      user = jsonData[i]['user']
      date = str(datetime.datetime.now())
    except Exception as e:
      logging.info(e.response['Error']['Message'])
    else:
      result = {
        'url':url,
        'date':date,
        'status':res.status_code,
        'user':user
    }
      print(result)
      res = status_table.put_item( Item = result )

  return res
