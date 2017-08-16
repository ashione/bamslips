import requests
from bamslips.fund.fund_base import Fund_base
from bamslips.conf.settings import DATA_ROOT
from bamslips.conf.fund_code_list import code_list
import json
import glog
import os
from joblib import Parallel, delayed
import pandas as pd
from datetime import datetime
#coding=utf-8

class Fund_realtime_detail(Fund_base) : 

    url_format ='https://fundmobapi.eastmoney.com/FundMApi/FundBase.ashx?FCODE={code}&deviceid=Wap&plat=Wap&product=EFund&version=2.0.0'

    def get_fund_realtime_detail(self,code='000001'):
        fund_stack_url = self.url_format.format(code=code if isinstance(code,str) else '{:06d}'.format(code))
        resp = requests.get(fund_stack_url,headers=self.header)
        resp_json = resp.json()
        return resp_json

    def get_fund_realtime_net_unit(self,code):
        resp_json = self.get_fund_realtime_detail(code)
        realtime_unit = json.loads(resp_json['Datas']['Valuation'])
        value_s =\
        pd.DataFrame([[datetime.strptime(realtime_unit['gztime'],"%Y-%m-%d %H:%M"),
            float(realtime_unit['gsz']),float(realtime_unit['gszzl'])]], columns=('date', 'net_asset_value', 'delta'))
        return value_s.set_index(['date'])

def get_fund_realtime_net_info(code):
    item = Fund_realtime_detail()
    info = item.get_fund_realtime_detail(code)
    json_file = '{:06d}_rt_info.json'.format(code) if isinstance(code,int) else code+'_rt_info.json'
    json_file = os.path.join(DATA_ROOT,json_file)
    with open(json_file,'w') as fp:
        json.dump(info,fp,indent=4) 
        glog.info('write {} fund stack into {}'.format(code,json_file))

def append_realtime_info_to_csv(afp,res,t,csv_file):
    time_str = t['date'].values[0]
    t_date = datetime.strptime(time_str,'%Y-%m-%d %H:%M:%S') if \
        time_str.find(':')>0 else datetime.strptime(time_str,'%Y-%m-%d')
    for res_s_index in res.index:
        res_s = res[res.index==res_s_index]
        res_s_datetime = pd.to_datetime(res_s.index.values[0],format='%Y-%m-%d %H:%M:%S')
        if res_s_datetime > t_date :
            res[res.index>=res_s_index].to_csv(afp,header=False)
            glog.info("append one commit code info to {}".format(csv_file))
            break

fund_realtime_item = Fund_realtime_detail()

#unreal_time_type = ['005','002']

def append_fund_realtime_unit(code):
    try :
        code = '{:06d}'.format(code) if isinstance(code,int) else code
        csv_file = os.path.join(DATA_ROOT,code+'_rt.csv')
        json_file = os.path.join(DATA_ROOT,code+'_rt_info.json')
        if os.path.exists(json_file):
            with open(json_file,'r') as json_f:
                fund_code_detail = json.load(json_f)
                #if(fund_code_detail['Datas']['FUNDTYPE'] in unreal_time_type):
                #    glog.info('skip fund type :\
                #    {}'.format(fund_code_detail['Datas']['FUNDTYPE']))
                if (not fund_code_detail['Datas'].has_key('Valuation')) or \
                       fund_code_detail['Datas']['Valuation'] == None or \
                       fund_code_detail['Datas']['Valuation'] == 'null' :
                    return
        if not os.path.exists(csv_file):
            glog.info("no such code source file, code {}, now touch it".format(code))
            res = fund_realtime_item.get_fund_realtime_net_unit(code)
            res.to_csv(csv_file)
            return

        t = None
        with open(csv_file,'r') as fp:
            t = pd.read_csv(fp).tail(1)

        with open(csv_file,'a') as afp:
            res = fund_realtime_item.get_fund_realtime_net_unit(code)
            if len(res.index) < 1 :
                glog.info("{} have {} lines".format(code,len(res.index)))
                return 
            append_realtime_info_to_csv(afp,res,t,csv_file)

    except Exception,e:
        glog.error("append_fund_realtime info,{},timeout, exception msg : {}".format(code,e))

def paralle_get_fund_detail_according_fund_code():
    Parallel(n_jobs=4)(delayed(get_fund_realtime_net_info)(code) for code in code_list)

def paralle_get_fund_realtime_info_according_fund_code(codes=None):
    if codes:
        Parallel(n_jobs=4)(delayed(append_fund_realtime_unit)(code) for code in codes)
    else :
        Parallel(n_jobs=4)(delayed(append_fund_realtime_unit)(code) for code in code_list)

if __name__ == '__main__' :
    #paralle_get_fund_detail_according_fund_code()
    item = Fund_realtime_detail()
    #print item.get_fund_realtime_net_unit(110006)
    #print item.get_fund_realtime_detail(110006)
    print append_fund_realtime_unit('003718')
    #paralle_get_fund_realtime_info_according_fund_code()

