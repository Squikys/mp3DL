FROM python:3.12-alpine3.22

WORKDIR /app

COPY requirements.txt ./

RUN apk add --no-cache ffmpeg
RUN pip install fastapi fastapi[standard] yt-dlp spotdl

COPY . ./

EXPOSE 7000
CMD [ "python" ,"main.py"]