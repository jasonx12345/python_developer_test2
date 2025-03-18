import subprocess
from PIL import Image, ImageDraw, ImageFont
from gtts import gTTS

# Configuration
image_path = "input.jpg"
music_file = "background.mp3"
output_video = "output.mp4"
output_audio = "voiceover.mp3"
processed_image_path = "processed_image.jpg"
captions_file = "captions.srt"
overlay_text = "This is a sample text overlay."
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
font_size = 40
duration_seconds = 5

# Process image
image = Image.open(image_path).convert("L")
draw = ImageDraw.Draw(image)
font = ImageFont.truetype(font_path, font_size)
draw.text((50, 50), overlay_text, font=font, fill="white")
image.save(processed_image_path)

# Generate voiceover
tts = gTTS(text=overlay_text, lang="en")
tts.save(output_audio)

# Create captions file
with open(captions_file, "w") as f:
    f.write("1\n00:00:00,000 --> 00:00:05,000\n" + overlay_text)

# Generate video using FFmpeg
ffmpeg_cmd = [
    "ffmpeg", "-y",
    "-loop", "1", "-i", processed_image_path,
    "-i", output_audio,
    "-i", music_file,
    "-filter_complex", "[1:a][2:a]amix=inputs=2:duration=first[a]",
    "-map", "0:v", "-map", "[a]",
    "-t", str(duration_seconds),
    "-vf", f"subtitles={captions_file}:force_style='Fontsize=24,PrimaryColour=&HFFFFFF&'",
    "-c:v", "libx264", "-c:a", "aac",
    output_video
]

subprocess.run(ffmpeg_cmd, check=True)
print("Video generation complete!")
