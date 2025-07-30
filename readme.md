#### Prerequisites `ffmpeg`, `python`

#### To install required modules run this command
##### For Linux
```bash
python -m venv venv
source venv/bin/activate
pip -r requirements.txt
```
##### For Windows
```bash
python -m venv venv
.\venv\Scripts\activate
pip -r requirements.txt
```
#### To run the app
##### For Linux
```bash
source venv/bin/activate
python main.py
```
##### For Windows
```bash
.\venv\Scripts\activate
python main.py
```
##### you can access the app by going to url `localhost:7000`
#### If you have `Docker` installed, then use
```bash
docker compose up
```
#### to run the app