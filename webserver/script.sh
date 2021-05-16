#!/bin/bash

# start services
service rsyslog start
service cron start
service nginx start

# start cron job
declare -p | grep -Ev 'BASHOPTS|BASH_VERSINFO|EUID|PPID|SHELLOPTS|UID' > ~/cron.env
(crontab -l 2>/dev/null; echo "SHELL=/bin/bash") | crontab -
(crontab -l 2>/dev/null; echo "BASH_ENV=~/cron.env") | crontab -
(crontab -l 2>/dev/null; echo "0 */2 * * * /usr/local/bin/python /app/repository-updater/repo_updater.py >> ~/cron.log 2>&1") | crontab -

# update databse once and start web server
python repository-updater/repo_updater.py
cd web-server
gunicorn --bind=unix:/tmp/socket app:app