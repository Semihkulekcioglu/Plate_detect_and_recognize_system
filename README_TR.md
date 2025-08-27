# Plaka Tanıma Sistemi

[Also available in English (İngilizce README.md)](README.md)

Bu proje, bilgisayarlı görü ve derin öğrenme teknikleri kullanarak gerçek zamanlı plaka tanıma yapan bir sistemdir. Sistem, kamera görüntüsünden plakaları tespit edebilir ve okuyabilir, sonuçları hem metin hem de Excel dosyalarına kaydeder.

Bu sistem şunları yapacak şekilde tasarlanmıştır:
- YOLO nesne tespiti kullanarak gerçek zamanlı plaka tespiti
- Daha iyi tanıma için tespit edilen plaka görüntüsünü işleme ve iyileştirme
- OCR teknolojisi ile plakadaki metni okuma
- Takip ve analiz için sonuçları zaman damgalarıyla saklama

## Proje Açıklaması

Sistem, en son teknolojilerin bir kombinasyonunu kullanır:
- **YOLO (You Only Look Once)**: Hızlı ve doğru plaka tespiti için
- **Görüntü İşleme**: Plaka okunabilirliğini artırmak için çeşitli teknikler uygular
  - Gri tonlamaya dönüştürme
  - Gürültü azaltma
  - Kontrast iyileştirme
  - Perspektif düzeltme (plaka açılı ise)
- **EasyOCR**: Çoklu dil desteği ile doğru metin tanıma için

## Özellikler

- Gerçek zamanlı plaka tespiti
- Plakalardan metin okuma (OCR)
- Türkçe ve İngilizce karakterleri destekler
- Sonuçları metin ve Excel dosyalarına kaydetme
- Gerçek zamanlı görselleştirme ve çerçeveleme

## Gereksinimler

- Python 3.x
- OpenCV
- PyTorch
- EasyOCR
- Ultralytics YOLO
- OpenPyXL

## Kurulum

1. Projeyi klonlayın:
```bash
git clone https://github.com/Semihkulekcioglu/Plate_detect_and_recognize_system.git
cd Plate_detect_and_recognize_system
```

2. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

3. Model dosyalarının proje dizininizde olduğundan emin olun:
- `Plate_detection.pt`
- `Plate_reading.pt`

## Kullanım

Ana betiği çalıştırın:
```bash
python plate.py
```

Program şunları yapacaktır:
1. Bilgisayarınızın kamerasını başlatır
2. Gerçek zamanlı olarak plakaları tespit eder
3. Tespit edilen plakalardan metni okur
4. Sonuçları şu dosyalara kaydeder:
   - `plaka_bilgileri.txt` (metin dosyası)
   - `plaka_bilgileri.xlsx` (Excel dosyası)
5. Tespit edilen plakalarla birlikte video görüntüsünü gösterir

Programdan çıkmak için 'q' tuşuna basın.

## Çıktı Dosyaları

- `plaka_bilgileri.txt`: Her tespit için zaman damgası ve plaka metnini içerir
- `plaka_bilgileri.xlsx`: Zaman damgası ve plaka metnini tablo formatında içeren Excel dosyası

## Not

- Sistem plaka tespiti için YOLO (You Only Look Once) kullanır
- Metin tanıma için EasyOCR kullanılır
- İlk çalıştırma, gerekli model dosyalarını indireceği için daha uzun sürebilir

## Katkıda Bulunma

Sorun bildirimleri veya katkı istekleri için issues ve pull request'leri kullanabilirsiniz.

