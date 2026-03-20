import os

def downloader():
    os.system('clear')
    print("==========================================")
    print("      UNIVERSAL VIDEO DOWNLOADER (V1.1)   ")
    print("==========================================")
    
    url = input("\n[+] Please paste the video link: ")
    
    if not url:
        print("[-] Error: Link cannot be empty.")
        return

    print("\nSelect Download Quality:")
    print("-------------------------")
    print("[1] 1080p (Full HD)")
    print("[2] 720p  (HD)")
    print("[3] 360p  (Low)")
    print("[4] Music (MP3 Audio Only)")
    print("[5] Exit")
    
    choice = input("\nEnter your choice [1-5]: ")

    # Storage Path
    save_path = "/sdcard/Download/VideoDownloader/%(title)s.%(ext)s"
    os.system("mkdir -p /sdcard/Download/VideoDownloader")

    if choice == '1':
        fmt = "bestvideo[height<=1080]+bestaudio/best[height<=1080]"
    elif choice == '2':
        fmt = "bestvideo[height<=720]+bestaudio/best[height<=720] / best[height<=720]"
    elif choice == '3':
        fmt = "bestvideo[height<=360]+bestaudio/best[height<=360] / best[height<=360]"
    elif choice == '4':
        print("\n[*] Downloading & Converting to MP3... Please wait.")
        # --newline နဲ့ --progress က အတန်းလေးပြေးတာကို သေချာမြင်ရစေတယ်
        os.system(f'yt-dlp -x --audio-format mp3 --newline --progress -o "{save_path}" {url}')
        print("\n[✔] Audio download completed successfully!")
        return
    elif choice == '5':
        print("\nGoodbye!")
        return
    else:
        print("[-] Invalid selection. Please try again.")
        return

    print(f"\n[*] Starting download... Quality: {choice}")
    # --newline --progress က အတန်းလေးပြေးတာကို ပြပေးမှာပါ
    os.system(f'yt-dlp -f "{fmt}" --merge-output-format mp4 --no-mtime --newline --progress -o "{save_path}" {url}')
    print("\n[✔] Download completed! Please check 'Download/VideoDownloader' folder.")

if __name__ == "__main__":
    downloader()

