import pandas as pd
from bamslips.fund.fund_data import Fund_web

def diff_unit_price(fund_stage):
    fund_stage['net_asset_value_diff'] = \
        fund_stage['net_asset_value'].diff().fillna(0.0)
    print fund_stage


if __name__ == '__main__' :
    test_data = {'net_asset_value_diff' : [1,2.]}
    fund = Fund_web()
    data = fund.get_last_year_fund_info(code='164906')
    diff_unit_price(data)

