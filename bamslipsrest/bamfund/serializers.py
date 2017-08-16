from rest_framework import serializers
from .models import Fund,FundNet

class FundSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fund
        fields = ('id', 'fund_code', 'fund_name')

class FundNetSerializer(serializers.ModelSerializer):

    class Meta:
        model = FundNet
        fields = ('id', 'fund_code', 'date','net_asset_value','accumulated_net')
