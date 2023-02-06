import os
import time
from pathlib import Path
from PIL import Image, ImageSequence

# Create the TMP_DIR if it doesn't exist
TMP_DIR = Path(os.environ.get("TMPDIR", "/tmp")) / "xwrap-qt"
TMP_DIR.mkdir(parents=True, exist_ok=True)

# Extract frames from the GIF file and save them to TMP_DIR
def extract_frames_from_gif(gif_path):
    gif = Image.open(gif_path)
    frame_paths = [TMP_DIR / f"frame_{i}.jpeg" for i, frame in enumerate(ImageSequence.Iterator(gif))]
    for frame, frame_path in zip(ImageSequence.Iterator(gif), frame_paths):
        frame = frame.convert("RGB")
        frame.save(frame_path, "JPEG")
    return frame_paths

# Set the wallpaper using pcmanfm-qt
def set_wallpaper(frame_path):
    os.system(f"pcmanfm-qt --set-wallpaper {frame_path}")

def main(gif_path, sleep_time):
    frame_paths = extract_frames_from_gif(gif_path)
    while True:
        for frame_path in frame_paths:
            set_wallpaper(frame_path)
            time.sleep(sleep_time)

if __name__ == "__main__":
    config_path = Path(__file__).parent / "XWrap-Qt.conf"
    if config_path.exists():
        with open(config_path) as f:
            gif_path = f.readline().strip()
            sleep_time = float(f.readline().strip())
    else:
        print("Config File not found, Creating a new one...")
        gif_path = input("Enter the Path to the GIF File: ")
        sleep_time = float(input("Enter the Sleep Time (in Seconds) Between Frames: "))
        with open(config_path, "w") as f:
            f.write(f"{gif_path}\n{sleep_time}")
    main(gif_path, sleep_time)
