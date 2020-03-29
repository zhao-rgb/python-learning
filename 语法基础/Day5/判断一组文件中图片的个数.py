"""
判断一组文件中图片的个数

"""

def count_iamge(file_list):
    """
    判断一组文件中图片的个数
    :param file_list: 文件列表

    :return:图片文件数量
    """
    count = 0
    for file in file_list:
        if file.endswith('.png') or file.endswith('.jpg') or \
            file.endswith('webp') or file.endswith('bmp'):
            count = count + 1
    return count

# 调用函数
img_list = ['image.jpg','images.png','1.webp','2.mp3','3.bmp','4.doc']
result = count_iamge(img_list)
print('一共有', result, '个图片文件')