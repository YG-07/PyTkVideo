#-*- coding:utf-8 -*-

from tkinter import *
from tkinter.messagebox import *


class Application(Frame):
    # 一个经典的GUI程序
    def __init__(self, master=None):
        super().__init__(master)    #super()是父类的构造器
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        # 创建组件
        self.btn = Button(self, text='显示信息', command=self.about)
        self.btn.pack()

    def about(self):
        txt = '关于\n' \
              '这里是关于的内容\n' \
              '功能什么什么\n'
        self.mbox = showinfo(title='关于', message=txt)


if __name__ == '__main__':
    root = Tk()
    root.title('简单对话框的GUI程序')
    root.geometry('800x500+700+260')
    app = Application(master=root)
    root.mainloop()