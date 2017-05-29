#!/usr/bin/python
import requests 
import random
from bs4 import BeautifulSoup as bs
import re
import pandas as pd
from datetime import datetime,timedelta,date
import dateutil.relativedelta
import glog
from bamslips.fund.fund_base import Fund_base

class Fund_web(Fund_base) : 
    url_format =\
    'http://fund.eastmoney.com/f10/F10DataApi.aspx?type=lsjz&code={code}&page={page}&per={per_page}&sdate={start_date}&edate={end_date}&rt={rand_time}'
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

        glog.info('request url : {}'.format(code_url))

        resp = requests.get(code_url,headers=self.header)
        matcher =\
        re.compile(u'.*?(?P<date>\d+-\d+-\d+).*?>(?P<net_asset_value>\d+\.\d+)<.*?>(?P<accumulated_net>\d+\.\d+)<.*?')
        #print resp.content,type(resp.content),len(resp.content)
        matched = matcher.finditer(resp.content)
        value_res =pd.DataFrame(columns=('date', 'net_asset_value', 'accumulated_net'))

        for matche_s in matched :
            x = matche_s.groupdict().values()
            value_s = pd.DataFrame([[datetime.strptime(x[0],"%Y-%m-%d"),float(x[1]),float(x[2])]], columns=('date', 'net_asset_value', 'accumulated_net'))
            value_res = pd.concat([value_res,value_s],ignore_index=True)
        res = value_res.set_index(['date']).sort_index()
        return res
    def get_yesterday_fund_info(self,code):
        today = date.today()
        yesterday = today - timedelta(days=1)
        return self.get_pure_info(code=code,sdate=yesterday,edate=today)

    def get_last_week_fund_info(self,code):
        today = date.today()
        last_week = today - timedelta(weeks=1)
        return self.get_pure_info(code=code,sdate=last_week,edate=today)

    def get_last_month_fund_info(self,code):
        today = date.today()
        last_month = today - dateutil.relativedelta.relativedelta(months=1)
        return self.get_pure_info(code=code,sdate=last_month,edate=today)

    def get_last_year_fund_info(self,code):
        today = date.today()
        last_year = today - dateutil.relativedelta.relativedelta(years=1)
        return self.get_pure_info(code=code,sdate=last_year,edate=today)

if __name__ == '__main__':
    item = Fund_web()
    #item.get_pure_info(edate='2017-05x-22',sdate=date(2017,3,4))
    #print item.get_yesterday_fund_info(1)
    #print item.get_last_week_fund_info(1)
    print item.get_last_month_fund_info(1)
    print item.get_last_year_fund_info(1)

