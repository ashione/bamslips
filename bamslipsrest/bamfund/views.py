# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from bamfund.models import Fund,FundNet
from bamfund.serializers import FundSerializer,FundNetSerializer
#from ipdb import set_trace


@api_view(['GET', 'POST'])
def fund_list(request):
    """
    List all fund, or create a new fund.
    """
    if request.method == 'GET':
        funds = Fund.objects.all()
        serializer = FundSerializer(funds, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FundSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def fund_detail(request, pk):
    """
    Retrieve, update or delete a fund instance.
    """
    try:
        fund = Fund.objects.get(pk=pk)
    except Fund.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FundSerializer(fund)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FundSerializer(fund, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        fund.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def fund_net_list(request):
    """
    List all fund_net, or create a new fund_net.
    """
    print request.data
    if request.method == 'GET':
        fund_nets = FundNet.objects.all()
        serializer = FundNetSerializer(fund_nets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FundNetSerializer(data=request.data)
        #set_trace()
        if serializer.is_valid():
            #print serializer.data
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def fund_net_detail(request, pk):
    """
    Retrieve, update or delete a fund_net instance.
    """
    try:
        fund_net = FundNet.objects.get(pk=pk)
    except FundNet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FundNetSerializer(fund_net)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FundNetSerializer(fund_net, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        fund_net.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

