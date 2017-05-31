from apscheduler.schedulers.blocking import BlockingScheduler
from bamslips.fund.fund_realtime_info import paralle_get_fund_realtime_info_according_fund_code


sched = BlockingScheduler()

@sched.scheduled_job('cron',id='fund_realtime_fun_info_job',hour='9-16,21-29',minute="*/5")
def sch_append_fund_realtime_info():
    paralle_get_fund_realtime_info_according_fund_code()

sched.start()
