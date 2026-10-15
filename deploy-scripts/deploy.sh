#!/bin/bash
set -euo pipefail

APP_DIR="/home/ubuntu/mlops-student-app"
VENV="/opt/ml-venv"

echo "Starting Student Result Predictor deployment..."

# Install Python tools

export DEBIAN_FRONTEND=noninteractive
apt-get update -y
apt-get install -y python3-venv python3-pip

# Create the virtual environment once

if [ ! -d "$VENV" ]; then
python3 -m venv "$VENV"
fi

# Install project dependencies

cd "$APP_DIR"
"$VENV/bin/pip" install --no-cache-dir -r requirements.txt

# Train and save the updated model

"$VENV/bin/python" train.py

# Create a systemd service to run the application

cat > /etc/systemd/system/mlops-student-app.service <<'SERVICE'
[Unit]
Description=MLOps Student Result Predictor
After=network.target

[Service]
Type=simple
WorkingDirectory=/home/ubuntu/mlops-student-app
ExecStart=/opt/ml-venv/bin/gunicorn --workers 2 --bind 0.0.0.0:80 app:app
Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target
SERVICE

# Reload and start the application

systemctl daemon-reload
systemctl enable mlops-student-app
systemctl restart mlops-student-app

echo "Student Result Predictor deployment completed."
