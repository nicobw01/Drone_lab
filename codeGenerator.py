import qrcode
import barcode 
from barcode.writer import ImageWriter


def generate(code):
    img = qrcode.make(code)
    img.save("QRcode.png")



    my_Ean = code
    a = barcode.get_barcode_class('code128')
    a = a(my_Ean,writer=ImageWriter())
    a.save("BarCode")



generate('Codigo 10')