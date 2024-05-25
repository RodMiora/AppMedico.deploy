#!/usr/bin/env bash
# exit on error
set -o errexit

# Ensure correct line endings (LF) for this script
sed -i 's/\r$//' "$0"

pip install -r requirements.txt

python manage.py collectstatic --no-input

python manage.py migrate