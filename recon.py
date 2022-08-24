import cv2
# from djitellopy import tello
from pyzbar import pyzbar
import json

# dron = tello.Tello()
# dron.connect()
# dron.streamon()

data = {}
data['barcodes'] = []
TEMPCODE = "null"


def read_barcode(frame,qr):
    global TEMPCODE
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y , w, h = barcode.rect
        #1
        barcode_info = barcode.data.decode('utf-8')
        if barcode_info == "mi codigo qr":
            if TEMPCODE == "null":
                TEMPCODE = {'x':x,'y':y,'w':x + w,'h':y + h,'color':(255,0,0),'border':2}

                # cv2.rectangle(frame, (x, y),(x+w, y+h), (255, 0, 0), 2)
                cv2.rectangle(frame, (TEMPCODE['x'], TEMPCODE['y']),(TEMPCODE['w'], TEMPCODE['h']), TEMPCODE['color'], TEMPCODE['border'])
                
            #2
                data['barcodes'].append({
                'pos': (x,y),
                'size': (x+w, y+h),
                'info': barcode.data.decode('utf-8')
                })
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, barcode_info, (x + 6, y - 6), font, 2.0, (50, 50, 50), 1) #3
            # with open("barcode_result.txt", mode ='w') as file:
    
    if TEMPCODE is not "null":        #     file.write("Recognized Barcode:" + barcode_info)
        cv2.rectangle(frame, (TEMPCODE['x'], TEMPCODE['y']),(TEMPCODE['w'], TEMPCODE['h']), TEMPCODE['color'], TEMPCODE['border'])
        
    
    

    return qr

camera = cv2.VideoCapture(0)
ret,frame = camera.read()


def main(): #1
    global TEMPCODE
    ret, frame = camera.read() #2
    while ret:
        ret, frame = camera.read()
        read_barcode(frame,TEMPCODE)
        cv2.imshow('Barcode/QR code reader', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break #3        
    with open('data.json', 'w') as file:
        json.dump(data, file, indent = 4)
    camera.release()
    cv2.destroyAllWindows()#4


    
    
if __name__ == '__main__':
    main()