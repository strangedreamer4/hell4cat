#!/bin/bash

 # Define the download URL for ngrok (update to the latest version if needed)
NGROK_URL="https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip"

# Define the ngrok authentication token (replace with your own token)
NGROK_AUTH_TOKEN="2FrD5bm0yZ8KeLaxstKA71dU37d_3GhAtNut3rJsTbugbhwev"

# Check if ngrok is already installed
if [ -f ngrok ]; then
    :
else
    # Download and install ngrok without output
    curl -L $NGROK_URL -o ngrok.zip >/dev/null 2>&1
    unzip ngrok.zip >/dev/null 2>&1
    rm ngrok.zip
    chmod +x ngrok
fi

# Authenticate ngrok (replace with your ngrok auth token)
./ngrok authtoken $NGROK_AUTH_TOKEN >/dev/null 2>&1

# Run ngrok with desired options (e.g., HTTP on port 4444) using nohup to suppress output
nohup ./ngrok http 2424 >/dev/null 2>&1 &

# Disown the ngrok process to allow the terminal to be used for other tasks
disown

