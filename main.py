"""
Autonomous Lane Detection

Usage:
    main.py [--video --image] [--all] INPUT_PATH 

Options:

-h --help                               show this screen
--video                                 process video file
--image                                 process image file
--all                                   output all results (complete, sliding window, and bird's eye)
"""

import numpy as np
import matplotlib.image as mpimg
import cv2
from docopt import docopt
from moviepy.editor import VideoFileClip
from Thresholding import Thresholding
from PerspectiveTransformation import PerspectiveTransformation
from LaneLines import LaneLines
import os

class FindLaneLines:
    def __init__(self):
        """ Init Application"""
        self.thresholding = Thresholding()
        self.transform = PerspectiveTransformation()
        self.lanelines = LaneLines()

    def sliding_window(self, img):
        out_img = np.copy(img)
        out_img = self.transform.forward(out_img)
        out_img = self.thresholding.forward(out_img)
        out_img = self.lanelines.draw_sliding_windows(out_img)
        return out_img
    
    def complete(self, img):
        out_img = np.copy(img)
        img = self.transform.forward(img)
        img = self.thresholding.forward(img)
        img = self.lanelines.draw_lanes(img)
        img = self.transform.backward(img)

        out_img = cv2.addWeighted(out_img, 1, img, 0.6, 0)
        out_img = self.lanelines.plot(out_img)
        return out_img
    
    def birds_eye(self, img):
        out_img = np.copy(img)
        out_img = self.transform.forward(out_img)
        img = self.transform.forward(img)
        img = self.thresholding.forward(img)
        img = self.lanelines.draw_lanes(img)

        out_img = cv2.addWeighted(out_img, 1, img, 0.6, 0)
        return out_img

    def process_image(self, input_path):
        img = mpimg.imread(input_path)
        out_img = self.complete(img)
        mpimg.imsave(output_file_path(input_path, "_complete", "output_images"), out_img)

    def process_image_all(self, input_path):
        img = mpimg.imread(input_path)
        complete_img = self.complete(img)
        mpimg.imsave(output_file_path(input_path, "_complete", "output_images"), complete_img)
        sliding_window_img = self.sliding_window(img)
        mpimg.imsave(output_file_path(input_path, "_sliding_window", "output_images"), sliding_window_img)
        birds_eye_img = self.birds_eye(img)
        mpimg.imsave(output_file_path(input_path, "_birds_eye", "output_images"), birds_eye_img)

    def process_video(self, input_path):
        clip = VideoFileClip(input_path)
        out_clip = clip.fl_image(self.complete)
        out_clip.write_videofile(output_file_path(input_path, "_complete", "output_videos"), audio=False)

    def process_video_all(self, input_path):
        clip = VideoFileClip(input_path)
        complete_clip = clip.fl_image(self.complete)
        complete_clip.write_videofile(output_file_path(input_path, "_complete", "output_videos"), audio=False)
        sliding_window_clip = clip.fl_image(self.sliding_window)
        sliding_window_clip.write_videofile(output_file_path(input_path, "_sliding_window", "output_videos"), audio=False)
        birds_eye_clip = clip.fl_image(self.birds_eye)
        birds_eye_clip.write_videofile(output_file_path(input_path, "_birds_eye", "output_videos"), audio=False)

def main():
    args = docopt(__doc__)
    input = args['INPUT_PATH']

    findLaneLines = FindLaneLines()
    if args['--video'] and args['--all']:
        findLaneLines.process_video_all(input)
    elif args['--image'] and args['--all']:
        findLaneLines.process_image_all(input)
    elif args['--video']:
        findLaneLines.process_video(input)
    elif args['--image']:
        findLaneLines.process_image(input)

def output_file_path(input_path, suffix, directory):
    base_name, ext = os.path.splitext(os.path.basename(input_path))
    new_directory = os.path.join(directory, base_name)
    os.makedirs(new_directory, exist_ok=True)
    new_file_name = f"{base_name}{suffix}{ext}"
    return os.path.join(new_directory, new_file_name)

if __name__ == "__main__":
    main()