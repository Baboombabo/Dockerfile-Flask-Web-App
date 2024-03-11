FROM python:latest

RUN mkdir /app

WORKDIR  /app

COPY . .

RUN pip install Flask

RUN pip install requests

EXPOSE 5001

CMD python app.py