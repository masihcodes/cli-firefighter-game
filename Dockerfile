FROM python:3.10-slim


RUN apt-get update && apt-get install -y \
  curl \
  && rm -rf /var/lib/apt/lists/*


RUN curl -sLK https://github.com/tsl0922/ttyd/releases/download/1.7.4/ttyd.x86_64 -o /usr/local/bin/ttyd \
  && chmod +x /usr/local/bin/ttyd


WORKDIR /app


COPY . /app


RUN python generate_maps.py


CMD ["sh", "-c", "ttyd -p $PORT python FirefighterGame.py"]