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
        self.label01 = Label(self, text='用户名：')
        self.label01.pack()

        # StringVar和组件的textvariable值双向绑定
        # v1.get()和self.entry01.get()一样
        v1=StringVar()
        self.entry01 = Entry(self, textvariable=v1)
        self.entry01.pack()

        self.label02 = Label(self, text='密码：')
        self.label02.pack()

        v2 = StringVar()
        self.entry02 = Entry(self, textvariable=v2)
        self.entry02.pack()

        self.btnlog = Button(self, text='登录', command=self.login)
        self.btnlog.pack()

    def login(self):
        username = self.entry01.get()
        password = self.entry02.get()
        if username=='admin' and password=='123':
            messagebox.showinfo('登录信息', '登录成功！欢迎，开始学习吧~')
            print(self.label01['text'], username, self.label02['text'], password)
        else:
            messagebox.showerror('登录信息', '登录失败！用户名或密码错误！')

if __name__ == '__main__':
    root = Tk()
    root.title('Entry控件的GUI程序')
    root.geometry('1050x750+400+160')
    app = Application(master=root)
    root.mainloop()