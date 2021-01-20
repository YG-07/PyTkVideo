#-*- coding:utf-8 -*-

import re
from tkinter import *
# url 地址解析
from urllib import parse
# 消息盒子
import tkinter.messagebox as msgbox
# 控制浏览器
import webbrowser

class App:
    def __init__(self, width=500, height=300):
        self.w = width
        self.h = height

        # 软件名称
        self.title = '视频解析助手'
        # tk对象
        self.root = Tk(className=self.title)
        self.root.geometry('%dx%d+500+300' % (self.w, self.h))

        # 接收用户的电影URL，并对地址做处理
        self.url = StringVar()
        self.v = IntVar()
        self.v.set(1)

        # 软件空间划分
        frame_1 = Frame(self.root)
        frame_2 = Frame(self.root)

        # 软件控件内容
        group = Label(frame_1, text='播放通道', padx=10, pady=10)
        tb = Radiobutton(frame_1, text='唯一通道',
            variable=self.v, value=1, width=10, height=3)

        label = Label(frame_2, text='请输入视频URL:')
        entry = Entry(frame_2,
            textvariable=self.url, highlightcolor='Fuchsia',
            highlightthickness=1, width=30)
        play = Button(frame_2, text='解析播放',
            font=('仿宋', 10), fg='Purple',
            width=2, height=1, command=self.video_play)

        # 控件布局，激活空间、控件位置确定
        frame_1.pack()
        frame_2.pack()
        # 空间1
        group.grid(row=0, column=0)
        tb.grid(row=0, column=1)
        # 空间2
        label.grid(row=0, column=0)
        entry.grid(row=0, column=1)
        play.grid(row=0, column=2, ipadx=30,ipady=3)

    # 定义播放按钮的事件函数
    def video_play(self):
        # 第三方播放解析api
        port = 'http://www.wmxz.wang/video.php?url='

        # 判断用户输入的URL是否合法
        if re.match(r'https?:/{2}\w.+$', self.url.get()):
            ip = self.url.get()
            ip = parse.quote_plus(ip)
            # 自动打开浏览器
            webbrowser.open(port + ip)
        else:
            msgbox.showerror(title='错误', message='视频URL无效，请重新输入!')

    # 启动软件
    def loop(self):
        self.root.mainloop()


if __name__ == '__main__':
    app = App()
    app.loop()