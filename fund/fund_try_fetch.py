from fund_data import Fund_web
from bamslips.conf.settings import DATA_ROOT
import glog
import os
import pandas as pd
from joblib import Parallel, delayed
fund_web = Fund_web()
time_out_list = []
from datetime import datetime
from bamslips.conf.fund_code_list import code_list

def fetch_fund_code(i):
    try :
        code = '{:06d}'.format(i)
        res = fund_web.get_pure_info(code=code)
        if len(res.index) > 1 :
            glog.info("{} have {} lines".format(code,len(res.index)))
            res.to_csv(os.path.join(DATA_ROOT,code+'.csv'))
            glog.info("write {} in date ".format(code+'.csv'))
    except Exception,e:
        time_out_list.append(i)
        glog.error("{},timeout, exception msg :  {}".format(i,e))

def append_info_to_csv(afp,res,t,csv_file):

    t_date = datetime.strptime(t['date'].values[0],'%Y-%m-%d')
    for res_s_index in res.index:
        res_s = res[res.index==res_s_index]
        res_s_datetime = pd.to_datetime(res_s.index.values[0])
        if res_s_datetime > t_date :
            res[res.index>=res_s_index].to_csv(afp,header=False)
            glog.info("append one commit code info to {}".format(csv_file))
            break

def append_fund_code_yesterday(code):
    try :
        code = '{:06d}'.format(code) if isinstance(code,int) else code
        csv_file = os.path.join(DATA_ROOT,code+'.csv')
        if not os.path.exists(csv_file):
            glog.info("no such code source file, code {}".format(code))
            return
        t = None
        with open(csv_file,'r') as fp:
            t = pd.read_csv(fp).tail(1)

        with open(csv_file,'a') as afp:
            res = fund_web.get_yesterday_fund_info(code)
            #res = fund_web.get_pure_info(code,sdate='2017-03-25',edate='2017-05-31')
            if len(res.index) < 1 :
                glog.info("{} have {} lines".format(code,len(res.index)))
                return 
            append_info_to_csv(afp,res,t,csv_file)

    except ValueError,e:
        glog.error("append_fund_code_yesterday,{},timeout, exception msg : {}".format(code,e))

def paralle_read_all_fund_info():
    Parallel(n_jobs=4)(delayed(fetch_fund_code)(i) for i in range(0,999999))

def paralle_append_all_fund_yesterday_info():
    Parallel(n_jobs=4)(delayed(append_fund_code_yesterday)(code) for code in code_list)

if __name__ == '__main__':
    #Parallel(n_jobs=4)(delayed(fetch_fund_code)(i) for i in range(0,999999))
    #print time_out_list
    #print append_fund_code_yesterday(539003)
    paralle_append_all_fund_yesterday_info()
