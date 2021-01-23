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
        self.f1 = Frame(self.master, width=400, height=400, bg='green')
        self.f1.place(x=30, y=30)

        Button(self.f1, text='按钮1').place(x=40, y=40)
        Button(self.f1, text='按钮2').place(relx=0.5, rely=0.5)
        # 同时存在是先定位相对父容器位置，再加上x,y的坐标
        Button(self.f1, text='按钮3').place(relx=0.5, rely=0.5, x=60, y=60)
        Button(self.f1, text='按钮4').place(relx=0.5, rely=0.5, x=-60, y=-60)
        # 使用place布局钢琴按键更加真实,有层叠感
        Button(self.f1, text='白', bg='#fff').place(relx=0.1, rely=0.5, relwidth=0.1, relheight=0.5)
        Button(self.f1, text='白', bg='#fff').place(relx=0.2, rely=0.5, relwidth=0.1, relheight=0.5)
        Button(self.f1, text='黑', bg='#000', fg='#fff').place(relx=0.15, rely=0.5, relwidth=0.1, relheight=0.25)


if __name__ == '__main__':
    root = Tk()
    root['bg']='#fff'
    root.title('place布局的GUI程序')
    root.geometry('500x500+700+260')
    app = Application(master=root)
    root.mainloop()