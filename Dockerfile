FROM python:slim 
# This line sets the docker image this contatiner will be based on. I picked it so python would already be installed
WORKDIR /bot
# This line sets the work directory inside the container to /bot. This is mostly for organization purposes  
COPY requirements.txt requirements.txt
# Copies the requirements to the container
RUN pip install -r requirements.txt
# installs the python requirements (-r stands for requirements), I didn't do this in a virtual 
# enviorement because we are already in a known state inside the docker container
COPY . .
# Copys the rest of the files in the current directory to the container
CMD ["python3", "bot.py"]
# Runs the bot
