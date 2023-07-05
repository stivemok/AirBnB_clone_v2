#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

apt-get -y update
apt-get install -y nginx
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/release/test/
# touch /data/web_static/release/test/index.html
echo "Holberton School" > /data/web_static/release/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -hR ubuntu:ubuntu /data
sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
service nginx restart
