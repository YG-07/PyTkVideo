#-*- coding:utf-8 -*-

# 【项目】画图软件开发开发一款简单的画图软件，包含如下功能：
# 1.画笔
# 2.矩形/椭圆绘制
# 3.清屏
# 4.橡皮擦
# 5.直线/带箭头的直叶
# 6.修改画笔颜色、背景颜色

from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter.filedialog import *
from tkinter.messagebox import *

from PIL import ImageGrab


class Application(Frame):
    # 一个经典的GUI程序
    def __init__(self, master=None):
        super().__init__(master)    #super()是父类的构造器
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        # 创建组件
        self.c = Canvas(self.master, width=450, height=280, bg='#fff')
        self.c.pack(fill='both',expand=1)
        self.c.create_oval(10, 10, 60, 70, fill='yellow')
        self.c.create_oval(600, 500, 150, 160, fill='green')
        self.c.create_oval(900, 900, 150, 160, fill='red')


        # 创建功能按钮
        self.save = Button(self, text='保存', name='save', command=self.getter)
        self.save.pack(side='left', padx=10)
        self.open = Button(self, text='打开', name='open', command=self.setter)
        self.open.pack(side='left', padx=10)

    def getter(self):
        self.c.update()
        x = self.master.winfo_rootx() + self.c.winfo_x() + 1
        y = self.master.winfo_rooty() + self.c.winfo_y() + 1
        x1 = x + self.c.winfo_width() - 8
        y1 = y + self.c.winfo_height() - 8
        self.filename = asksaveasfilename(title='保存图片到', initialfile='未命名.png', defaultextension='.png', \
            filetypes=[('PNG图片', '*.png'),('JPEG图片', '*.jpg'),('GIF图片', '*.gif'),('BMP位图', '*.bmp')])
        if self.filename:
            ImageGrab.grab().crop((x, y, x1, y1)).save(self.filename)

    def setter(self):
        self.filename = askopenfilename(title='打开图片', defaultextension='.png', \
            filetypes=[('PNG图片', '*.png'),('GIF图片', '*.gif')])
        if not self.filename:
            return
        self.img = PhotoImage(file=self.filename)
        w = self.img.width()
        h = self.img.height()
        cx = int(w/2)
        cy = int(h/2)
        self.c.create_image(cx,cy,image=self.img)


if __name__ == '__main__':
    root = Tk()
    root.title('简易画图程序')
    root.geometry('700x730+700+160')
    app = Application(master=root)
    root.mainloop()