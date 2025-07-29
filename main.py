import yt_dlp
import subprocess

def download_yt_audio(youtube_url, output_path='.'):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

def download_spotify_audio(spotify_url, output_path='.'):
    cmd = ['spotdl', '--output', output_path, spotify_url]
    subprocess.run(cmd)

youtube_url="https://youtu.be/CFjI21M9wZs?si=PERTH1LXXfbzaDNx"
spotify_url="https://open.spotify.com/track/0auX6W6oLjO9cHmx4UTaNj?si=bf2d6bbf98cc45a0"

download_yt_audio(youtube_url=youtube_url)
download_spotify_audio(spotify_url=spotify_url)


