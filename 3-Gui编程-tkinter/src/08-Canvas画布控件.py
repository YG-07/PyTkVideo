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
        self.canvas = Canvas(self, width=800, height=500, bg='#fff')
        self.canvas.pack()
        # 画直线或折线(多组x,y值)
        line = self.canvas.create_line(10, 10, 300, 200, 40, 50, 10, 20)
        # 画一个矩形(左上角,右下角x,y)
        rect = self.canvas.create_rectangle(10, 300, 210, 400)

if __name__ == '__main__':
    root = Tk()
    root.title('Entry控件的GUI程序')
    root.geometry('1050x750+400+160')
    app = Application(master=root)
    root.mainloop()