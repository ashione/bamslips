from rest_framework import serializers
from .models import Fund,FundNet,FundRealTimeNet

class FundSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fund
        fields = ('id', 'fund_code', 'fund_name','created_at','updated_at')

class FundNetSerializer(serializers.ModelSerializer):

    class Meta:
        model = FundNet
        fields = ('id', 'fund_code',
                'date','net_asset_value','accumulated_net','created_at','updated_at')

class FundRealTimeNetSerializer(serializers.ModelSerializer):

    class Meta:
        model = FundRealTimeNet
        fields = ('id', 'fund_code', 'date','net_asset_value','delta','created_at','updated_at')
