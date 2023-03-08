#!/bin/bash
# Read URL from user input
curl -s $1 | wc -c
