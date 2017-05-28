#!/usr/bin/python
import requests 
import random
from bs4 import BeautifulSoup as bs
import re
import pandas as pd
from datetime import datetime
from datetime import date
import glog

class Fund_web : 
    url = 'http://fund.eastmoney.com/f10/F10DataApi.aspx?type=lsjz&code=164906&page=1&per=20&sdate=2017-05-25&edate=2017-05-28&rt=0.6335554370129914'
    url_format =\
    'http://fund.eastmoney.com/f10/F10DataApi.aspx?type=lsjz&code={code}&page={page}&per={per_page}&sdate={start_date}&edate={end_date}&rt={rand_time}'
    header = { 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
               'Accept-Encoding':'gzip, deflate, sdch',
               'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
               'Connection':'keep-alive',
               'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Mobile Safari/537.36' 
               }
    def get_pure_info(self,code='164906',sdate=None,edate=None):
        if not sdate:
            sdate = date(2000,1,1)
        if not edate:
            edate = date.today() 
        try :
            sdate = datetime.strptime(sdate,'%Y-%m-%d').date() if isinstance(sdate,str) else sdate
            edate = datetime.strptime(edate,'%Y-%m-%d').date() if isinstance(edate,str) else edate
        except Exception,e :
            glog.error("value error,{}".format(e))
            glog.info("set start_day in 2000.1.1 and end_day is today")
            sdate,edate = date(2000,1,1),date.today()

        days = abs(edate - sdate)
        page,per_page = (1,days.days)
        code_url = self.url_format.format(code=code,page=page,per_page=per_page,\
                                          start_date=sdate.isoformat(),end_date=edate.isoformat(),rand_time=random.random())
        print code_url
        resp = requests.get(code_url,headers=self.header)
        matcher =\
        re.compile(u'.*?(?P<date>\d+-\d+-\d+).*?>(?P<net_asset_value>\d+\.\d+)<.*?>(?P<accumulated_net>\d+\.\d+)<.*?')
        #print resp.content,type(resp.content),len(resp.content)
        matched = matcher.finditer(resp.content)
        value_dict = {}
        value_res =pd.DataFrame(columns=('date', 'net_asset_value', 'accumulated_net'))
        for matche_s in matched :
            x = matche_s.groupdict().values()
            value_s = pd.DataFrame([[datetime.strptime(x[0],"%Y-%m-%d"),float(x[1]),float(x[2])]], columns=('date', 'net_asset_value', 'accumulated_net'))
            value_res = pd.concat([value_res,value_s],ignore_index=True)
        res = value_res.set_index(['date']).sort_index()
        return res

if __name__ == '__main__':
    item = Fund_web()
    item.get_pure_info(edate='2017-05x-22',sdate=date(2017,3,4))

