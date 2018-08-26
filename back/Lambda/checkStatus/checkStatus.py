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
dynamodb = boto3.resource('dynamodb')
_starget_ = dynamodb.Table('S-Target')
_sstatus_ = dynamodb.Table('S-Status')

def lambda_handler(event, context):
  # tableをスキャン
  _scan_ = _starget_.scan()

  _stjson_ = _scan_['Items']  # スキャン結果をJsonデータへ変換
  _list_ = len(_stjson_)  # 配列数を取得

  for i in range(0,_list_):
    _url_ = "https://" + _stjson_[i]['domain']
    _name_ = _stjson_[i]['name']
    _dns_ = _stjson_[i]['dns']
    _date_ = str(datetime.datetime.now())

    if _dns_ == "OK":
      try:
        _req_ = requests.get(_url_, timeout=3)
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
        res = _sstatus_.put_item( Item = _result_ )
    else:
      print(_stjson_[i]['domain'] + " is not resolved.")

  return

