import re
import subprocess

def is_spotify_track_available(url: str) -> bool:
    cmd = ["spotdl", "save", url, "--dry-run"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode == 0

def is_valid_spotify_track_url(url):
    """
    Checks if the given URL is a valid Spotify track URL.
    """
    pattern = r'^https://open\.spotify\.com/track/[A-Za-z0-9]{22}(?:\?si=[A-Za-z0-9]+)?$'
    if re.match(pattern, url) is not None :
        return True
    elif re.match(pattern, url) is not None and is_spotify_track_available(url=url) :
        return True
    else : return False

import yt_dlp

def is_valid_youtube_video(url: str) -> bool:
    try:
        with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
            info = ydl.extract_info(url, download=False)
            if info and info.get("is_live"):
                return False  # It's a live video
            return True
    except yt_dlp.utils.DownloadError:
        return False
    except Exception as e:
        print(f"[ERROR] {e}")
        return False

