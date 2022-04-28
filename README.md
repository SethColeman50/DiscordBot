# DiscordBot 

## Instructions to run locally 
1. Clone the repo in a directory of your choosing.
2. Run the following commands to create virtual environment```python3 -m venv .venv ```
3. Run the following commands to install the required libraries ```.venv/bin/pip3 install -r requirements.txt ```
3. Make a file named `.env`
4. Paste this line into `.env` and insert your discord bot token: ```DISCORD_TOKEN = "your token here"```
4. Run the following commands to run the bot using the virtual environment you created : ```.venv/bin/python3 bot.py ```  
5. To bring the bot down press control+ c 

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




## Instructions for AWS 
1. Create EC2 instance 
2. create Key pair name and save the file to be able to connect to the instance 
3. You must create security group to allow http port 80 and if you want to connect to the instance allow port 22 to connect to the instance. 
4. click on advanced details then go to the user data field and copy paste the following commands with consideration pasting your own discord token
```
#!/bin/bash 
sudo yum update 
sudo yum install -y git
git clone https://github.com/cs220s22/DiscordBot.git
cd DiscordBot
python3 -m venv .venv 
.venv/bin/pip3 install -r requirements.txt 
touch .env 
echo ""DISCORD_TOKEN="Enter your own Discord Token" > .env 
sudo .venv/bin/python3 bot.py 
```
## explaining the bash commands
1. Update the packages on your system
2. Installing git commands with a switch ```-y``` skips the user inputs 
3. Clone DiscordBot repo
4. Change directory to DiscordBot
5. creating virtual environment with a switch ```-m``` creeating a module 
6. going to the module and install the requirements with a switch  ```-r``` to install all the libraries in the file.
6. Create .env file
7. Write discord token key 
8. run the bot.py using virtual environment


# Technologies 
## AWS EC2 
1. https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html
2. https://dev.to/rishabk7/host-your-discord-bot-on-ec2-instance-aws-5c07

