import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=5, border=2,)
qr.add_data('https://www.linkedin.com/in/manzil-shrestha-6b0607218/')
qr.make(fit=True)
image = qr.make_image(fill_color='black', back_color='white')
image.save('linkedin_Manzil.png')
