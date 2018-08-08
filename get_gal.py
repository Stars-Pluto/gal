# -*- conding:utf-8 -*-
#自定义的一个关于UA随机的模块
import UserAgent
import requests
import time
from bs4 import BeautifulSoup
import sqlite3
import traceback
import string
'''
#进行了一些断代码的测试，比如元素定位的测试，请求提交的测试
u='https://www.mygalgame.com/category/%E6%B1%89%E5%8C%96%E7%A1%AC%E7%9B%98%E7%89%88/ah/a/page/2/'
ua={'user-agent':UserAgent.randomUserAgent()}
r = requests.get(u,headers=ua)
post_data = {
    'e_secret_key': 'A557'}
#r = requests.post(u,headers=ua,data=post_data)
print(r.raise_for_status)
r.encoding = 'utf-8'#r.apparent_encoding

soup = BeautifulSoup(r.text,"html.parser")
hn = soup.select('.panel-body .e-secret a button')[0]
print(hn['onclick'])
'''
#所有的页面
url_as = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','19','其它']

#第一次就创建数据库；不论第几次均返回一个连接conn。
def sqlit_create():
    with sqlite3.connect('more_gal.db',check_same_thread=False) as conn:
        conn.isolation_level = ''
        try:
            create_tb = '''create table if not exists more_a (id integer primary key autoincrement,pan char(60),get char(8),show char(1024),img char(50),name char(40));'''
            conn.execute(create_tb)
        except:
            print('more_a表已经存在。')
        return conn
#向表中插入数据并提交。
def sqlit_input(conn,pan,get,show,img,name):
    try:
        href = (str(pan),str(get),str(show),str(img),str(name),)
        #print(href)
        sql_input = 'insert into more_a (pan,get,show,img,name) values (?,?,?,?,?)'
        conn.execute(sql_input,href)
        conn.commit()
    except sqlite3.Error as e:
        print("sqlite3 Error:", e)
        traceback.print_exc()
#构成每个页面的URL
def input_init(url_as_i):#通过循环列表的元素构成每页的链接
    base_url = 'https://www.mygalgame.com/category/汉化硬盘版/ah/'
    req_Url=base_url+'/'+url_as_i+'/'
    return req_Url
#通过requests进行get请求
def request(req_url):
    #time.sleep(2)
    useragent = {'user-agent':UserAgent.randomUserAgent()}
    req = requests.get(req_url,headers=useragent)
    req.raise_for_status
    req.encoding = req.apparent_encoding
    return req
#获取分页的链接，如果存在
def get_page_url(soup):
    page_url = soup.select('#zan-page ul li a')[:-1]
    return page_url
#获取具体每一个的全文页面
def get_more_url(soup):
    more_url = soup.select('#mainstay #article-list div .visible-xs a')
    url_title,url_img = [],[]
    for i in more_url:
        if '<img alt=' in str(i):
            s_href = i['href']
            s_src = i.img['src']
            url_title.append(s_href)
            url_img.append(s_src)
    return url_title,url_img

def pan_form_href(soup):#获取提交表单的目的链接和提交数据
    form_action = soup.select('.panel-body form')[0]['action']
    form_post = soup.select('.panel-footer b span span')[0].text
    return form_action,form_post
    
def post_pan(form_action,form_post):#进行表单数据的提交，返回一个html页面
    post_data = {
    'e_secret_key': form_post}
    ua={'user-agent':UserAgent.randomUserAgent()}
    post_html = requests.post(form_action,headers=ua,data=post_data)
    post_html.raise_for_status
    post_html.encoding = post_html.apparent_encoding
    return post_html
#获取云盘的链接还要主要介绍和游戏名字
def pan_url(soup):
    try:
        yun_pan_url = soup.select('.panel-body .e-secret a button')[0]['onclick'][50:-2]
    except:
        yun_pan_url = soup.select('.panel-body a button')[0]['onclick'][50:-2]
    url_name = soup.select('.visible-xs h4 a')[0].text
    url_show_check = soup.find('div',{'class':'alert alert-success'})
    if url_show_check:
        url_show = url_show_check.text
    else:
        url_show = 'more should be more'
    return yun_pan_url,url_show,url_name

def ec(url_title,url_img):
    for j in range(len(url_title)):
        #print(url_title[j])
        more_req = request(url_title[j])
        more_soup = BeautifulSoup(more_req.text,"html.parser")
        try:
            form_action,form_post = pan_form_href(more_soup)
            more_html = post_pan(form_action,form_post)
            post_soup = BeautifulSoup(more_html.text,"html.parser")
        except:
            post_soup = more_soup
        yun_pan_url,url_show,url_name = pan_url(post_soup)
        print(yun_pan_url,url_name)
        sqlit_input(conn,yun_pan_url,form_post,url_show,url_img[j],url_name)
if __name__=='__main__':
    conn = sqlit_create()
    for i in url_as:
        req_url = input_init(i)
        print(req_url)
        req = request(req_url)
        soup = BeautifulSoup(req.text,"html.parser")
        url_title,url_img = get_more_url(soup)
        ec(url_title,url_img)
        page_url = get_page_url(soup)
        for p in page_url:
            s_url = p['href']
            req_a = request(s_url)
            soup_a = BeautifulSoup(req_a.text,"html.parser")
            url_title_a,url_img_a = get_more_url(soup_a)
            ec(url_title_a,url_img_a)
