import cv2
from moviepy.editor import VideoClip
import numpy as np

# Fungsi untuk menghasilkan frame animasi
def make_frame(t):
    width, height = 640, 480
    img = np.zeros((height, width, 3), dtype=np.uint8)
    img.fill(255)
    radius = int(100 + 100 * np.sin(2 * np.pi * t))
    cv2.circle(img, (320, 240), radius, (0, 0, 255), -1)
    return img

# Membuat objek VideoClip dari fungsi make_frame
animation = VideoClip(make_frame, duration=5)

# Menyimpan animasi sebagai file video
animation.write_videofile("output.mp4", fps=30)
