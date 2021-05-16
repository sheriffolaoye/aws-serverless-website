FROM python:3.9-slim

RUN apt update \
    && apt install --no-install-recommends --no-install-suggests -y \
    nginx cron rsyslog

WORKDIR /app
COPY nginx_config ./
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt \
    && cp nginx_config /etc/nginx/sites-enabled/default
COPY script.sh ./
RUN chmod +x script.sh

COPY web-server web-server
COPY repository-updater repository-updater

ENTRYPOINT ["./script.sh"]