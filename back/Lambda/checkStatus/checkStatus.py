# checkURL.py
# Get URLs from DynamoDB.
# Check the status of URL.
# Write the status to DynamoDB.

import requests
import boto3
from boto3.dynamodb.conditions import Key, Attr
import logging
import json
import datetime

# DynamoDB
_dynamodb_ = boto3.resource('dynamodb')
_starget_ = _dynamodb_.Table('S-Target')
_sstatus_ = _dynamodb_.Table('S-Status')

def lambda_handler(event, context):
# tableをスキャン
  _scan_ = _starget_.scan()

  _stjson_ = _scan_['Items']  # スキャン結果をJsonデータへ変換
  _list_ = len(_stjson_)  # 配列数を取得

  for i in range(0,_list_):
    try:
      _url_ = "https://" + _stjson_[i]['domain']
      _req_ = requests.get(_url_, timeout=3)
      _name_ = _stjson_[i]['name']
      _date_ = str(datetime.datetime.now())
    except Exception as e:
      logging.info(e.response['Error']['Message'])
    else:
      _result_ = {
        'url':_url_,
        'date':_date_,
        'scode':_req_.status_code,
        'name':_name_
      }
      print(_result_)
      _res_ = _sstatus_.put_item( Item = _result_ )

  return _res_

