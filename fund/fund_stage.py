import pandas as pd

def diff_unit_price(fund_stage):
    fund_stage['net_asset_value_diff'] = \
        fund_stage['net_asset_value'].diff().fillna(0.0)


if __name__ == '__main__' :
    test_data = {'net_asset_value_diff' : [1,2.]}
            }

