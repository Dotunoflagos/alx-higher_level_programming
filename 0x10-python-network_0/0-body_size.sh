#!/bin/bash
# Read URL from user input
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
