import glob
import os
import yt_dlp
import subprocess


def download_yt_audio(youtube_url: str, tmpdir: str = "/tmp") -> str:

    os.makedirs(tmpdir, exist_ok=True)
    outtmpl = os.path.join(tmpdir, "%(title)s.%(ext)s")

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': outtmpl,
        'noplaylist': True,
        'ignoreerrors': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(youtube_url, download=True)
        if info is None:
            raise RuntimeError("Could not retrieve video information.")
        downloaded_file = ydl.prepare_filename(info)

    if downloaded_file.lower().endswith(".mp3") and os.path.exists(downloaded_file):
        return downloaded_file

    audio_files = []
    for ext in ('*.mp3', '*.m4a', '*.webm', '*.opus', '*.flac'):
        audio_files.extend(glob.glob(os.path.join(tmpdir, '**', ext), recursive=True))
    if not audio_files:
        raise RuntimeError("No audio file was created by yt-dlp")

    original_file = audio_files[0]
    mp3_file = os.path.splitext(original_file)[0] + ".mp3"

    if not original_file.lower().endswith(".mp3"):
        subprocess.run([
            'ffmpeg', '-y', '-i', original_file,
            '-q:a', '0',
            mp3_file
        ], check=True)
        return mp3_file
    else:
        return original_file


def download_spotify_audio(spotify_url: str, tmpdir: str = "/tmp") -> str:

    os.makedirs(tmpdir, exist_ok=True)

    cmd = [
        'spotdl',
        '--output', tmpdir,
        spotify_url
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"SpotDL failed:\n{result.stderr or result.stdout}")

    audio_files = []
    for ext in ('*.mp3', '*.m4a', '*.flac', '*.ogg', '*.opus', '*.webm'):
        audio_files.extend(glob.glob(os.path.join(tmpdir, '**', ext), recursive=True))

    if not audio_files:
        raise RuntimeError("No audio file was created by SpotDL")

    original_file = audio_files[0]
    mp3_file = os.path.splitext(original_file)[0] + ".mp3"

    if not original_file.lower().endswith(".mp3"):
        subprocess.run([
            'ffmpeg', '-y', '-i', original_file,
            '-q:a', '0',
            mp3_file
        ], check=True)
        return mp3_file
    else:
        return original_file
