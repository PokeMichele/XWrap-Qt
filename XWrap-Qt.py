import os
import time
import tempfile
from PIL import Image, ImageSequence


def extract_frames_from_gif(gif_path):
    with Image.open(gif_path) as gif:
        frames = [frame.copy() for frame in ImageSequence.Iterator(gif)]

    temp_folder = tempfile.mkdtemp()
    frame_paths = []
    for i, frame in enumerate(frames):
        frame_path = os.path.join(temp_folder, f'frame_{i}.jpg')
        frame = frame.convert("RGB")
        frame.save(frame_path)
        frame_paths.append(frame_path)

    return frame_paths


gif_path = input("Enter the path to the GIF file: ")
frame_paths = extract_frames_from_gif(gif_path)

while True:
    for frame_path in frame_paths:
        os.system(f'pcmanfm-qt --set-wallpaper {frame_path}')
        time.sleep(1/24)  # You can adjust the Sleep Time to control the Animation Speed
