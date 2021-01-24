#-*- coding:utf-8 -*-

from tkinter import *


class Application(Frame):
    # 一个经典的GUI程序
    def __init__(self, master=None):
        super().__init__(master)    #super()是父类的构造器
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        # 创建组件
        self.c1 = Canvas(self, width=700, height=400, bg='yellow')
        self.c1.pack()
        self.c1.bind('<B1-Motion>', self.testDrag)

    def testDrag(self, event):
        self.c1.create_oval(event.x,event.y,event.x+1,event.y+1)

if __name__ == '__main__':
    root = Tk()
    root.title('事件处理程序')
    root.geometry('800x500+700+260')
    app = Application(master=root)
    root.mainloop()