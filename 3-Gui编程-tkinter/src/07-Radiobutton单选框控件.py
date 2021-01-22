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
        self.v = StringVar()
        self.v.set('F')

        self.r1 = Radiobutton(self, text='男', value='M', variable=self.v)
        self.r2 = Radiobutton(self, text='女', value='F', variable=self.v)

        self.r1.grid(row=0, column=0),self.r2.grid(row=0, column=1)
        Button(self, text='确定', command=self.sex).grid(row=0, column=2)

        self.codeHobby = IntVar()
        self.videoHobby = IntVar()

        print(self.codeHobby.get())
        self.label = Label(self, text='爱好：').grid(row=1, column=0)
        self.c1 = Checkbutton(self, text='敲代码',
            variable=self.codeHobby, onvalue=1, offvalue=0)
        self.c2 = Checkbutton(self, text='看B站',
            variable=self.videoHobby, onvalue=1, offvalue=0)

        self.c1.grid(row=1, column=1), self.c2.grid(row=1, column=2)
        Button(self, text='确定', command=self.hobbies).grid(row=1, column=3)

    def sex(self):
        # 类似的三元运算: 真 if 条件 else 假
        str = '男' if self.v.get()=='M' else '女'
        messagebox.showinfo('结果', '选择的性别：'+str)

    def hobbies(self):
        str = '选择的爱好：'
        if self.codeHobby.get()==1:
            str += self.c1['text']+' '
        if self.videoHobby.get()==1:
            str += self.c2['text']+' '
        messagebox.showinfo('结果', str)


if __name__ == '__main__':
    root = Tk()
    root.title('Radiobutton控件的GUI程序')
    root.geometry('1050x750+400+160')
    app = Application(master=root)
    root.mainloop()