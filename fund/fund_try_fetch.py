from fund_data import Fund_web
from bamslips.conf.settings import DATA_ROOT
import glog
import os
from joblib import Parallel, delayed
fund_web = Fund_web()
time_out_list = []

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


if __name__ == '__main__':
    Parallel(n_jobs=4)(delayed(fetch_fund_code)(i) for i in range(0,999999))
    print time_out_list
