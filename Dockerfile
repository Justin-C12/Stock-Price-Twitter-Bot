# syntax=docker/dockerfile:1
FROM python:3.9.1
ADD tweet_bot.py /
COPY requirements.txt ./ 
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
COPY . .
CMD [ "python", "./tweet_bot.py" ]

