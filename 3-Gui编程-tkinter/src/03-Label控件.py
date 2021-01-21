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
        # 设置组件选项方式，
        # 方法一：传参 源码参数：
        # __init__(self, master=None, cnf={}, **kw) (字典cnf和kw一样，会合并字典)
        self.label01 = Label(self, width=10, height=2,\
            font=('微软雅黑', 24))
        # 方法二：字典索引 __setitem__
        self.label01['text']='七楽神奈'
        # 方法三：.config()
        self.label01.config(bg='pink', fg='white')
        self.label01.pack()
        # 显示图像
        self.img = PhotoImage(file='./img/gm.gif')
        # 或 global img  img = ...
        self.label02 = Label(self, image=self.img, \
            width=65, height=65, borderwidth=1, relief='solid')
        self.label02.pack(pady=5)
        # 显示多行文本
        self.txt = '《诗经·大雅·桑柔》\n' \
                   '靡所止疑，云徂何往？\n' \
                   '君子实维，秉心无竞。\n' \
                   '谁生厉阶，至今为梗？\n' \
                   '忧心殷殷，念我土宇。'
        self.label03 = Label(self, text=self.txt,\
            borderwidth=1, relief='solid', justify='center',\
            font=('微软雅黑', 28))
        self.label03.pack()


if __name__ == '__main__':
    root = Tk()
    root.title('Label控件的GUI程序')
    root.geometry('1050x750+400+160')
    app = Application(master=root)
    root.mainloop()