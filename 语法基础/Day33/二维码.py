"""
二维码

"""

import qrcode
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=8, border=4)
qr.add_data('Love means never having to say you’re sorry.')
img = qr.make_image()
img.save('./res/img/code.png')

qr.add_data('https://www.baidu.com')
img1 = qr.make_image(fill_color='rgb(254,135,66)',
                     back_color='rgb(198,177,190)')
img1.save('./res/img/code1.png')