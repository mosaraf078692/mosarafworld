#!bin/bash

python3 -m venv mw_venv
source mw_venv/bin/activate
pip install -r requirements.txt
gunicorn mw_pro.wsgi --bind 127.0.0.1:8000