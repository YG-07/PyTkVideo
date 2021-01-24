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
        # tickinterval标记刻度，orient默认垂直方向
        self.s1 = Scale(self, from_=10, to=50, length=200,\
            tickinterval=5, orient=HORIZONTAL, command=self.change)
        self.s1.pack()
        self.label = Label(self, text='滑块改变文字大小', width=16, height=1, bg='#000', fg='#fff')
        self.label.pack()

    def change(self, value):
        print('滑块的值：', value)
        newFont = ('黑体', value)
        self.label.config(font=newFont)


if __name__ == '__main__':
    root = Tk()
    root.title('Scale控件的GUI程序')
    root.geometry('800x300+700+260')
    app = Application(master=root)
    root.mainloop()