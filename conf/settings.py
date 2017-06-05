import bamslips
import os,sys
import joblib

PROJECT_ROOT=os.path.dirname(bamslips.__file__)
CONF_ROOT=os.path.join(PROJECT_ROOT,'conf')
DATA_ROOT=os.path.join(PROJECT_ROOT,'data')

PROJECT_JOB_NUM = 4*joblib.cpu_count()

