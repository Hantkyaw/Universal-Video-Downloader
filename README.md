# 🚀 K2 Mobile Downloader (V2.0)
**Developed by:** Khant Kyaw Thu (K2 Mobile)

The most reliable and professional CLI video downloader for Termux. Download your favorite content from YouTube, TikTok, Facebook, and more with high-speed performance and smart file organization.

## ✨ Advanced Features
- 📺 **Multi-Platform Support:** Works with YouTube, TikTok, Facebook, and 1000+ other sites.
- 🎬 **Quality Selection:** Choose from 1080p (Full HD), 720p (HD), or 360p (SD).
- 🎵 **High-Fidelity Audio:** Dedicated MP3 conversion with 320kbps output quality.
- 📂 **Auto-Playlist Download:** Paste a playlist link and download everything at once.
- 📁 **Smart Storage:** Files are automatically sorted into `/sdcard/Download/K2_Downloads`.
- 📊 **Real-time Progress:** Clean UI with a dynamic progress bar and speed tracking.

## 📥 Quick Installation

Copy and paste these commands in Termux to get started:

```bash
# Update system and install dependencies
pkg update && pkg upgrade -y
pkg install git python ffmpeg nodejs-lts -y

# Install the downloader engine
pip install yt-dlp

# Clone the repository
git clone [https://github.com/Hantkyaw/Universal-Video-Downloader.git](https://github.com/Hantkyaw/Universal-Video-Downloader.git)
cd Universal-Video-Downloader

# Run the tool
python k2dl.py
