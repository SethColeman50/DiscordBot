# DiscordBot

## Instructions for Docker
1. Clone the repo in a directory of your choosing.
2. Install docker at this link: https://docs.docker.com/get-docker/
3. Make a file named `.env`
4. Paste this line into `.env` and insert your discord bot token: ```DISCORD_TOKEN = "your token here"```
4. Run: ```source up.sh``` 
5. To bring the bot down run: ```source down.sh```

## Instructions for Heroku
1. Install Heroku CLI
2. Login on CLI
3. Configure your .env file through the Settings -> Config on the Heroku web GUI
4. Add a heroku.yml with
```	build:
		docker:
			web: Dockerfile```

5. In the terminal run `heroku stack:set container`
6. Run `heroku ps:scale web=1`

References used:
[Heroku tutorial|<https://devcenter.heroku.com/articles/build-docker-images-heroku-yml>]

