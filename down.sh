#!/bin/sh
docker stop discord_bot
# Stops the container gracefully to save any changes
docker rm discord_bot
# Removes the container so it can be run again by up.sh
