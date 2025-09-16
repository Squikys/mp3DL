FROM python:3.12.11-trixie

WORKDIR /app

COPY requirements.txt ./

RUN apt update && apt install -y ffmpeg
RUN pip install -r requirements.txt

COPY . ./

CMD [ "python" ,"main.py"]