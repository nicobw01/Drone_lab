import cv2
import qrcode

img = qrcode.make('mi codigo qr')
type(img)  # qrcode.image.pil.PilImage
img.save("some_file.png")


