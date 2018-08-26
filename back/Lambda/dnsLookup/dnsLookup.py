# dnsLookup.py
# Check the domain is registered in DNS.

import socket
import boto3
from boto3.dynamodb.conditions import Key, Attr
import logging
import datetime

_dynamodb_ = boto3.resource('dynamodb')
_starget_ = _dynamodb_.Table('S-Target')

# tableをスキャン
_scan_ = _starget_.scan()
_stjson_ = _scan_['Items']  # スキャン結果をJsonデータへ変換
_list_ = len(_stjson_)  # 配列数を取得

def lambda_handler(event, context):
  for i in range(0,_list_):
    try:
      _domain_ = _stjson_[i]['domain']
      _name_ = _stjson_[i]['name']
      _dns_ = _stjson_[i]['dns']
      _date_ = str(datetime.datetime.now())
    except Exception as e:
      logging.info(e.response['Error']['Message'])
    else:
      try:
        _addr_ = socket.gethostbyname(_domain_)
      except Exception as e:
        logging.info(e.response['Error']['Message'])
        res = _starget_.update_item(
          Key={
            'domain': _domain_,
            'name': _name_
          },
          UpdateExpression='SET dns = :vall',
          ExpressionAttributeValues={
            ':vall': "NG"
          }
        )
        print(res)
      else:
        res = _starget_.update_item(
          Key={
            'domain': _domain_,
            'name': _name_
          },
          UpdateExpression='SET dns = :dns, udate = :udate ',
          ExpressionAttributeValues={
            ':dns': "OK",
            ':udate': _date_
          }
        )
        print(res)

  return
