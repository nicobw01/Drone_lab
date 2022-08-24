from djitellopy import Tello
import cv2



tello = Tello()

tello.connect()

tello.streamon()


def ShowCam():
    img = tello.get_frame_read().frame
    img = cv2.resize(img,(700,640))
    return img