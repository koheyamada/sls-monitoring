import requests
import boto3
from boto3.dynamodb.conditions import Key, Attr
import logging
import json
import datetime
import slackweb

# DynamoDB
_dynamodb_ = boto3.resource('dynamodb')
_starget_ = _dynamodb_.Table('S-Target')
_sstatus_ = _dynamodb_.Table('S-Status')
_sresult_ = _dynamodb_.Table('S-Result')

#def lambda_handler(event, context):
_scan_ = _starget_.scan()
_stjson_ = _scan_['Items']
_list_ = len(_stjson_)

for i in range(0,_list_):
  try:
    _url_ = "https://" + _stjson_[i]['domain']
    _gens_ = _stjson_[i]['gens']
    _name_ = _stjson_[i]['name']
    _check_ = _stjson_[i]['check']
    _healthy_ = _stjson_[i]['healthy']
    _unhealthy_ = _stjson_[i]['unhealthy']
    _slack_ = _stjson_[i]['slack']

    _ssquery_ = _sstatus_.query(
      KeyConditionExpression = Key('url').eq(_url_),
      FilterExpression=Attr('name').eq(_name_),
      ScanIndexForward = False,
      Limit = int(_gens_)
    )

    num = 0
    for i in _ssquery_['Items']:
      if i['scode'] != 200:
        num += 1

    if num == _gens_:
      _status_ = 'unhealthy'
      if _unhealthy_ == 1:
        slack = slackweb.Slack(url=_slack_)
        slack.notify(text="unhealthy!!")
    else:
      _status_ = 'healthy'
      if _healthy_ == 1:
        slack = slackweb.Slack(url=_slack_)
        slack.notify(text="healthy!!")

    _date_ = str(datetime.datetime.now())
    result = {
      'url':_url_,
      'date':_date_,
      'gens':_gens_,
      'name':_name_,
      'status':_status_
    }
    print(result)
    res = _sresult_.put_item( Item = result )
  except Exception as e:
    print(e)

# return res
