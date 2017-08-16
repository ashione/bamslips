#-*- coding:utf-8 -*-
import requests
from datetime import datetime
from bamslips.fund.fund_data import Fund_web


def add_fund_net():
    url = 'http://127.0.0.1:8000/fund_net/'

    fund_code = '164906'
    fund_web = Fund_web()
    fund_data = fund_web.get_last_year_fund_info(code=fund_code)
    #print fund_data
    for index, fund_item in fund_data.iterrows():
        print 'index : ',index
        print 'fund_item' ,fund_item
        #print fund_data[index]

        fund_net_test_json = {
                'fund_code' : '164906',
                'date' : index.strftime('%Y-%m-%d'),
                #'date' : datetime.strptime('2015-10-12', '%Y-%M-%d'),
                'net_asset_value' : fund_item.net_asset_value,
                "accumulated_net" : fund_item.accumulated_net,
        }

        result = requests.post(url,json=fund_net_test_json)

        print result.content

def add_fund():
    url = 'http://127.0.0.1:8000/funds/'
    fund= {
            'fund_code' : "164906",
            'fund_name' : "",
    }

    result = requests.post(url,json=fund)

    print result.content

#add_fund()
add_fund_net()
