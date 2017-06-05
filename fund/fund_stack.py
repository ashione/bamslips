import requests
from bamslips.fund.fund_base import Fund_base
from bamslips.conf.settings import DATA_ROOT,PROJECT_JOB_NUM
from bamslips.conf.fund_code_list import code_list
import json
import glog
import os
from joblib import Parallel, delayed
#coding=utf-8

class Fund_stack(Fund_base) : 

    url_format = 'https://fundmobapi.eastmoney.com/FundMApi/FundInverstPositionNew.ashx?FCODE={code}&deviceid=Wap&plat=Wap&product=EFund&version=2.0.0'
    def get_fund_stack(self,code='000001'):
        fund_stack_url = self.url_format.format(code=code if isinstance(code,str) else '{:06d}'.format(code))
        resp = requests.get(fund_stack_url,headers=self.header,verify=False)
        resp_json = resp.json()
        return resp_json

def get_fund_stack_info(code):
    item = Fund_stack()
    info = item.get_fund_stack(code)
    json_file = '{:06d}.json'.format(code) if isinstance(code,int) else code+'.json'
    json_file = os.path.join(DATA_ROOT,json_file)
    with open(json_file,'w') as fp:
        json.dump(info,fp,indent=4) 
        glog.info('write {} fund stack into {}'.format(code,json_file))

def paralle_get_stack_info_according_fund():
    Parallel(n_jobs=PROJECT_JOB_NUM)(delayed(get_fund_stack_info)(code) for code in code_list)

if __name__ == '__main__' :
    paralle_get_stack_info_according_fund()

