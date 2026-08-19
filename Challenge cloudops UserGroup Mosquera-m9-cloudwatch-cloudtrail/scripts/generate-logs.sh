#!/bin/bash

LOG_FILE="/var/log/cloudops/application.log"

while true
do
  TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
  echo "$TIMESTAMP INFO CloudOps application running normally" >> "$LOG_FILE"
  sleep 10
done
