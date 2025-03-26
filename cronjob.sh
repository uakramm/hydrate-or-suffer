#!/bin/bash

cd /Users/ushna/OU/personal/hydrate-or-suffer
source .venv/bin/activate
python src/reminder.py >> reminder.log 2>&1
