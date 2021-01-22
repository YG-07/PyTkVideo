#-*- coding:utf-8 -*-

from tkinter import *
from tkinter import messagebox

class Application(Frame):
    # 一个经典的GUI程序
    def __init__(self, master=None):
        super().__init__(master)    #super()是父类的构造器
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        # 创建组件
        self.btn01 = Button(self, text='普通按钮', width=10, height=2)
        # disabled禁用按钮
        self.btn01.config(state='disabled')
        # anchor按钮内容定位(默认center)，参数有n, ne, e, se, s, sw, w, nw, or center
        self.btn01.config(anchor='nw')
        self.btn01.pack()
        # 图片按钮
        self.img = PhotoImage(file='./img/shutdown.gif')
        self.btn02 = Button(self, image=self.img,\
            width=48, height=48, command=self.master.destroy)
        self.btn02.pack()

if __name__ == '__main__':
    root = Tk()
    root.title('Button控件的GUI程序')
    root.geometry('1050x750+400+160')
    app = Application(master=root)
    root.mainloop()