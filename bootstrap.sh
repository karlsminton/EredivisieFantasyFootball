#!/bin/sh
#export FLASK_APP=./index.py
#flask run -h 0.0.0.0
cd /home/ubuntu/app
python3 -m cron.fetch_clubs
python3 -m cron.fetch_players