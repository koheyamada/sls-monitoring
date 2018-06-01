# sls-monitoring

checkStatus.py: URLヘルスチェック
例.
{'url': 'https://www.google.com', 'date': '2018-06-02 00:24:53.517059', 'gens': Decimal('3'), 'user': 'yamada', 'status': 'healthy'}
{'url': 'https://www.hengjiu.jp', 'date': '2018-06-02 00:24:53.587269', 'gens': Decimal('5'), 'user': 'kohei', 'status': 'healthy'}
{'url': 'https://www.yahoo.co.jp/', 'date': '2018-06-02 00:24:53.632257', 'gens': Decimal('3'), 'user': 'kohei', 'status': 'healthy'}

checkURL.py: URLステータスチェック 
例.
{'url': 'https://www.google.com', 'date': '2018-06-02 01:03:17.195019', 'status': 200, 'user': 'yamada'}
{'url': 'https://www.hengjiu.jp', 'date': '2018-06-02 01:03:17.524817', 'status': 200, 'user': 'kohei'}
{'url': 'https://www.yahoo.co.jp/', 'date': '2018-06-02 01:03:17.613123', 'status': 200, 'user': 'kohei'}
 
responseHistory.py: ステータス返却
例.
{'user': 'yamada', 'gens': Decimal('3'), 'url': 'https://www.google.com', 'id': Decimal('1')}
{'user': 'kohei', 'gens': Decimal('5'), 'url': 'https://www.hengjiu.jp', 'id': Decimal('1')}
{'user': 'kohei', 'gens': Decimal('3'), 'url': 'https://www.yahoo.co.jp/', 'id': Decimal('2')}

