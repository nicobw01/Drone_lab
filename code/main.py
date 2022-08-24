import cv2
import recon
import time
import threading


#  Function Camera ON 
# TODO Explanation Function
def Camera_Conect():
    global CAMERA 
    global IMG
    while True:
        cv2.imshow('Barcode/QR code reader', IMG)
        if not CAPTURE_ON:
            _,IMG = CAMERA.read()
        if cv2.waitKey(1) & 0xFF == 27:
            break
    

# Recon QRCode
# TODO Explanation Function
def Capture(color):
    global IMG
    global CAPTURE_ON

    CAPTURE_ON = True
    timeout = time.time() + 10

    while True:
        _,img = CAMERA.read()

        if time.time() < timeout:
            recon.read_barcode(img,color)
        else:
            print("salir")
            break

        IMG = img


    CAPTURE_ON = False



def Timer():
    timeout = time.time() + 10
    i=0
    print("Estoy volando ")
    while time.time() < timeout:
        print(f"secs[{i}]")
        i+=1


if __name__ == '__main__':
    CAMERA = None
    CAMERA = cv2.VideoCapture(0)
    CAPTURE_ON = False
    _,IMG = CAMERA.read()
    thread_Camera = threading.Thread(target = Camera_Conect, daemon= True)
    thread_Camera.start()
    Capture((255,0,0))
    Timer()
    Capture((0,255,0))