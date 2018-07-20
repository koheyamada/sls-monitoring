# checkURL.py
# Get URLs from DynamoDB.
# Check the status of URL.
# Write the status to DynamoDB.

import socket
import boto3
from boto3.dynamodb.conditions import Key, Attr
import logging

_dynamodb_ = boto3.resource('dynamodb')
_starget_ = _dynamodb_.Table('S-Target')

#def lambda_handler(event, context):
# tableをスキャン
_scan_ = _starget_.scan()
_stjson_ = _scan_['Items']  # スキャン結果をJsonデータへ変換
_list_ = len(_stjson_)  # 配列数を取得

for i in range(0,_list_):
  try:
    _domain_ = _stjson_[i]['domain']
    _addr1_ = socket.gethostbyname(_domain_)
    _addr2_ = socket.gethostbyname('google.c')
  except Exception as e:
#    logging.info(e.response['Error']['Message'])
    print(_addr1_)
    print(_addr2_)
  else:
    print(_addr1_)
    print(_addr2_)

#return res
