# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from bamfund.models import Fund,FundNet,FundRealTimeNet
from bamfund.serializers import FundSerializer,FundNetSerializer,FundRealTimeNetSerializer
from rest_framework import generics
from rest_framework import permissions
from datetime import datetime,timedelta,date
import glog
from rest_framework.exceptions import APIException,ValidationError
#from rest_framework.pagination import PageNumberPagination
#from ipdb import set_trace


class FundList(generics.ListCreateAPIView):
    queryset = Fund.objects.all()
    serializer_class = FundSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        """
        Optionally restricts the queryset by filtering against
        query parameters in the URL.
        """
        fund_code = self.request.query_params.get('code')
        if fund_code:
            return self.queryset.filter(fund_code = fund_code)
        else:
            return self.queryset

    #"""
    #List all fund, or create a new fund.
    #"""
    #if request.method == 'GET':
    #    funds = Fund.objects.all()
    #    serializer = FundSerializer(funds, many=True)
    #    return Response(serializer.data)

    #elif request.method == 'POST':
    #    serializer = FundSerializer(data=request.data)
    #    if serializer.is_valid():
    #        serializer.save()
    #        return Response(serializer.data, status=status.HTTP_201_CREATED)
    #    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FundDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fund.objects.all()
    serializer_class = FundSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    #"""
    #Retrieve, update or delete a fund instance.
    #"""
    #try:
    #    fund = Fund.objects.get(pk=pk)
    #except Fund.DoesNotExist:
    #    return Response(status=status.HTTP_404_NOT_FOUND)

    #if request.method == 'GET':
    #    serializer = FundSerializer(fund)
    #    return Response(serializer.data)

    #elif request.method == 'PUT':
    #    serializer = FundSerializer(fund, data=request.data)
    #    if serializer.is_valid():
    #        serializer.save()
    #        return Response(serializer.data)
    #    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #elif request.method == 'DELETE':
    #    fund.delete()
    #    return Response(status=status.HTTP_204_NO_CONTENT)
class FundNetList(generics.ListCreateAPIView):
    queryset = FundNet.objects.all()
    serializer_class = FundNetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        """
        Optionally restricts the queryset by filtering against
        query parameters in the URL.
        """
        queryset = self.queryset

        fund_code = self.request.query_params.get('code')
        start_time = self.request.query_params.get('start_time')
        end_time = self.request.query_params.get('end_time')

        if fund_code:
            queryset = queryset.filter(fund_code = fund_code)
        if start_time and end_time :
            #today = date.today()
            #last_month = today - dateutil.relativedelta.relativedelta(months=1)
            print start_time,end_time
            try :
                start_date = datetime.strptime(start_time,'%Y%m%d')
                end_date = datetime.strptime(end_time,'%Y%m%d')
                queryset = queryset.filter(date__lte = end_date, date__gte = start_date)
            except Exception,e:
                glog.info(e)
                #return Response(status=status.HTTP_400_BAD_REQUEST)
                raise ValidationError(detail={"code" : 400,"msg":"data invalid"})

        return queryset

    #"""
    #List all fund, or create a new fund.
    #"""
    #if request.method == 'GET':
    #    funds = Fund.objects.all()
    #    serializer = FundSerializer(funds, many=True)
    #    return Response(serializer.data)

    #elif request.method == 'POST':
    #    serializer = FundSerializer(data=request.data)
    #    if serializer.is_valid():
    #        serializer.save()
    #        return Response(serializer.data, status=status.HTTP_201_CREATED)
    #    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FundNetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FundNet.objects.all()
    serializer_class = FundNetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

#@api_view(['GET', 'POST'])
#def fund_net_list(request):
#    """
#    List all fund_net, or create a new fund_net.
#    """
#    print request.data
#    if request.method == 'GET':
#        fund_nets = FundNet.objects.all()
#        serializer = FundNetSerializer(fund_nets, many=True)
#        return Response(serializer.data)
#
#    elif request.method == 'POST':
#        serializer = FundNetSerializer(data=request.data)
#        #set_trace()
#        if serializer.is_valid():
#            #print serializer.data
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#@api_view(['GET', 'PUT', 'DELETE'])
#def fund_net_detail(request, pk):
#    """
#    Retrieve, update or delete a fund_net instance.
#    """
#    try:
#        fund_net = FundNet.objects.get(pk=pk)
#    except FundNet.DoesNotExist:
#        return Response(status=status.HTTP_404_NOT_FOUND)
#
#    if request.method == 'GET':
#        serializer = FundNetSerializer(fund_net)
#        return Response(serializer.data)
#
#    elif request.method == 'PUT':
#        serializer = FundNetSerializer(fund_net, data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#    elif request.method == 'DELETE':
#        fund_net.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)


class FundRealTimeNetList(generics.ListCreateAPIView):
    queryset = FundRealTimeNet.objects.all()
    serializer_class = FundRealTimeNetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

#@api_view(['GET', 'POST'])
#def fund_realtime_net_list(request):
#    """
#    List all fund_realtime_net, or create a new fund_realtime_net.
#    """
#    print request.data
#    if request.method == 'GET':
#        fund_realtime_nets = FundRealTimeNet.objects.all()
#        serializer = FundRealTimeNetSerializer(fund_realtime_nets, many=True)
#        return Response(serializer.data)
#
#    elif request.method == 'POST':
#        serializer = FundRealTimeNetSerializer(data=request.data)
#        #set_trace()
#        if serializer.is_valid():
#            #print serializer.data
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FundRealTimeNetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FundRealTimeNet.objects.all()
    serializer_class = FundRealTimeNetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

#@api_view(['GET', 'PUT', 'DELETE'])
#def fund_realtime_net_detail(request, pk):
#    """
#    Retrieve, update or delete a fund_realtime_net instance.
#    """
#    try:
#        fund_realtime_net = FundRealTimeNet.objects.get(pk=pk)
#    except FundRealTimeNet.DoesNotExist:
#        return Response(status=status.HTTP_404_NOT_FOUND)
#
#    if request.method == 'GET':
#        serializer = FundRealTimeNetSerializer(fund_realtime_net)
#        return Response(serializer.data)
#
#    elif request.method == 'PUT':
#        serializer = FundRealTimeNetSerializer(fund_realtime_net, data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#    elif request.method == 'DELETE':
#        fund_realtime_net.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)
#
