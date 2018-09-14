#-*- coding:utf-8 -*-
# import sys
#
# print('命令行参数如下:')
# for i in sys.argv:
#     print(i)
#
# print('\n\nPython 路径为：', sys.path, '\n')
# #
# # num = float(input("输入一个数字: "))
# # if num >= 0:
# #    if num == 0:
# #        print("零")
# #    else:
# #        print("正数")
# # else:
# #    print("负数")
#

import requests
import re
import os


def open_url(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0"}
    response = requests.get(url, headers=headers)

    return response


def find_img(url):
    html = open_url(url).text
    p = r'<img class="BDE_Image" src="([^"]+\.*)"'

    img_addrs = re.findall(p, html)

    for each in img_addrs:
        print(each)
    for each in img_addrs:
        file = each.split("/")[-1]
        with open(file, "wb") as f:
            img = open_url(each).content
            f.write(img)


def get_img():
    os.mkdir("TieBaTu")
    os.chdir("TieBaTu")
    find_img(url)


if __name__ == "__main__":
    url = 'https://tieba.baidu.com/p/5085123197'
    #url = 'https://dev.mi.com/myitems/0/0?userId=1422030790'
    get_img()


# for j in range(len(img_list)):
#     img_url = img_list[j]
#     img = "F:\ceshi/ceshi_" + str(i) + str(j) + ".jpg"
#     print("正在下载第" + str(i) + "页，第" + str(j) + "个图片")
#     urllib.request.urlretrieve(img_url, img)
#     print("第" + str(i) + str(j) + "个图片下载完成")
