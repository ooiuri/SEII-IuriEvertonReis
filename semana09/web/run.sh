#!/bin/bash
pip install virtualenv
sudo /usr/bin/easy_install virtualenv
virtualenv env
./env/Scripts/activate
pip install -r requirements.txt

python3 app.py