# DiscordBot

## Instructions for Docker
1. Clone the repo in a directory of your choosing.
2. Install docker at this link: https://docs.docker.com/get-docker/
3. Make a file named `.env`
4. Paste this line into `.env` and insert your discord bot token: ```DISCORD_TOKEN = "your token here"```
4. Run: ```source up.sh``` 
5. To bring the bot down run: ```source down.sh```

## Instructions for Heroku
### Getting started with the GUI
1. Create a Heroku account if you do not already have one
2. Create a new Heroku app on the site
3. While in the GUI, configure your app's environmental variables to add your bot key to the DISCORD_BOT variable  

### Setting up your local copy of the bot
1. Fork the repo
2. Clone the repo  

### Getting started with the CLI
1. Install Heroku CLI (tutorial below)
2. Login on CLI
3. Once logged in add the heroku app to your git remotes using the following command ```heroku git:remote -a your-app-name```
4. In the terminal run ```heroku stack:set container```
5. Run ```heroku-up.sh```
6. When done, run ```heroku-down.sh```

References used:
# TODO: add heroku tutorial for installing cli tools
[Heroku tutorial|<https://devcenter.heroku.com/articles/build-docker-images-heroku-yml>]

