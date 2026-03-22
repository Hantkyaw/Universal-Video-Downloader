import os
import subprocess
import sys
import time
import re
from colorama import Fore, Style, init

# Colors & Style Initialization
init(autoreset=True)
G, R, Y, C, W, B = Fore.GREEN, Fore.RED, Fore.YELLOW, Fore.CYAN, Fore.WHITE, Style.BRIGHT

def status_loading(msg):
    """အလုပ်လုပ်နေစဉ် Spinner ပြပေးမည့် function"""
    spinner = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    for i in range(10):
        sys.stdout.write(f"\r{C}[{spinner[i]}] {Y}{msg}...")
        sys.stdout.flush()
        time.sleep(0.08)
    print(f" {G}[Done]")

def banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(f"{C}{B}==================================================")
    print(f"{Y}{B}            K2 DOWNLOADER (V8.0 PRO)             ")
    print(f"{C}{B}==================================================")
    print(f"{G}  [High-Speed Engine | Multi-Bar | Loader] | K2")
    print(f"{C}{B}==================================================\n")

def run_engine(url, p_type, quality):
    # ၁။ Folder ဆောက်ခြင်း (မြင်သာအောင် spinner ပြမယ်)
    status_loading("Setting up storage and folders")
    base_dir = "/sdcard/Download/K2Downloader"
    
    # Playlist ဆိုရင် folder သီးသန့်ဆောက်ပြီး ဗီဒီယိုဆိုရင် Videos ထဲထည့်မယ်
    save_template = f"{base_dir}/%(playlist_title|Videos)s/%(title)s.%(ext)s"
    
    # ၂။ Engine Settings (Speed အမြင့်ဆုံးဖြစ်အောင် ညှိထားပါတယ်)
    # --concurrent-fragments 10 က Connections ၁၀ ခုနဲ့ ဒေါင်းမှာဖြစ်လို့ အရမ်းမြန်ပါတယ်
    cmd = [
        "yt-dlp",
        "--newline",
        "--progress",
        "--ignore-errors",
        "--no-playlist" if p_type != '1' else "--yes-playlist",
        "--buffer-size", "1M",
        "--concurrent-fragments", "10", 
        "--progress-template", "K2_DATA:%(info.title)s|%(progress._percent_str)s",
        "-o", save_template,
        "--no-mtime"
    ]

    # Quality Control
    if p_type == '1': # YouTube
        if quality == '1': cmd += ["-f", "bestvideo[height<=2160]+bestaudio/best"]
        elif quality == '2': cmd += ["-f", "bestvideo[height<=1080]+bestaudio/best"]
        elif quality == '3': cmd += ["-f", "bestvideo[height<=720]+bestaudio/best"]
        elif quality == '4': cmd += ["-x", "--audio-format", "mp3"]
        cmd += ["--merge-output-format", "mp4"]
    else: # Facebook, TikTok, Telegram, etc.
        cmd += ["-f", "bestvideo+bestaudio/best"]

    cmd.append(url)

    try:
        status_loading("K2 High-Speed Engine connecting")
        print(f"\n{Y}[*] Press Ctrl+C to stop.\n")
        
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        
        last_title = ""
        for line in process.stdout:
            if "K2_DATA:" in line:
                try:
                    # Data ခွဲထုတ်ခြင်း
                    raw_data = line.split("K2_DATA:")[1].strip()
                    title, percent_str = raw_data.rsplit('|', 1)
                    percent = float(percent_str.replace('%', '').strip())
                    
                    # Title မရှိရင် (ဥပမာ Telegram) အစားထိုးနာမည်ပေးမယ်
                    if title == "NA" or not title: title = "Social_Media_Video"

                    # သီချင်းအသစ်စရင် bar အသစ်အတွက် line ဆင်းမယ်
                    if title != last_title:
                        if last_title != "": print() 
                        print(f"{W}Downloading: {G}{title[:55]}...")
                        last_title = title
                    
                    # Progress Bar အလှဆင်ခြင်း
                    bar_len = 25
                    filled = int(bar_len * percent / 100)
                    bar = '█' * filled + '░' * (bar_len - filled)
                    
                    # Output ကို Real-time ပြခြင်း
                    sys.stdout.write(f"\r{C}  [{bar}] {percent:.1f}% {Y}[FAST]")
                    sys.stdout.flush()
                except:
                    pass
            
        process.wait()
        print(f"\n\n{G}[✔] 100% Download Completed! Check K2Downloader folder.")
    except Exception as e:
        print(f"\n{R}[!] Error: {e}")

def main():
    while True:
        banner()
        print(f"{C}[1] {W}YouTube (Video/Playlist/MP3)")
        print(f"{C}[2] {W}Facebook / Instagram")
        print(f"{C}[3] {W}TikTok / Telegram / X (Twitter)")
        print(f"{C}[4] {W}Firmware Download (Wget)")
        print(f"{R}[5] Exit")
        
        choice = input(f"\n{Y}[?] Select Option: ")
        
        if choice in ['1', '2', '3']:
            url = input(f"\n{G}[+] Paste Link Here: ").strip()
            if not url: continue
            
            q = 'best'
            if choice == '1':
                print(f"\n{C}Select Quality: [1] 4K | [2] 1080p | [3] 720p | [4] MP3")
                q = input(f"{Y}[?] Choice: ")
            
            run_engine(url, choice, q)
            input(f"\n{G}Press Enter to return to menu...")
            
        elif choice == '4':
            banner()
            fw_url = input(f"{G}[+] Paste Firmware Link: ")
            if fw_url:
                fw_dir = "/sdcard/Download/K2Downloader/Firmware"
                if not os.path.exists(fw_dir): os.makedirs(fw_dir)
                status_loading("Initializing High-Speed Wget")
                os.system(f"wget -P {fw_dir} --show-progress {fw_url}")
            input(f"\n{G}Press Enter...")
            
        elif choice == '5':
            print(f"{Y}Thank you for using K2 Downloader. Goodbye!")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{R}[!] Aborted by user.")
        sys.exit()

