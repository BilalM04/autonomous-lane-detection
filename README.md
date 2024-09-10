# Autonomous Lane Detection

This project implements a lane detection system using OpenCV to process images and videos for identifying lane markings. By transforming the camera’s view and applying advanced image processing techniques, the system accurately detects lanes, even in challenging conditions like curves. It also offers multiple visualizations, including detected lanes, sliding windows, and a bird’s-eye view, making it a versatile tool for autonomous driving research.

## Standard Lane Detection

The standard lane detection view displays the detected lane markings, direction arrows indicating the lane's curvature, the vehicle's center offset, and the calculated curve radius for accurate lane tracking.

https://github.com/user-attachments/assets/ac170b0d-3898-4ae4-ba7d-5ed523caaf4f

## Bird's Eye View

The bird's-eye view provides a top-down perspective of the road, highlighting the lane lines for better visualization of the lane's structure.

https://github.com/user-attachments/assets/c69d7890-56bc-43bf-93b0-06a28e5db923

## Sliding Window View

The sliding window view shows the detection process, using windows that track the lane markings along the road, ensuring consistent lane detection throughout the image.

https://github.com/user-attachments/assets/758cde22-d7d8-4a64-a873-aaf29a553a44

## Technologies Used

- **Python:** Used as the primary programming language for implementing the lane detection algorithm.
- **OpenCV:** For image and video processing, including perspective transformation and lane detection.
- **NumPy:** To perform matrix operations for transformations and measurements.
- **Matplotlib:** For visualizing intermediate steps and final output.
- **MoviePy:** To handle video processing, including reading and writing video files.
- **Docopt:** For command-line argument parsing. 

## Lane Detection Workflow

1. **Image/Video Capture**
   - In this step, frames are captured from a video stream (e.g., a dashboard camera) or single images are loaded for processing. Each frame or image serves as the input to the lane detection algorithm.
2. **Perspective Transformation**
   - This step involves transforming the camera's point of view into a bird’s-eye view. It allows you to see the road from a top-down perspective, making it easier to detect and analyze lane lines.
3. **Thresholding**
   - Here, the image is filtered to isolate the most important features, such as lane lines. Using techniques like color thresholding or gradient thresholding, unnecessary parts of the image are filtered out to highlight the lane region.
4. **Detecting Lanes**
   - Lane detection is carried out using the sliding window method and Canny edge detection. Canny edge detection helps identify the edges within the image, which are typically the lane boundaries. The sliding window technique is then used to detect and follow these lines along the lanes, ensuring accurate lane marking detection even when the road curves.
5. **Calculating Measurements**
    - After detecting the lanes, measurements such as the lane's curvature radius, the direction of the curve (left or right), and the vehicle’s offset from the center of the lane are calculated. These metrics help understand the road structure and assist in vehicle alignment.

## Project Structure

- `main.py`: Entry point of the lane detection system.
- `Thresholding.py`: Contains code for image thresholding to identify lane lines.
- `PerspectiveTransformation.py`: Code for transforming the image to a bird's eye view.
- `LaneLines.py`: Contains code for detecting and visualizing the lane lines.
- `input_images/`: Contains sample input images for the program.
- `input_videos/`: Contains sample input videos for the program.
- `output_images/`: Stores output images processed by the program.
- `output_videos/`: Stores output videos processed by the program.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/BilalM04/autonomous-lane-detection.git
   ```
2. Navigate to the project directory:
   ```bash
   cd autonomous-lane-detection
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application through the command line:

```bash
python main.py [--video | --image] [--all] INPUT_PATH
```

### Options

- `--video`: Process a video file.
- `--image`: Process an image file.
- `--all`: Output all results (lane detection, sliding window, and bird's eye view).

### Example commands

1. Process a video with all visualizations:
   ```bash
   python main.py --video ./input_videos/short_video.mp4
   ```
2. Process an image with all visualizations:
   ```bash
   python main.py --image ./input_images/straight_lines1.jpg
   ```

### Results

The resulting outputs are available in the `output_images/` and `output_videos/` directories.





