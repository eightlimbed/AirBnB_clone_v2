#!/usr/bin/env bash
# This script sets up web servers for the deployment of web_static

# Install nginx
sudo apt-get update && apt-get install -y nginx

# Create directories
sudo mkdir -p /data/web_static/shared
sudo mkdir -p /data/web_static/releases/test

# Create fake html file for testing if deployment worked
echo "success" | sudo tee /data/web_static/releases/test/index.html

# Create symlink called 'current' that links to the test folder
# If it already exists, remove it
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# Give ownership of /data/ and all subdirectories to ubuntu
sudo chown -R ubuntu:ubuntu /data/

# Update sites-enabled/default to to serve the contents of `current` from the
# URL example.com/hbhb_static
sudo sed -i \
'42i location /hbnb_static/ {\n alias /data/web_static/current/;\n}' \
/etc/nginx/sites-enabled/default

sudo rm /etc/nginx/sites-available/default

# Restart the server
sudo service nginx restart
