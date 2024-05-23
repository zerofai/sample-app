#!/bin/bash

# Obtain the environment variables
TARGET_URL=${TARGET_URL}
INTERVAL=${INTERVAL}
INSECURE=${INSECURE}

# Check if TARGET_URL and INTERVAL are set
if [ -z "$TARGET_URL" ] || [ -z "$INTERVAL" ]; then
  echo "TARGET_URL and INTERVAL environment variables must be set."
  exit 1
fi

# Convert comma-separated TARGET_URL into an array
IFS=',' read -r -a URL_ARRAY <<< "$TARGET_URL"

# Function to access all URLs
access_all_urls() {
  for URL in "${URL_ARRAY[@]}"; do
    # Build the curl command
    CURL_CMD="curl -s -o /dev/null -w "%{http_code}""

    if [ "$INSECURE" == "YES" ]; then
      CURL_CMD="$CURL_CMD --insecure"
    fi

    CURL_CMD="$CURL_CMD $URL"

    # Execute the curl command
    echo "Accessing $URL"
    $CURL_CMD
  done
}

# Loop that accesses all URLs based on the specified interval
while true; do
  access_all_urls
  sleep "$INTERVAL"
done