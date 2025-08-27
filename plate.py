import cv2
import torch
import easyocr
import openpyxl
import time
from ultralytics import YOLO

# Modelleri yükleme
plate_detection_model = YOLO('Plate_detection.pt')
plate_reading_model = YOLO('Plate_reading.pt')

# EasyOCR modelini başlatma (Türkçe ve İngilizce için)
reader = easyocr.Reader(['en', 'tr'])

# Not Defteri dosyası oluşturma
notebook_file = 'plaka_bilgileri.txt'

# Excel dosyası oluşturma
excel_file = 'plaka_bilgileri.xlsx'
workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = "Plaka Bilgileri"
sheet.append(["Zaman", "Plaka"])

# Kamera başlatma
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Plaka tespiti
    results_plate = plate_detection_model(frame)
    for result in results_plate:
        boxes = result.boxes.xyxy.cpu().numpy()  # Tespit edilen nesnenin koordinatları
        for box in boxes:
            x1, y1, x2, y2 = map(int, box[:4])
            plate_img = frame[y1:y2, x1:x2]
            
            # Plaka üzerindeki yazıları EasyOCR ile tespit etme
            plate_text = reader.readtext(plate_img, detail=0, paragraph=False)
            plate_text = " ".join(plate_text)
            
            # Sonuçları terminale yazdırma
            print(f"Plaka: {plate_text}")
            
            # Not Defteri dosyasına yazma
            with open(notebook_file, 'a') as f:
                f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Plaka: {plate_text}\n")
            
            # Excel dosyasına yazma
            sheet.append([time.strftime('%Y-%m-%d %H:%M:%S'), plate_text])
            workbook.save(excel_file)
            
            # Tespit edilen plaka üzerinde dikdörtgen çizme
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
            cv2.putText(frame, plate_text, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
    
    # Görüntüyü gösterme
    cv2.imshow('Plaka Tespiti', frame)
    
    # 'q' tuşuna basarak çıkış yapma
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamera ve pencereleri kapatma
cap.release()
cv2.destroyAllWindows()
