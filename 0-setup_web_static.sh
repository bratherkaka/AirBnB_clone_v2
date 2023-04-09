#!/usr/bin/env bash

# Install nginx if it is not already installed
if [ ! -x "$(command -v nginx)" ]; then
  sudo apt-get update
  sudo apt-get -y install nginx
fi

# Create required directories if they don't exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo chown -R ubuntu:ubuntu /data/

# Create a fake HTML file to test nginx configuration
echo "<html><head></head><body>Holberton School</body></html>" | sudo tee /data/web_static/releases/test/index.html

# Create symbolic link to test folder
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Update nginx configuration to serve the content of /data/web_static/current/
# Restart nginx after updating configuration
sudo sed -i '29i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx restart

exit 0
