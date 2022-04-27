FROM python:slim
WORKDIR /bot
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python3", "bot.py"]
