# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Fund(models.Model):

    fund_code = models.CharField(max_length=10,unique=True,default = "default")
    fund_name = models.CharField( blank=True, max_length=100 )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #meta_data = models.CharField( blank= True, max_length = 256, default ='null' )

    class Meta :
        ordering = ("fund_code",)

class FundNet(models.Model):
    fund_code = \
    models.ForeignKey(Fund,on_delete=models.CASCADE,to_field='fund_code',db_column='fund_code')	
    date = models.DateField()
    net_asset_value = models.FloatField()
    accumulated_net = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('fund_code','date',)
        unique_together = (("fund_code", "date"),)


class FundRealTimeNet(models.Model):
    fund_code = \
    models.ForeignKey(Fund,on_delete=models.CASCADE,to_field='fund_code',db_column='fund_code')	
    date = models.DateTimeField(['%Y-%m-%d %H:%M:%S'])
    net_asset_value = models.FloatField()
    delta = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('fund_code','date',)
        unique_together = (("fund_code", "date"),)

