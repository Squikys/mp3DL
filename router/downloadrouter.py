import os
import shutil
import tempfile
from fastapi import BackgroundTasks, FastAPI,APIRouter, Form
from fastapi.responses import FileResponse
from handler.downloader import download_spotify_audio,download_yt_audio
from handler.checker import is_valid_spotify_track_url,is_valid_youtube_video
def cleanup_file(file_path: str):
    try:
        print(f"[DEBUG] Deleting file: {file_path}")
        os.remove(file_path)

        folder = os.path.dirname(file_path)
        print(f"[DEBUG] Deleting folder: {folder}")
        shutil.rmtree(folder)
    except Exception as e:
        print(f"[ERROR] Cleanup failed: {e}")
download_router=APIRouter(prefix="/api")

@download_router.post("/download")
def ping(background_tasks: BackgroundTasks,url:str=Form(...)):
        tmpdir=tempfile.mkdtemp()
        filepath=""
        if is_valid_spotify_track_url(url=url):
            print("spotify check")
            filepath = download_spotify_audio(url, tmpdir=tmpdir)
        elif is_valid_youtube_video(url=url):
            print("youtube check")
            filepath = download_yt_audio(url, tmpdir=tmpdir)
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