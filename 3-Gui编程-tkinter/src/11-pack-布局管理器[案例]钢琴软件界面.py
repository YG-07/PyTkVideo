#-*- coding:utf-8 -*-

from tkinter import *


class Application(Frame):
    # 一个经典的GUI程序
    def __init__(self, master=None):
        super().__init__(master)    #super()是父类的构造器
        self.master = master
        self.pack()
        self.createbtnTup()
        self.createWidget()

    def createbtnTup(self):
        self.btnTup = ('流行风','中国风','日本风','重金属','轻音乐')

    def createWidget(self):
        # 创建组件
        self.f1, self.f2 = Frame(self), Frame(self)
        self.f1.pack(),self.f2.pack()

        # 生成风格按钮
        for item in self.btnTup:
            Button(self.f1, text=item).pack(side='left', padx=10)
        # 生成钢琴键盘
        for i in range(1, 24):
            Label(self.f2, width=5, height=10,borderwidth=1, relief='solid',\
                bg='#000' if self.chkPiano(i) else '#fff').pack(side='left',padx=2)

    def chkPiano(self, n):
        n = n % 12
        if n==2 or n==4 or n==7 or n==9 or n==11:
            return True
        else:
            return False


if __name__ == '__main__':
    root = Tk()
    root.title('pack布局的GUI程序')
    root.geometry('1200x220+400+160')
    app = Application(master=root)
    root.mainloop()