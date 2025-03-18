Python Developer Test 2: FFmpeg and Pillow Video Generator

This script generates a short video from an image using Pillow for image processing and FFmpeg for video generation. The video includes text overlay, a grayscale transformation, background music, captions, and a generated voiceover narration using gTTS.

Requirements
------------
- Python 3.x
- Pillow for image processing
- gTTS for text-to-speech narration
- FFmpeg installed on your system
- A TrueType font file (for text overlay)

Installation
------------
1. Install Python dependencies:
   pip install pillow gtts

2. Install FFmpeg:
   - Linux:
     sudo apt install ffmpeg
   - macOS:
     brew install ffmpeg
   - Windows:
     Download FFmpeg from https://ffmpeg.org/download.html and add it to your PATH.

Usage
-----
1. Place your input image (e.g., input.jpg) and background music file (e.g., background.mp3) in the same directory as the script.
2. Edit the configuration section in the script to adjust paths and text (e.g., image_path, music_file, overlay_text, font_path).
3. Run the script:
   python video_generator.py
4. The script will generate:
   - processed_image.jpg – The transformed image with text overlay.
   - voiceover.mp3 – The generated voiceover narration.
   - captions.srt – The subtitles file with captions.
   - output.mp4 – The final video with background music, captions, and voiceover.
   
Customization
-------------
- overlay_text: Modify this to change the text overlay and narration.
- duration_seconds: Adjust this to set the video duration.
- font_path and font_size: Customize the font for text overlay.

Troubleshooting
---------------
- FFmpeg not found: Ensure FFmpeg is installed and added to your system PATH.
- Font issues: Verify the specified font file exists on your system; update font_path if needed.
- Audio sync problems: Adjust FFmpeg filter parameters if the voiceover and music are not synchronized.
