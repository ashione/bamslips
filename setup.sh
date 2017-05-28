#!/bin/bash

PIP=`which pip`
if [ ${#PIP} -eq 0 ] ; then
    echo "please install pip first"
    exit
fi
function install_requirements(){
    current_dir=`pwd`
    parent_path=`dirname $current_dir` 

    source ./venv/bin/activate
    echo "$parent_path" > ./venv/lib/python2.7/site-packages/bamslips.pth
    pip install -r requirements.txt
    export PATH=./venv/bin:$PATH
}
if [ ! -d venv ]; then
    pip install virutalenv
    virutallenv venv
fi

if [ ! -d data ]; then
    mkdir data
fi

install_requirements
    
