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
        self.btn1 = Button(self, text='按钮', command=self.btn_click)
        self.btn1.pack()
        # 退出按钮
        self.btnQuit = Button(self, text='退出', command=self.master.destroy)
        self.btnQuit.pack()

    def btn_click(self):
        messagebox.showinfo('信息', '点击了按钮!~')
        print('点击了按钮')

if __name__ == '__main__':
    root = Tk()
    root.title('一个经典的面向对象的GUI程序')
    root.geometry('1050x750+400+160')
    app = Application(master=root)
    root.mainloop()