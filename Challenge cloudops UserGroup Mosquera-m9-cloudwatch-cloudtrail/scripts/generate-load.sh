#!/bin/bash

LOG_FILE="/var/log/cloudops/application.log"

echo "======================================"
echo " CloudOps M9 - CPU Incident Generator "
echo "======================================"
echo
echo "Generating CPU load for 5 minutes..."
echo "Watch CPUUtilization in CloudWatch."
echo

echo "$(date '+%Y-%m-%d %H:%M:%S') WARN High workload detected - CPU stress test started" >> "$LOG_FILE"

stress-ng --cpu 2 --timeout 300s &
STRESS_PID=$!

sleep 60
echo "$(date '+%Y-%m-%d %H:%M:%S') ERROR Application response degraded - High CPU utilization" >> "$LOG_FILE"

sleep 60
echo "$(date '+%Y-%m-%d %H:%M:%S') ERROR Processing timeout detected - Application performance degraded" >> "$LOG_FILE"

wait "$STRESS_PID"

echo "$(date '+%Y-%m-%d %H:%M:%S') INFO CPU workload finished - Application recovering" >> "$LOG_FILE"

echo
echo "Incident finished."
