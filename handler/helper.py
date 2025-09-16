import os
import shutil
def cleanup_file(file_path: str):
    try:
        print(f"[DEBUG] Deleting file: {file_path}")
        os.remove(file_path)

        folder = os.path.dirname(file_path)
        print(f"[DEBUG] Deleting folder: {folder}")
        shutil.rmtree(folder)
    except Exception as e:
        print(f"[ERROR] Cleanup failed: {e}")