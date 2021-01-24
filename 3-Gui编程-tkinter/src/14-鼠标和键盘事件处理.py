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
        self.c1 = Canvas(self, width=700, height=400, bg='yellow')
        self.c1.pack()
        self.c1.bind('<Button-1>', self.mouseTest)
        self.c1.bind('<B1-Motion>', self.testDrag)
        self.master.bind('<KeyPress>', self.testKey)
        # 小写的a才起作用
        self.master.bind('<KeyPress-a>', self.press_a)
        self.master.bind('<KeyRelease-a>', self.release_a)


    def mouseTest(self, event):
        print('左键单击(相对父容器):{0},{1}'.format(event.x, event.y))
        print('左键单击(相对屏幕):{0},{1}'.format(event.x_root, event.y_root))
        print('事件绑定的组件:', event.widget)

    def testDrag(self, event):
        self.c1.create_oval(event.x,event.y,event.x+1,event.y+1)

    def testKey(self, event):
        print('按键的keycode:{0}, 键的char:{1}, 键的keysym:{2}'\
            .format(event.keycode, event.char, event.keysym))
    def press_a(self, event):
        print('按下了a键')
    def release_a(self, event):
        print('释放了a键')

if __name__ == '__main__':
    root = Tk()
    root.title('事件处理程序')
    root.geometry('800x500+700+260')
    app = Application(master=root)
    root.mainloop()