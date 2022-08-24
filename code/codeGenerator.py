import qrcode
import barcode 
from barcode.writer import ImageWriter


def generate(code):
    img = qrcode.make(code)
    img.save("data/QRcode.png")



    my_Ean = code
    new_ean = barcode.get_barcode_class('code128')
    new_ean = new_ean(my_Ean,writer=ImageWriter())
    new_ean.save("data/BarCode")



generate('me lo fumo en pipa')