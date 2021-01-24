#-*- coding:utf-8 -*-

from tkinter import *
from tkinter.filedialog import *


class Application(Frame):
    # 一个经典的GUI程序
    def __init__(self, master=None):
        super().__init__(master)    #super()是父类的构造器
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        # 创建组件
        self.btn = Button(self, text='显示文件名', command=self.openfile)
        self.btn.pack()
        self.btn2 = Button(self, text='打开并读取文件', command=self.openfile2)
        self.btn2.pack()
        self.show = Label(self, width=60, height=20, bg='#fff', fg='#000')
        self.show.pack()

    def openfile(self):
        # 返回文件名
        self.file = askopenfilename(title='打开文件',\
            initialdir='D:/', filetypes=[('所有文件', '.*'),('文本文件', '.txt')])
        print(self.file)
        self.show.config(text=self.file)

    def openfile2(self):
        # 返回文对象
        with askopenfile(title='读取文件',\
            initialdir='D:/', filetypes=[('文本文件', '.txt')]) as f:
            self.show.config(text= f.read())



if __name__ == '__main__':
    root = Tk()
    root.title('文件选择框的GUI程序')
    root.geometry('800x500+700+260')
    app = Application(master=root)
    root.mainloop()