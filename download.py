import yt_dlp
import os

def unduh_media():
    print("=== PENGUNDUH MEDIA OTOMATIS ===")
    url = input("Masukkan URL video (YouTube, dll): ")
    
    # Lokasi penyimpanan: Folder 'Download' di memori internal HP kamu
    folder_tujuan = '/sdcard/Download/'
    
    # Konfigurasi yt-dlp
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best', # Ambil kualitas terbaik
        'outtmpl': os.path.join(folder_tujuan, '%(title)s.%(ext)s'), # Format nama file
        'merge_output_format': 'mp4', # Gabungkan jadi format MP4
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
