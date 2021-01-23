#-*- coding:utf-8 -*-

from tkinter import *
from PIL import Image, ImageTk
import random

class Application(Frame):
    # 一个经典的GUI程序
    def __init__(self, master=None):
        super().__init__(master)    #super()是父类的构造器
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        # 创建组件
        self.f1 = Frame(self.master, width=1400, height=400)
        self.f1.place(x=50, y=30)

        self.dealCrads()
        self.deal = Button(self.f1, text='发牌', font=('微软雅黑',24), command=self.dealCrads)
        self.deal.place(relx=0.45,rely=0.02)

    def dealCrads(self):
        cards = []
        # temps = []    # 排序暂不考虑
        for i in range(17):
            while(True):
                flag = True
                tmp = random.randrange(1, 55)
                for c in cards:
                    if(c == str(tmp)):
                        flag = False
                        break
                if(flag):
                    break
            cards.append(str(tmp))

        print(cards)
        self.cards = cards
        self.cardLabels = [n for n in range(17)]
        self.imgs = [n for n in range(17)]
        dltx = 1.0 / 18.5
        print(dltx)
        for i in range(17):
            imgp = Image.open("./img/pukeImage/%s.gif" % self.cards[i])
            imgp = imgp.resize(self.reSizeImg(1.5, imgp), Image.ANTIALIAS)
            self.imgs[i] = ImageTk.PhotoImage(imgp)
            self.cardLabels[i] = Label(self.f1, image=self.imgs[i])
            # self.cardLabels[i].bind('<Button-1>', self.cardTurn)
            self.cardLabels[i].place(relx=dltx * i, rely=0.3, x=5)
        self.cardLabels[0].bind_class('Label', '<Button-1>', self.cardTurn)

    def cardTurn(self, event):
        # 组件的geometry
        # print(event.widget.winfo_geometry())
        # 组件的y坐标
        # print(event.widget.winfo_y())
        if event.widget.winfo_y()==120:
            event.widget.place(y=-25)
        else:
            event.widget.place(y=0)

    def reSizeImg(self, scale, imgPIL):
        [width, height] = imgPIL.size
        if scale>0:
            return (int(width*scale), int(height*scale))
        else:
            return (width, height)


if __name__ == '__main__':
    root = Tk()
    root.title('性感Python在线发牌')
    root.geometry('1500x500+200+160')
    app = Application(master=root)
    root.mainloop()