#!/usr/bin/env bash
set -euo pipefail

# The directory name is deliberately restricted to a single safe path segment.
read -r -p 'Enter a name for the output folder: ' folder_name
if [[ ! "$folder_name" =~ ^[A-Za-z0-9_-]+$ ]]; then
  echo 'Use only letters, numbers, underscores, or hyphens.' >&2
  exit 1
fi

report_dir="${PWD}/${folder_name}"
mkdir -p "$report_dir"
process_file="${report_dir}/processes.txt"
touch "$process_file"

current_date=$(date)
host_name=$(hostname)
user_name=$(id -un)

echo "Date: $current_date"
echo "Hostname: $host_name"
echo "Username: $user_name"
echo 'Disk usage:'
df -h
echo 'Running processes:'
ps -ef > "$process_file"
echo "Process list saved to $process_file"
