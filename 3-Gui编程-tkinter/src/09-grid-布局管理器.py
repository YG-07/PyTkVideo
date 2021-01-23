#-*- coding:utf-8 -*-

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
        Label(self, text='账号：').grid(row=0, column=0)
        self.entry01 = Entry(self)
        self.entry01.grid(row=0, column=1)
        Label(self, text='(用户名/手机号/邮箱)').grid(row=0, column=2)

        Label(self, text='密码：').grid(row=1, column=0)
        self.entry01 = Entry(self, show='*')
        self.entry01.grid(row=1, column=1)

        Button(self, text='登录').grid(row=2, column=1, sticky=W)
        Button(self, text='取消').grid(row=2, column=2, sticky=E)

if __name__ == '__main__':
    root = Tk()
    root.title('grid布局的GUI程序')
    root.geometry('1050x750+400+160')
    app = Application(master=root)
    root.mainloop()