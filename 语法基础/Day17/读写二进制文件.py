"""
读写二进制文件

"""

def main():
    try:
        # 将1.jpg以二进制只读方式打开，读入data变量
        with open('./res/1.jpg', 'rb') as fsl:
            data = fsl.read()
            print(type(data))
        # 将1.jpg以二进制写的方式打开，写入1_copy.jpg
        with open('./res/1_copy.jpg', 'wb') as fs2:
             fs2.write(data)
    except FileNotFoundError as e:
        print(e)
    except IOError as e:
        print(e)
    print('程序执行结束')

if __name__ == '__main__':
    main()