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
        self.v = StringVar(self)
        self.v.set('Python')
        self.om = OptionMenu(self, self.v, 'Python', 'JavaScript', 'HTML', 'C/C++', 'PHP')
        self.om.pack()
        self.btn = Button(self, text='确定', command=self.getOption)
        self.btn.pack()

    def getOption(self):
        messagebox.showinfo('结果', '你选择的是：'+self.v.get())


if __name__ == '__main__':
    root = Tk()
    root.title('OptionMenu控件的GUI程序')
    root.geometry('400x300+700+260')
    app = Application(master=root)
    root.mainloop()