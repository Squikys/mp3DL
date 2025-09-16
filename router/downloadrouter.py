import os
import shutil
import tempfile
from fastapi import BackgroundTasks, FastAPI,APIRouter, Form
from fastapi.responses import FileResponse
from handler.downloader import download_spotify_audio,download_yt_audio
from handler.checker import is_valid_spotify_track_url,is_valid_youtube_video
from handler.helper import cleanup_file
download_router=APIRouter(prefix="/api")

@download_router.post("/download")
def ping(background_tasks: BackgroundTasks,url:str=Form(...),bitrate:str=Form(...)):
        tmpdir=tempfile.mkdtemp()
        filepath=""
        if is_valid_spotify_track_url(url=url):
            print("spotify check")
            quality=0
            if bitrate=="128":quality=9
            elif bitrate=="192": quality=6
            elif bitrate=="256": quality=3
            elif bitrate=="320":quality=0
            filepath = download_spotify_audio(spotify_url=url, tmpdir=tmpdir,Bitrate=str(quality))
        elif is_valid_youtube_video(url=url):
            print("youtube check")
            filepath = download_yt_audio(youtube_url=url, tmpdir=tmpdir,Bitrate=bitrate)
        else :
             return{"response":"invalid URL"}
        

        # Confirm file exists
        if not os.path.isfile(filepath):
            raise RuntimeError(f"File at path {filepath} does not exist.")

        filename = os.path.basename(filepath)
        print(f"Sending file: {filename}")
        print(f"Full path: {filepath}")
        background_tasks.add_task(cleanup_file, filepath)

        return FileResponse(
            path=filepath,
            filename=filename,
            media_type="audio/mpeg",
            background=background_tasks
        )