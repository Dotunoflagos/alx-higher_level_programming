#!/bin/bash
# Read URL from user input
response=$(curl -sI $1)
size=$(echo "$response" | awk '/Content-Length/ {print $2}')
echo "$size"
