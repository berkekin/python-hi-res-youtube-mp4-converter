from pytube import YouTube
import os
from tqdm import tqdm  # İlerleme çubuğu için tqdm kütüphanesini kullanın

# YouTube video URL'si
video_url = 'https://youtu.be/qgn_Wngf4wM'  # İndirmek istediğiniz video URL'sini buraya yazın

def get_highest_resolution_stream(yt):
    """
    YouTube videosunun en yüksek çözünürlüğe sahip akışını döndürür.
    """
    streams = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()
    return streams.first()

# YouTube nesnesi oluştur
yt = YouTube(video_url)

# Video başlığını al
video_title = yt.title

# İndirme klasörü yolu
download_folder = r'C:\Users\ekinz\OneDrive\Masaüstü\python indirilenler'

# İndirme tarihi ve saatini alarak benzersiz bir dosya adı oluştur
download_file = os.path.join(download_folder, f"{video_title} - {yt.publish_date.strftime('%Y-%m-%d %H-%M-%S')}.mp4")

try:
    # En yüksek çözünürlükteki video akışını al
    video_stream = get_highest_resolution_stream(yt)
    
    if video_stream:
        # Videoyu indirme işlemi
        video_stream.download(output_path=download_folder, filename=video_title)
        print(f"Video başarıyla indirildi: {download_file}")

        # İndirilen video hakkında bilgi veren bir rapor oluştur
        report = f"Video Başlığı: {video_title}\nİndirilen Dosya Yolu: {download_file}"
        with open('indirme_raporu.txt', 'w') as f:
            f.write(report)
        print("İndirme raporu oluşturuldu: indirme_raporu.txt")

    else:
        print("İndirilebilir video akışı bulunamadı.")

except Exception as e:
    print(f"Hata oluştu: {str(e)}")
