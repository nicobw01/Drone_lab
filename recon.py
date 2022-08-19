import cv2
# from djitellopy import tello
from pyzbar import pyzbar
import json

# dron = tello.Tello()
# dron.connect()
# dron.streamon()

data = {}
data['barcodes'] = []
barcodesGlobal=[]


def read_barcode(frame):
    barcodes = pyzbar.decode(frame)
    
    for barcode in barcodes:
        x, y , w, h = barcode.rect
        if barcode not in barcodesGlobal:
            barcodesGlobal.append(barcode)
        #1
        barcode_info = barcode.data.decode('utf-8')
        cv2.rectangle(frame, (x, y),(x+w, y+h), (255, 0, 0), 2)

        #2
        font = cv2.FONT_HERSHEY_DUPLEX

        cv2.putText(frame, barcode_info, (x + 6, y - 6), font, 2.0, (50, 50, 50), 1) #3
        # with open("barcode_result.txt", mode ='w') as file:
        #     file.write("Recognized Barcode:" + barcode_info)
    

    return barcodes

camera = cv2.VideoCapture(0)
ret,frame = camera.read()


def main(): #1
    
    ret, frame = camera.read() #2
    while ret:
        ret, frame = camera.read()
        read_barcode(frame)
        cv2.imshow('Barcode/QR code reader', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break #3
    for barcode in barcodesGlobal:
        x, y , w, h = barcode.rect
        data['barcodes'].append({
            'pos': (x,y),
            'size': (x+w, y+h),
            'info': barcode.data.decode('utf-8')
        })
    with open('data.json', 'w') as file:
        json.dump(data, file, indent = 4)
    camera.release()
    cv2.destroyAllWindows()#4
    
    
if __name__ == '__main__':
    main()