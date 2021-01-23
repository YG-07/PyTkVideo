#-*- coding:utf-8 -*-

from tkinter import *
from PIL import Image, ImageTk


class Application(Frame):
    # 一个计算器的GUI程序
    def __init__(self, master=None):
        super().__init__(master)    #super()是父类的构造器
        self.master = master
        self.pack()
        self.createList()
        self.createWidget()

    def createList(self):
        # 创建元组(tuple)
        self.btnTup = \
            (('MC', 'M+', 'M-', 'MR'),\
             ('C', '±', '÷', '×'),\
             (7, 8, 9, '-'), \
             (4, 5, 6, '+'), \
             (1, 2, 3, '='), \
             (0, '.'))

    def createWidget(self):
        # 创建组件,7行4列，entey占4列，'0'占2列，'='占2行
        # columnspan合并列，rowspan合并行
        # 结果输入框
        Entry(self, width=16, font=('黑体', 28)).grid(row=0, column=0, padx=2, pady=5, columnspan=4)
        # 遍历生成按钮
        for ri,r in enumerate(self.btnTup):
            for ci,c in enumerate(r):
                if not (c==0 or c=='.' or c=='='):
                    Button(self, text=c, width=2, height=2).grid(row=ri+1, column=ci, padx=2, pady=2, sticky=NSEW)
                elif c=='=':
                    Button(self, text=c, width=2, height=2).grid(row=ri+1, column=ci, padx=2, pady=2, rowspan=2, sticky=NSEW)
                elif c==0:
                    Button(self, text=c, width=2, height=2).grid(row=ri+1, column=ci, padx=2, pady=2, columnspan=2, sticky=NSEW)
                elif c=='.':
                    Button(self, text=c, width=2, height=2).grid(row=ri+1, column=ci+1, padx=2, pady=2, sticky=NSEW)


if __name__ == '__main__':
    root = Tk()
    root.title('简易计算器-grid布局')
    root.geometry('330x360+600+360')
    app = Application(master=root)
    root.mainloop()