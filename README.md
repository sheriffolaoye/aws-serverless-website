# my-website
Source and configruation files for my website [sheriffolaoye.com](sheriffolaoye.com)

This website uses:

- EC2: An EC2 t2.nano server running ubuntu 18.
- Flask: Flask is used to handle and process requests.
- Gunicorn: WSGI HTTP server for running Flask web app. It is configured to run as a systemctl service.
- Nginx: High performance proxy server that talks to gunicorn.
- MySQL: Database for storing repository information.
- Cron Job: For running a python script that regularly updates the database with the latest repository information.
- Route 53: For the Domain Name Service(DNS).