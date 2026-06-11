import yt_dlp
import os

def unduh_media():
    print("=== PENGUNDUH MEDIA OTOMATIS (V2) ===")
    url = input("Masukkan URL video (YouTube, TikTok, IG, dll): ")
    
    folder_tujuan = '/sdcard/Download/'
    
    # Konfigurasi sakti untuk mengelabui server ketat seperti TikTok & IG
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best', 
        'outtmpl': os.path.join(folder_tujuan, '%(title)s.%(ext)s'), 
        'merge_output_format': 'mp4',
        
        # TRIK MENEMBUS BLOKIR:
        # 1. Menyamar sebagai browser Chrome Android/Windows asli (User-Agent)
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        # 2. Mengabaikan cek sertifikat SSL yang sering bikin error di Termux
        'nocheckcertificate': True,
        # 3. Paksa coba ulang otomatis kalau koneksi mendadak diputus server
        'retries': 10,
        'fragment_retries': 10,
    }
    
    print("\nSedang mengunduh... Mohon tunggu sebentar.")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("\n[SUKSES] Video berhasil diunduh dan disimpan di folder Download HP kamu!")
    except Exception as e:
        print(f"\n[ERROR] Terjadi kesalahan: {e}")

if __name__ == '__main__':
    unduh_media()

