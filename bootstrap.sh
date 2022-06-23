#!/bin/sh
cd /home/ubuntu/app
python3 -m cron.fetch_clubs
python3 -m cron.fetch_players