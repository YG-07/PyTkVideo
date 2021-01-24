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
        self.btn1 = Button(self, text='按钮1', command=lambda: self.show('Jick', 23))
        self.btn1.pack()
        self.btn2 = Button(self, text='command绑定事件 按钮2', command=lambda :print('command绑定事件,不能直接获取event'))
        self.btn2.pack()
        self.btn3 = Button(self, text='bind绑定事件 按钮3')
        self.btn3.bind('<Button-1>',\
            lambda event:print('bind绑定事件,左键单击的控件：', event.widget))
        self.btn3.pack()
        self.master.bind_class('Button', '<Button-3>',\
            lambda event:print('bind_class绑定事件,右键单击的控件：', event.widget))

    def show(self, name, age):
        print('姓名：{0}, 年龄：{1}'.format(name, age))

if __name__ == '__main__':
    root = Tk()
    root.title('事件处理程序')
    root.geometry('400x300+700+260')
    app = Application(master=root)
    root.mainloop()