#!/bin/sh
docker build . -t discord_bot
# Builds a docker image with the Dockerfile in the current directory. -t specifies the name of the image
docker run -d -v $PWD:/bot --name discord_bot discord_bot
# Runs the discord_bot image and makes a container. -d is daemon mode so you get your command prompt back, -v mounts the /bot directory in the container to the
# current directory, and the --name sets the name to discord_bot