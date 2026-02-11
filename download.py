import os

def downloader():
    os.system('clear')
    print("=== Video Downloader (YouTube/TikTok/FB) ===")
    link = input("\nPaste the video link here: ")
    
    # مسار الحفظ في مجلد التحميلات بالهاتف
    save_path = "/sdcard/Download/%(title)s.%(ext)s"
    
    print("\nStarting download... Please wait.")
    os.system(f'yt-dlp -o "{save_path}" {link}')
    
    print("\nDone! Check your Downloads folder.")

if __name__ == "__main__":
    downloader()

