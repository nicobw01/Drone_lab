import cv2
import recon
import time
import threading



def Camera_Conect():
    global CAMERA
    global IMG
    while True:
        cv2.imshow('Barcode/QR code reader', IMG)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    


def Capture():
    global IMG
    timeout = time.time() + 30
    while True:
        _,img = CAMERA.read()

        if time.time() < timeout:
            recon.read_barcode(img)
        else:
            print("salir")
            break

        IMG = img

        k = cv2.waitKey(1)


if __name__ == '__main__':
    CAMERA = None
    CAMERA = cv2.VideoCapture(0)
    _,IMG = CAMERA.read()
    t = threading.Thread(target = Camera_Conect, daemon= True)
    t.start()
    Capture()
    Capture()