FROM python:3.12-slim-bookworm

WORKDIR /app

COPY requirements.txt ./

RUN apt update && apt install -y ffmpeg
RUN pip install -r requirements.txt

COPY . ./

CMD [ "python" ,"main.py"]