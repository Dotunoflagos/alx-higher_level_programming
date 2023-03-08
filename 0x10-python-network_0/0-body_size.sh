#!/bin/bash

# Read URL from user input
read -p "Enter URL: " url

# Send request using curl and save response to a variable
response=$(curl -sI $url)

# Extract the Content-Length header value
content_length=$(echo "$response" | grep -i content-length | awk '{print $2}' | tr -d '\r')

# Display the size of the body of the response
echo "${content_length}"
