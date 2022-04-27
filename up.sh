#!/bin/sh
docker build . -t discord_bot
docker run -d -v $PWD:/bot --name discord_bot discord_bot

