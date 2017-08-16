from apscheduler.schedulers.blocking import BlockingScheduler
from bamslips.fund.fund_try_fetch import paralle_append_all_fund_yesterday_info,paralle_append_all_fund_last_week_info


sched = BlockingScheduler()

@sched.scheduled_job('cron',id='fund_every_yesterday_job',hour='*/3')
def sch_append_fund_info_every_yesterday():
    paralle_append_all_fund_yesterday_info()

@sched.scheduled_job('cron',id='fund_last_wekk_job',hour='2',day_of_week='6')
def sch_append_fund_info_last_week():
    paralle_append_all_fund_last_week_info()

#sched.add_job(sch_job, 'interval', seconds=5)
sched.start()

