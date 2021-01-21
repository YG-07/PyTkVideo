#-*- coding:utf-8 -*-

from tkinter import *
from tkinter import messagebox

def btn_click(e):
    messagebox.showinfo('信息','点击了按钮!~')

root = Tk()
root.title('测试窗口1')
# geometry('width x height +/-x +/-y'),
# 参数：窗口宽x高，窗口左上角与屏幕位置：正xy是距离左上，负xy是距离右下
root.geometry('1050x750+400+160')

btn1 = Button(root, text='按钮')
btn1.pack()
btn1.bind("<Button-1>",btn_click)


# mainloop()方法，进入事件循环
root.mainloop()