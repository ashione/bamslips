from bamfund.models import Fund,FundNet
from bamfund.serializers import FundSerializer,FundNetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import datetime

fund = Fund.objects.get(pk=1)
fund_net = FundNet(fund = fund,date='2015-10-12',net_asset_value = 1.0,accumulated_net = 1.0)
fund_net = FundNet(fund = fund,date='2015-10-12',net_asset_value = 2.0,accumulated_net = 1.0)
fund_net.save()
