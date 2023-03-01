import qrcode as qr
from PIL import image


# Taking User input
txt = input("Enter Text To Generate QR:\n")



# simple qr code generator
# img = qr.make(txt)
# img.save("qr.png")

# With Advance features like height, width, border, color and so on...
s1 = qr.QRCode(version=1,
               error_correction=qr.constants.ERROR_CORRECT_H,
               box_size=10, border=4)

s1.add_data(txt)
s1.make(fit=True)
img = s1.make_image(fill_color="black", back_color="white")
img.save("qr.png")
