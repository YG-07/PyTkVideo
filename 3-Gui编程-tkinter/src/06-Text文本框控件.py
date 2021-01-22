#-*- coding:utf-8 -*-

import webbrowser
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
        self.w1 = Text(self, width=120, height=30, bg='#ccc')
        self.w1.pack()
        self.w1.insert(1.0, '1234567890\nabcdefg')
        self.w1.insert(2.3, '第2行,第3列插入\n')

        Button(self, text='插入重复文本', command=self.insertText).pack(side='left', padx=35)
        Button(self, text='返回文本', command=self.returnText).pack(side='left', padx=35)
        Button(self, text='添加图片', command=self.addImage).pack(side='left', padx=35)
        Button(self, text='添加组件', command=self.addWidget).pack(side='left', padx=35)
        Button(self, text='通过tag精确控制文本', command=self.testTag).pack(side='left', padx=35)

    def insertText(self):
        # insert(插入位置,内容)插入,INSERT光标处,END末尾处
        self.w1.insert(INSERT, 'Hello ')
        self.w1.insert(END, '[sxt]')
        self.w1.insert(1.8, '喵喵喵')

    def returnText(self):
        # get(1.0, END)获取文本框内容get(起始位置，结束位置),左闭右开
        print(self.w1.get(1.2, 1.6))
        self.w1.insert(1.8, '哈哈')
        print('所有文本：\n'+self.w1.get(1.0, END))

    def addImage(self):
        # 添加图片,image属性
        self.img = PhotoImage(file='./img/gm.gif')
        self.w1.image_create(END, image=self.img)

    def addWidget(self):
        # 添加组件,window属性
        b1 = Button(self.w1, text='爱上学堂')
        self.w1.window_create(INSERT, window=b1)

    def testTag(self):
        # 删除数据delete
        self.w1.delete(1.0, END)
        self.w1.insert(INSERT, 'good good study, day day up!\n嘤嘤嘤\n百度')
        # 添加标签tag_add，标签有指令功能，如：事件监听tag_bind
        self.w1.tag_add('good', 1.0, 1.9)
        self.w1.tag_config('good', background='yellow', foreground='pink')

        self.w1.tag_add('baidu', 3.0, 3.2)
        self.w1.tag_config('baidu', underline=True)
        self.w1.tag_bind('baidu', '<Button-1>', self.webshow)

    def webshow(self, event):
        webbrowser.open('https://www.baidu.com')

if __name__ == '__main__':
    root = Tk()
    root.title('Text控件的GUI程序')
    root.geometry('1050x750+400+160')
    app = Application(master=root)
    root.mainloop()