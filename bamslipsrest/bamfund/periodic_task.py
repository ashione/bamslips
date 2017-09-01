from bamslips.fund.fund_data import Fund_web
from bamslips.fund.fund_realtime_info import Fund_realtime_detail
import os,datetime
from bamfund.models import Fund,FundNet,FundRealTimeNet
import glog

def append_fund_info_last_week():
    fund_list = Fund.objects.all()
    fund_web = Fund_web()
    succ_count = 0
    for fund in fund_list : 
        fund_data =  fund_web.get_last_month_fund_info(code = fund.fund_code)
        for index,fund_item in fund_data.iterrows():
            try :
                FundNet.objects.create(fund_code = fund,
                        date = index,                       
                        net_asset_value=fund_item.net_asset_value,
                        accumulated_net = fund_item.accumulated_net)
                succ_count += 1
            except Exception,e:
                glog.info("integrityError : {}".format(e))
    return succ_count

def append_fund_realtime():
    fund_list = Fund.objects.all()
    fund_web = Fund_realtime_detail()
    succ_count = 0
    for fund in fund_list : 
        fund_data =  fund_web.get_fund_realtime_net_unit(code = fund.fund_code)
        for index,fund_item in fund_data.iterrows():
            try :
                FundRealTimeNet.objects.create(fund_code = fund,
                        date=index.strftime('%Y-%m-%d %H:%M:%S'),
                        net_asset_value=fund_item.net_asset_value,
                        delta = fund_item.delta)
                succ_count += 1
            except Exception,e:
                glog.info("integrityError : {}".format(e))
    glog.info("{} rows will be appended.".format(succ_count))
    return succ_count
#append_fund_info_last_week()
#append_fund_realtime()

