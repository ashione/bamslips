#!/bin/bash

PIP=`which pip`
if [ ${#PIP} -eq 0 ] ; then
    echo "please install pip first"
    exit
fi
function install_requirements(){
    source ./venv/bin/activate
    pip install -r requirements.txt
}
if [ ! -d venv ]; then
    pip install virutalenv
    virutallenv venv
fi

install_requirements
    
