"""
用myqr库制作二维码

"""
from MyQR import myqr
import os
from PIL import Image, ImageDraw, ImageFont

# 图片背景二维码,如使用gif背景，则可以生成动态背景效果

def img_code():
    myqr.run(words='https://share.mubu.com/doc/Mp6y7cWVPr',
             # 设置容错率为最高
             version=1,
             # 控制纠错水平,范围是L、M、Q、H,从左到右依次升高
             level='H',
             # 背景图
             picture='./res/img/3.jpg',
             # 彩色二维码
             colorized=True,
             # 用以调节图片的对比度，1.0标识原始图片，更小的值表示更低对比度，更大反之，默认为1.0
             contrast=1.0,
             # 用来调节图片的亮度，其余用法和取值同上
             brightness=1.0,
             # 保存文件的名字，模式可以是jpg，png，bmp，gif
             save_name='QRCode1.png',
             # 保存位置
             save_dir=os.getcwd() +'/res/img')

def draw():
    img = Image.open('./res/img/QRCode1.png')
    w, h = img.size
    txt = '撒野'
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('./res/font/SimHei.ttf', 26)
    draw.text((w/2-100,10), txt, (0,0,0), font=font)
    img.save('./res/img/QRCode2.png')

if __name__ == '__main__':
    img_code()
    draw()
