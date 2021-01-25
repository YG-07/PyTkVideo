#-*- coding:utf-8 -*-

from tkinter import *
from tkinter.simpledialog import askinteger


class Application(Frame):
    # 一个经典的GUI程序
    def __init__(self, master=None):
        super().__init__(master)    #super()是父类的构造器
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        # 创建组件
        self.btn = Button(self, text='设置年龄', command=self.setAge)
        self.btn.pack()
        self.label = Label(self, width=50, height=2, bg='#fff')
        self.label.pack()

    # askstring、askfloat同理
    def setAge(self):
        self.a = askinteger(title='输入年龄', prompt='请输入年龄',\
            initialvalue=18, minvalue=1, maxvalue=150)
        print(self.a)
        if not self.a==None:
            self.label.config(text=self.a)


if __name__ == '__main__':
    root = Tk()
    root.title('简单对话框的GUI程序')
    root.geometry('800x500+700+260')
    app = Application(master=root)
    root.mainloop()