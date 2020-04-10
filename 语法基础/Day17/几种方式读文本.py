"""
几种方式读文本

"""

import time

def main():

    try:
        # 一次性读取整个文件内容
        with open('./res/kobi.txt', 'r', encoding='utf-8') as f:
            print(f.read())

        #读取文件按行读取到列表中
        with open('./res/kobi.txt') as f:
            lines = f.readlines()
        print(lines)
    
        # 通过for-in循环逐行读取，加上延时
        with open('./res/kobi.txt', mode='r') as f:
            for line in f:
                print(line, end='')
                time.sleep(0.5)
            print()
        
    except FileNotFoundError as e:
        print(e)
    except LookupError as e:
        print(e)
    except UnicodeDecodeError as e:
        print(e)

if __name__ == '__main__':
    main()
