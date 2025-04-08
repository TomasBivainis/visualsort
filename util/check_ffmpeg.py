import os
import subprocess
import platform
import urllib.request
import zipfile

def is_ffmpeg_installed():
    """Check if FFMPEG is installed and accessible."""
    try:
        subprocess.run(["ffmpeg", "-version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except (FileNotFoundError, subprocess.CalledProcessError):
        return False

def download_ffmpeg():
    """Download and extract FFMPEG for the current platform."""
    system = platform.system().lower()
    ffmpeg_url = ""

    if system == "darwin":  # macOS
        ffmpeg_url = "https://evermeet.cx/ffmpeg/ffmpeg.zip"
    elif system == "windows":
        ffmpeg_url = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
    elif system == "linux":
        ffmpeg_url = "https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz"
    else:
        raise OSError("Unsupported operating system.")

    print("Downloading FFMPEG...")
    ffmpeg_zip_path = "ffmpeg_download.zip"
    urllib.request.urlretrieve(ffmpeg_url, ffmpeg_zip_path)

    print("Extracting FFMPEG...")
    if system == "linux":
        import tarfile
        with tarfile.open(ffmpeg_zip_path, "r:xz") as tar:
            tar.extractall("./ffmpeg")
    else:
        with zipfile.ZipFile(ffmpeg_zip_path, "r") as zip_ref:
            zip_ref.extractall("./ffmpeg")

    os.remove(ffmpeg_zip_path)
    print("FFMPEG downloaded and extracted.")

    # Set the environment variable to point to the downloaded FFMPEG binary
    os.environ["IMAGEIO_FFMPEG_EXE"] = os.path.abspath("./ffmpeg/ffmpeg")

def ensure_ffmpeg():
    """Ensure FFMPEG is installed and available."""
    if not is_ffmpeg_installed():
        print("FFMPEG not found. Downloading...")
        download_ffmpeg()
    else:
        print("FFMPEG is already installed.")

if __name__ == "__main__":
    ensure_ffmpeg()