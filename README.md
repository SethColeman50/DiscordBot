# DiscordBot

## Instructions for Docker
1. Clone the repo in a directory of your choosing.
2. Install docker at this link: https://docs.docker.com/get-docker/
3. Make a file named `.env`
4. Paste this line into `.env` and insert your discord bot token: ```DISCORD_TOKEN = "your token here"```
4. Run: ```source up.sh``` 
5. To bring the bot down run: ```source down.sh```

## Instructions for Heroku
### Setting up a local repository
1. Clone the repo using ```git clone https://github.com/cs220s22/DiscordBot.git```

### Getting started with the GUI
1. Create a Heroku account if you do not already have one
2. Create a new Heroku app on the site
3. From the Settings tab, configure your environmental variables to add your bot key to the ```DISCORD_TOKEN``` variable
4. From the Settings tab, add the ```heroku/python``` build package to your application  

### Getting started with the CLI
1. Install Heroku CLI (tutorial below)
2. Login on CLI
3. Once logged in add the heroku app to your git remotes using the following command ```heroku git:remote -a your-app-name```
4. In the terminal run ```heroku stack:set container```
5. Deploy your app using ```git push heroku main```
6. Run ```heroku-up.sh```
7. When done, run ```heroku-down.sh```

References used:
(Install the Heroku CLI|<https://devcenter.heroku.com/articles/heroku-cli#install-the-heroku-cli>)
(Heroku tutorial|<https://devcenter.heroku.com/articles/build-docker-images-heroku-yml>)

