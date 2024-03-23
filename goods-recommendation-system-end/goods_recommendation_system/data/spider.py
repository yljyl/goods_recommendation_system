# -*- coding: utf-8 -*-
import os
from random import randint

import pandas as pd
import requests
import io
from bs4 import BeautifulSoup as BS
import time
import re
import urllib3

"""爬取产品商品数据： 目标网站：阿里巴巴"""


def creat_path(dirpath):
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)

def save_images(link):
    res = requests.get(url=link, headers=headers)
    if res.status_code != 200:
        raise IOError("code not 200")
        # 跳过该数据
    image_path = "../media/goods/";
    creat_path(image_path)

    n = str(randint(5, 20000))

    image_name = image_path + n + '.jpg'
    print(image_name)
    with open(image_name, 'wb') as opener:
        opener.write(res.content)
    print('图片保存成功', image_name)
    return n + '.jpg'

headers = {
    "Origin": "https://www.1688.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
}

# CAD6BBFA - 手机
# B5E7C4D4 - 电脑
# C4D0D7B0 - 男装
# C5AED7B0 - 女装
# CBAEB9FB - 水果
# C4B8D3A4 - 母婴

categorys = ["-CAD6BBFA","-B5E7C4D4","-C4D0D7B0","-C5AED7B0","-CBAEB9FB","-C4B8D3A4"]
names = ["手机","电脑","男装","女装","水果","母婴"]
base = "https://www.1688.com/chanpin/";
base2 = "https://www.1688.com";
requestlist = []
prev_cat = ""
for j in range(len(categorys)):
    for i in range(1, 3):
        tmp = base + categorys[j] + ".html?spm=a261b.2187593.pagenav.1.6fcd4b55WAgpf9&beginPage="+str(i);
        requestlist.append({"url": tmp, "category": names[j]});
# 对应的url地址和所查询的位置
print(requestlist)
l = []
count = 1;
list = list()
for k in range(len(requestlist)):
    response = requests.get(requestlist[k]["url"], headers=headers)
    # print(response)
    html = response.text
    #print(html)
    soup = BS(html, 'html.parser')

    vs = soup.find_all(name="div", attrs={"class": "su-photo230"})  # 获取所有产品列表
    price_list = soup.find_all(name="span", attrs={"class": "su-price"})  # 获取所有产品价格
    price_div = soup.find_all(name="div", attrs={"class": "sm-offerShopwindow-price"})  # 获取所有价格标签
    foot_div = soup.find_all(name="div", attrs={"class": "sm-offerShopwindow-foot fd-clr"})  # 获取所有底部div
    company_div = soup.find_all(name="div", attrs={"class": "sm-offerShopwindow-company fd-clr"})  # 获取所有comany div

    print("len(vs)", len(vs))
    for j in range(len(vs)):
        print("正在打印的条数:", j)
        try:
            tmp = {};

            #标题
            name = vs[j].find(name="img").attrs["alt"];
            #图片地址
            image_str = vs[j].find(name="img").attrs["src"];
            #价格
            price = price_list[j].get_text().replace('¥','');
            #成交量
            sales_str = price_div[j].find(name="span",attrs={"class": "sm-offerShopwindow-trade"}).get_text();

            if sales_str is not None:
                pattern = r"\d+"
                deal_num_list  = re.findall(pattern, sales_str)
                sales = deal_num_list[0]
            else:
                sales = 10
            #详情
            content = name

            # 省份和城市
            location_str = foot_div[j].find(name="span", attrs={"class": "su-city"}).get_text();
            if location_str is not None:
                location_list = location_str.split()
                province = location_list[0]
                city = location_list[1]
            else:
                province = '广东'
                city = '广州'

            # 销售商家
            business = company_div[j].find(name="a", attrs={"target": "_blank"}).get_text().strip();
            # 产品链接
            links = 'https:'+vs[j].find(name="a", attrs={"class": "sw-ui-photo220-box"}).attrs["href"];

            print("标题："+name)
            print("图片："+image_str)
            print("价格："+price)
            print("成交量："+sales)
            print("详情："+content)
            print("省份："+province)
            print("城市："+city)
            print("商家："+business)
            print("链接："+links)

            image_name = save_images(image_str)


            tmp['name'] = name
            tmp['img'] = image_name
            tmp['price'] = price
            tmp['content'] = content
            tmp['category'] = requestlist[k]["category"]
            tmp['sales'] = sales
            tmp['province'] = province
            tmp['city'] = city
            tmp['business'] = business
            tmp['links'] = links

            if tmp["category"] != prev_cat:
                list.clear()
            prev_cat = tmp["category"]

            l.append(tmp);

            dic = {"产品名称": tmp["name"], '图片地址': tmp["img"],
                   '价格': tmp["price"], '详情': tmp['content'], '销售量': tmp['sales'], '省份': tmp['province']
                , '城市': tmp['city'], '商家': tmp['business'], '链接': tmp['links']}
            list.append(dic)

            time.sleep(1);
        except Exception as e:
            print(e)
            continue
        print("爬取数据", tmp)


        try:
            data = pd.DataFrame(list)
            data.to_excel('files/' + tmp["category"] + '.xlsx', index=None)
        except Exception as e:
            print(e)
            continue


