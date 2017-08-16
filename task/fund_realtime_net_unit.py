from apscheduler.schedulers.blocking import BlockingScheduler
from bamslips.fund.fund_realtime_info import paralle_get_fund_realtime_info_according_fund_code
from bamslips.conf.fund_code_list import code_list


sched = BlockingScheduler()

#@sched.scheduled_job('cron',id='fund_realtime_fun_info_job',hour='0-4,9-16,21-24',minute="*/10")
#def sch_append_fund_realtime_info():
#    paralle_get_fund_realtime_info_according_fund_code()

@sched.scheduled_job('cron',id='fund_realtime_fun_info_job_0',hour='0-4,9-16,21-24',minute="0/10")
def sch_append_fund_realtime_info_0():
    paralle_get_fund_realtime_info_according_fund_code(code_list[0::4])

@sched.scheduled_job('cron',id='fund_realtime_fun_info_job_1',hour='0-4,9-16,21-24',minute="1/10")
def sch_append_fund_realtime_info_1():
    paralle_get_fund_realtime_info_according_fund_code(code_list[1::4])

@sched.scheduled_job('cron',id='fund_realtime_fun_info_job_2',hour='0-4,9-16,21-24',minute="2/10")
def sch_append_fund_realtime_info_2():
    paralle_get_fund_realtime_info_according_fund_code(code_list[2::4])

@sched.scheduled_job('cron',id='fund_realtime_fun_info_job_3',hour='0-4,9-16,21-24',minute="3/10")
def sch_append_fund_realtime_info_3():
    paralle_get_fund_realtime_info_according_fund_code(code_list[3::4])

sched.start()

