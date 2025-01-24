#!/bin/bash

# Создаем символические ссылки, если их нет
if [ ! -L /etc/letsencrypt/live/mer1d1an.ru/fullchain.pem ]; then
    ln -s /etc/letsencrypt/archive/mer1d1an.ru/fullchain*.pem /etc/letsencrypt/live/mer1d1an.ru/fullchain.pem
    ln -s /etc/letsencrypt/archive/mer1d1an.ru/privkey*.pem /etc/letsencrypt/live/mer1d1an.ru/privkey.pem
fi

while true; do
    certbot renew --quiet --post-hook "nginx -s reload"
    sleep 86400
done