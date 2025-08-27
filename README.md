# License Plate Recognition System

[Also available in Turkish (Türkçe README_TR.md)](README_TR.md)

This project is a real-time license plate recognition system using computer vision and deep learning techniques. The system can detect and read license plates from camera feed, saving the results to both text and Excel files.

This system is designed to:
- Detect license plates in real-time using YOLO object detection
- Process and enhance the detected plate image for better recognition
- Read the text from the plate using OCR technology
- Store the results with timestamps for tracking and analysis

## Project Description

The system uses a combination of state-of-the-art technologies:
- **YOLO (You Only Look Once)**: For fast and accurate license plate detection
- **Image Processing**: Applies various techniques to enhance plate readability
  - Grayscale conversion
  - Noise reduction
  - Contrast enhancement
  - Perspective correction (if plate is at an angle)
- **EasyOCR**: For accurate text recognition with multi-language support

## Features

- Real-time license plate detection
- Text recognition from license plates (OCR)
- Supports both Turkish and English characters
- Saves results to text and Excel files
- Real-time visualization with bounding boxes

## Requirements

- Python 3.x
- OpenCV
- PyTorch
- EasyOCR
- Ultralytics YOLO
- OpenPyXL

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Semihkulekcioglu/Plate_detect_and_recognize_system.git
cd Plate_detect_and_recognize_system
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

3. Make sure you have the model files in your project directory:
- `Plate_detection.pt`
- `Plate_reading.pt`

## Usage

Run the main script:
```bash
python plate.py
```

The program will:
1. Start your computer's camera
2. Detect license plates in real-time
3. Read the text from detected plates
4. Save the results to:
   - `plaka_bilgileri.txt` (text file)
   - `plaka_bilgileri.xlsx` (Excel file)
5. Display the video feed with detected plates

Press 'q' to quit the program.

## Output Files

<img width="640" height="640" alt="Output_1" src="https://github.com/user-attachments/assets/450e3608-fe2c-4fa8-ad20-62c2fb40f804" />
<img width="640" height="640" alt="Output_2" src="https://github.com/user-attachments/assets/ab962fc0-b68f-436c-97aa-513ca381a7fb" />

- `plaka_bilgileri.txt`: Contains timestamp and plate text for each detection
- `plaka_bilgileri.xlsx`: Excel file with timestamp and plate text in tabular format

## Note

- The system uses YOLO (You Only Look Once) for plate detection
- EasyOCR is used for text recognition
- First run may take longer as it downloads required model files

## Contributing

Feel free to open issues or submit pull requests.
