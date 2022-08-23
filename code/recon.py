import cv2
from pyzbar import pyzbar
import json

def read_barcode(frame):
    barcodes = pyzbar.decode(frame)

    for barcode in barcodes:
        x, y , w, h = barcode.rect

        #1

        barcode = barcode.data.decode('utf-8')
        cv2.rectangle(frame, (x,y),(x+w, y+h), (0,140,0), 2)

        #2

        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, barcode, (x + 6, y - 6), font, 2.0, (255, 50, 50), 1) 

    return barcodes




def main(): #1
    camera = cv2.VideoCapture(0)
    ret,frame = camera.read() #2
    while ret:
        ret, frame = camera.read()
        read_barcode(frame)
        cv2.imshow('Barcode/QR code reader', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break 
    
    #3
    camera.release()
    cv2.destroyAllWindows()


    
    
if __name__ == '__main__':
    main()