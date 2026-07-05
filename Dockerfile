FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
  ttyd \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

RUN python generate_maps.py

CMD ["sh", "-c", "ttyd -p $PORT python FirefighterGame.py"]