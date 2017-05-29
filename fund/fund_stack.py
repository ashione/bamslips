import requests
from bamslips.fund.fund_base import Fund_base
import json
import glog
#coding=utf-8

class Fund_stack(Fund_base) : 
    url_format = 'https://fundmobapi.eastmoney.com/FundMApi/FundInverstPositionNew.ashx?FCODE={code}&deviceid=Wap&plat=Wap&product=EFund&version=2.0.0'

    def get_fund_stack(self,code='000001'):
        fund_stack_url = self.url_format.format(code=code if isinstance(code,str) else '{:06d}'.format(code))
        resp = requests.get(fund_stack_url,headers=self.header)
        resp_json = resp.json()
        return resp_json


if __name__ == '__main__' :
    item = Fund_stack()
    info = item.get_fund_stack(code=3)
    #glog.info(info['Datas']['fundboods'])
    glog.info(info['Datas']['fundStocks'][0]['GPJC'])
    
