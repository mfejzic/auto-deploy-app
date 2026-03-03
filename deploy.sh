#!/bin/bash
export GIT_SSH_COMMAND='ssh -i ~/.ssh/id_rsa_github -o StrictHostKeyChecking=no'
cd ~/auto-deploy-app
git pull origin main
pkill gunicorn
source venv/bin/activate
nohup gunicorn app:app --bind 0.0.0.0:8000 > deploy.log 2>&1 &
