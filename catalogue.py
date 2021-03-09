# 程序用途：1 统计文件数量； 2 统计文件类型； 3 生成目录

import os
from pathlib import Path
from collections import Counter

tree = ''


def catalogue(p, n=0):
    # 生成目录
    # 对路径转换后的，p = 下面的Path(filepath)
    global tree  # global 定义全局变量，实现在函数内部改变变量值
    if p.is_file():
        tree += '    |' * n + '····' + p.name + '\n'
    elif p.is_dir():
        tree += '    |' * n + '****' + str(p.relative_to(p.parent)) + '：' + '\n'  # 父路径
        for dir in p.iterdir():  # iterdir遍历目录
            catalogue(dir, n + 1)


def file_counter():
    # 统计文件的数量
    count = 0
    for paths, dirs, files in os.walk(filepath):
        for file in files:
            count += 1
    print('\n' + "一、文件数量为：" + str(count) + '\n')


def extension_counter():
    # 统计文件的类型
    print('\n' + "二、文件类型：" + '\n')
    file_list = []  # 建立存放文件名字的新列表
    for paths, dirs, files in os.walk(filepath):
        for file in files:
            file_list.append(file)
    extension_list = []  # 建立存放文件扩展名的列表
    for file in file_list:
        extension = os.path.splitext(file)[-1]
        extension_list.append(extension)
    # 对文件扩展名进行计数
    extension_number = Counter(extension_list)
    for m, n in extension_number.items():
        print(m + ": " + str(n) + ";")


if __name__ == '__main__':
    # 使用os.getced获取程序所在的路径，避免手动输入路径
    filepath = os.getcwd()
    catalogue(Path(filepath), 0)
    file_counter()
    extension_counter()
    print('\n' + "三、文件目录：" + '\n' + '\n' + tree)
    # 将目录保存至本地
    file_name = "catalogue.txt"
    with open(file_name, 'w', encoding="utf-8") as file_object:
        file_object.write(tree)
    print("运行成功，" + "请查看文件 catalogue.txt")
    input('\n' + "按任意键退出")


'''
@ 1757765654@qq.com
参考内容 https://blog.csdn.net/yaoyefengchen/article/details/80195231
'''
