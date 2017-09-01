#!/bin/bash
PID_DIR=/var/run/celery
LOG_DIR=/var/log/celery

function exist_or_create(){
    if [ ! -d $1  ]; then
          mkdir -p $1
    fi
}

function celery_help(){
    echo "celery manual help : "
    echo "please input action [start/stop] [all/work/beat]"
    echo -e "\t watch logfile $LOG_DIR, pid : ${LOG_DIR}"
}

function start_celery_work(){
    # --events \ send events to monitor 
    #--autoreload \ autoload tasks
    python manage.py celery worker  \
        --autoreload --beat \
        --events  \
        --loglevel=debug \
        --pidfile="$PID_DIR/%n.pid" \
        --logfile="$LOG_DIR/%n%I.log" &
}

function start_celery_beat() {
    python manage.py celery beat \
        --loglevel=debug \
        --pidfile="$PID_DIR/beat.pid" \
        --logfile="$LOG_DIR/beat.log" &

}

function start_all() {
    start_celery_beat
    start_celery_work
}

exist_or_create $PID_DIR
exist_or_create $LOG_DIR


if [ $# -gt 0 ]; then
    if [ $1 = 'start' ]; then
        if [ $# -gt 1 ]; then
            if [ $2 = 'worker' ]; then
                start_celery_work
            elif [ $2 = 'beat' ]; then
                start_celery_beat
            else 
                celery_help
            fi
        else
            start_all
        fi 

        #celery -A bamslipsrest beat -l info &
        #celery -A bamslipsrest worker -l info &
    elif [ $1 = 'stop' ]; then
         cat /var/run/celery/*.pid | xargs kill -9
         cat /var/run/celery/*.pid 
         echo 'kill all pid'
    elif [ $1 = 'shutdown' ]; then
        ps aux | grep "run/celery" | awk '{print $2}' | xargs kill -9
    else
        celery_help
    fi
else
    celery_help
fi
