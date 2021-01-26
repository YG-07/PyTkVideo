#-*- coding:utf-8 -*-

# 【项目】画图软件开发开发一款简单的画图软件，包含如下功能：
# 1.画笔
# 2.矩形/椭圆绘制
# 3.清屏
# 4.橡皮擦
# 5.直线/带箭头的直叶
# 6.修改画笔颜色、背景颜色

from tkinter import *
from tkinter.ttk import *
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
        self.createData()
        self.createWidget()

    def createData(self):
        self.v1 = '#000'
        self.v2 = None
        self.sx = 0
        self.sy = 0
        self.lastDraw = 0
        self.startLine = False

    def createWidget(self):
        # 创建组件
        self.c = Canvas(self.master, width=450, height=280, bg='#fff')
        self.c.pack(fill='both',expand=1)
        self.c.create_oval(10, 10, 60, 70, fill='yellow')
        self.c.create_oval(600, 500, 150, 160, fill='green')
        self.c.create_oval(900, 900, 150, 160, fill='red')

        # 创建画图工具
        self.erasor = Button(self, text='橡皮擦', name='erasor', width=8)
        self.erasor.pack(side='left')
        self.pen = Button(self, text='画笔', name='pen', width=8)
        self.pen.pack(side='left')
        self.line = Button(self, text='直线', name='line', width=8)
        self.line.pack(side='left')
        self.arrowLine = Button(self, text='箭头直线', name='arrowLine', width=8)
        self.arrowLine.pack(side='left')
        self.circle = Button(self, text='圆', name='circle', width=8)
        self.circle.pack(side='left')
        self.rect = Button(self, text='矩形', name='rect', width=8)
        self.rect.pack(side='left')
        self.color = Button(self, text='画笔颜色', name='color', width=8)
        self.color.pack(side='left')

        self.fgc = Label(self, width=2, height=1, bg=self.v1, borderwidth=1, relief='solid')
        self.fgc.pack(side='left', padx=3)
        self.bgc = Label(self, width=2, height=1, bg=self.v2, borderwidth=1, relief='solid', text='透')
        self.bgc.pack(side='left')
        Separator(self, orient='vertical').pack(side='left', fill='y', padx=20)

        # 创建功能按钮
        self.clear = Button(self, text='清屏', name='clear')
        self.clear.pack(side='left')
        self.save = Button(self, text='保存', name='save')
        self.save.pack(side='left')
        self.open = Button(self, text='打开', name='open')
        self.open.pack(side='left')

        # 鼠标事件处理
        self.save.bind('<Button-1>', self.getter)
        self.open.bind('<Button-1>', self.setter)
        self.master.bind_class('Button','<1>', self.eventMag)
        self.c.bind('<ButtonRelease-1>', self.stopDraw)
        # 改变颜色
        self.color.bind('<Button-1>', self.myFgc)
        self.fgc.bind('<Button-1>', self.myFgc)
        self.bgc.bind('<Button-1>', self.myBgc)
        self.bgc.bind('<Button-3>', self.myTou)
        # 颜色一快捷字母键
        self.master.bind('<KeyPress-r>', self.colorKey)
        self.master.bind('<KeyPress-g>', self.colorKey)
        self.master.bind('<KeyPress-y>', self.colorKey)
        self.master.bind('<KeyPress-p>', self.colorKey)
        self.master.bind('<KeyPress-b>', self.colorKey)



    # 画图功能函数,事件管理
    def eventMag(self, event):
        name = event.widget.winfo_name()
        print(name)
        if name=='line':
            self.c.bind('<B1-Motion>', self.myLine)
        elif name=='arrowLine':
            self.c.bind('<B1-Motion>', self.myArrLine)
        elif name=='rect':
            self.c.bind('<B1-Motion>', self.myRect)
        elif name=='circle':
            self.c.bind('<B1-Motion>', self.myCircle)
        elif name=='pen':
            self.c.bind('<B1-Motion>', self.myPen)
        elif name=='erasor':
            self.c.bind('<B1-Motion>', self.myErasor)
        elif name == 'clear':
            self.c.delete('all')

    def startDraw(self, event):
        self.c.delete(self.lastDraw)
        if not self.startLine:
            self.startLine = True
            self.sx = event.x
            self.sy = event.y
    # 画图开始函数
    def stopDraw(self, event):
        self.startLine = False
        self.lastDraw = 0
    # 直线
    def myLine(self, event):
        self.startDraw(event)
        self.lastDraw=self.c.create_line(self.sx, self.sy, event.x, event.y, fill=self.v1)
    # 箭头直线
    def myArrLine(self, event):
        self.startDraw(event)
        self.lastDraw=self.c.create_line(self.sx, self.sy, event.x, event.y, arrow=LAST, fill=self.v1)
    # 矩形
    def myRect(self, event):
        self.startDraw(event)
        self.lastDraw=self.c.create_rectangle(self.sx, self.sy, event.x, event.y, outline=self.v1, fill=self.v2)
    # 圆
    def myCircle(self, event):
        self.startDraw(event)
        self.lastDraw=self.c.create_oval(self.sx, self.sy, event.x, event.y, outline=self.v1, fill=self.v2)
    # 画笔
    def myPen(self, event):
        self.startDraw(event)
        self.c.create_line(self.sx, self.sy, event.x, event.y, fill=self.v1)
        self.sx = event.x
        self.sy = event.y
    # 橡皮擦
    def myErasor(self, event):
        self.startDraw(event)
        self.c.create_rectangle(event.x-4,event.y-4,event.x+4,event.y+4, outline='#fff',fill='#fff')
    # 改变颜色
    def myFgc(self, event):
        fg = askcolor(color=self.v1, title='选择颜色一')
        self.v1 = fg[1]
        self.fgc['bg']=self.v1

    def myBgc(self, event):
        bg = askcolor(color=self.v2, title='选择颜色二')
        self.v2 = bg[1]
        self.bgc.config(bg=self.v2, text='')

    def myTou(self, event):
        self.v2 = None
        self.bgc.config(bg='#eee', text='透')

    # 颜色快捷键
    def colorKey(self, event):
        if event.char == 'r':
            self.v1 = 'red'
        elif event.char == 'g':
            self.v1 = 'green'
        elif event.char == 'y':
            self.v1 = 'yellow'
        elif event.char == 'p':
            self.v1 = 'pink'
        elif event.char == 'b':
            self.v1 = '#000'
        self.fgc['bg'] = self.v1

    # 功能函数
    def getter(self, event):
        self.c.update()
        x = self.master.winfo_rootx() + self.c.winfo_x() + 1
        y = self.master.winfo_rooty() + self.c.winfo_y() + 1
        x1 = x + self.c.winfo_width() - 8
        y1 = y + self.c.winfo_height() - 8
        self.filename = asksaveasfilename(title='保存图片到', initialfile='未命名.png', defaultextension='.png', \
            filetypes=[('PNG图片', '*.png'),('JPEG图片', '*.jpg'),('GIF图片', '*.gif'),('BMP位图', '*.bmp')])
        if self.filename:
            ImageGrab.grab().crop((x, y, x1, y1)).save(self.filename)

    def setter(self, event):
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