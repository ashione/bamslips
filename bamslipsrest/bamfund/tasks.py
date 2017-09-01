# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery.task.schedules import crontab
from celery.decorators import periodic_task
import os,datetime
from .periodic_task import append_fund_info_last_week,append_fund_realtime

@periodic_task(run_every=(crontab(minute='*')), name="some_task")
def some_task():
    now_time = datetime.datetime.now()
    os.system("echo {} >> ~/t.txt".format(now_time))
    return now_time

@periodic_task(run_every=(crontab(minute=0,hour='*/4')), name="append_last_week_fund_net")
def sch_append_fund_info_last_week():
    return append_fund_info_last_week()

@periodic_task(run_every=(crontab(minute='*/3')),name="append_last_week_fund_realtimenet")
def sch_append_fund_realtime_unit():
    return append_fund_realtime()


@shared_task
def add(x, y):
    return x + y
#
#
#@shared_task
#def mul(x, y):
#    return x * y
#
#
#@shared_task
#def xsum(numbers):
#    return sum(numbers)
