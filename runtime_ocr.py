import cv2
from easyocr import Reader
l1=""
def docr_read():
    def perform_ocr_easyocr(frame, reader):
        results = reader.readtext(frame)
        text = ' '.join(result[1] for result in results)
        return text
    reader = Reader(['en'])

    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        text = perform_ocr_easyocr(frame, reader)
        cv2.imshow('Original Frame', frame)
        print('OCR Result:', text)
        l1=''.join(text)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    cap.release()
    cv2.destroyAllWindows()
    return l1







