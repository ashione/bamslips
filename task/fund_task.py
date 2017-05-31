from apscheduler.schedulers.blocking import BlockingScheduler
from bamslips.fund.fund_try_fetch import paralle_append_all_fund_yesterday_info


sched = BlockingScheduler()

@sched.scheduled_job('cron',id='fund_every_yesterday_job',hour='*/3')
def sch_append_fund_info_every_yesterday():
    paralle_append_all_fund_yesterday_info()

#sched.add_job(sch_job, 'interval', seconds=5)
sched.start()

