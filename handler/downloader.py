import glob
import os
import tempfile
import yt_dlp
import subprocess

def download_yt_audio(youtube_url,tmpdir):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(tmpdir, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])
    mp3_files = glob.glob(os.path.join(tmpdir, '*.mp3'))
    if not mp3_files:
        raise RuntimeError("MP3 file was not created")
    
    return mp3_files[0] 

def download_spotify_audio(spotify_url, tmpdir):
    cmd = ['spotdl', '--output', tmpdir, '--format', 'mp3', '--bitrate', '320k', spotify_url]
    subprocess.run(cmd)
    mp3_files = glob.glob(os.path.join(tmpdir, '*.mp3'))
    if not mp3_files:
        raise RuntimeError("MP3 file was not created")
    
    return mp3_files[0] 
    
'''
youtube_url="https://youtu.be/CFjI21M9wZs?si=PERTH1LXXfbzaDNx"
spotify_url="https://open.spotify.com/track/0auX6W6oLjO9cHmx4UTaNj?si=bf2d6bbf98cc45a0"

download_yt_audio(youtube_url=youtube_url)
download_spotify_audio(spotify_url=spotify_url)'''


