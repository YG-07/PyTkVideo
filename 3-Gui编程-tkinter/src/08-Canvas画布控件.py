#-*- coding:utf-8 -*-

import random
from tkinter import *
from PIL import Image, ImageTk


class Application(Frame):
    # 一个经典的GUI程序
    def __init__(self, master=None):
        super().__init__(master)    #super()是父类的构造器
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        # 创建组件
        self.canvas = Canvas(self, width=800, height=500, bg='#fff')
        self.canvas.pack()
        # 画直线或折线(多组x,y值)
        line = self.canvas.create_line(10, 10, 300, 200, 40, 80, 10, 50)
        # 画一个矩形(左上角,右下角x,y)
        rect = self.canvas.create_rectangle(100, 300, 410, 400)
        # 画一个圆或椭圆(2个点是外切矩形的(左上角,右下角x,y))
        oval = self.canvas.create_oval(200, 200, 500, 500)

        # tk.PhotoImage支持gif、png、pgm、ppm格式
        global img
        # 方法一：直接用tk的函数显示在tk画布上
        # img = PhotoImage(file='./img/nuo.gif')
        # 方法二：通过PIL库的Image导入图片，调整尺寸，再用ImageTk的函数显示在tk画布上
        imgp = Image.open("./img/nuo.gif")
        imgp = imgp.resize(self.reSizeImg(0.8,imgp), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(imgp)

        self.canvas.create_image(600, 100, image=img)
        Button(self, text='随机画3个矩形', command=self.drawRecgs).pack(side='left')

    def reSizeImg(self, scale, imgPIL):
        [width, height] = imgPIL.size
        if scale>0:
            return (int(width*scale), int(height*scale))
        else:
            return (width, height)

    def drawRecgs(self):
        for i in range(3):
            x1 = random.randrange(int(self.canvas['width'])/2)
            y1 = random.randrange(int(self.canvas['height'])/2)
            x2 = x1 + random.randrange(int(self.canvas['width']) / 2)
            y2 = y1 + random.randrange(int(self.canvas['height']) / 2)
            self.canvas.create_rectangle(x1, y1, x2, y2)


if __name__ == '__main__':
    root = Tk()
    root.title('Canvas控件的GUI程序')
    root.geometry('1050x750+400+160')
    app = Application(master=root)
    root.mainloop()