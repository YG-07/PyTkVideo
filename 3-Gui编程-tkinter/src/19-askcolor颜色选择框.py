#-*- coding:utf-8 -*-

from tkinter import *
from tkinter.colorchooser import *


class Application(Frame):
    # 一个经典的GUI程序
    def __init__(self, master=None):
        super().__init__(master)    #super()是父类的构造器
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        # 创建组件
        self.btn = Button(self, text='改变背景色', command=self.change)
        self.btn.pack()

    def change(self):
        self.s1 = askcolor(color='red', title='选择背景色')
        print(self.s1)
        self.master.config(bg=self.s1[1])


if __name__ == '__main__':
    root = Tk()
    root.title('askcolor颜色选择框的GUI程序')
    root.geometry('800x300+700+260')
    app = Application(master=root)
    root.mainloop()