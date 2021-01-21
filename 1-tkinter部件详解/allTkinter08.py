#-*- coding:utf-8 -*-

import tkinter as tk
import tkinter.ttk as ttk

# 定义画笔事件函数
def paint(event):
    x1,y1 = (event.x, event.y)
    x2,y2 = (event.x, event.y)
    canvas.create_rectangle(x1, y1, x2, y2)


root = tk.Tk(className='Tk的所有控件测试')
root.geometry('400x600+100+100')

# 20.Notebook记事本
frame_nb1,frame_nb2 = ttk.Frame(root), ttk.Frame(root)
notebook = ttk.Notebook(root, height=200, width=200)
notebook.add(frame_nb1, text='选项卡1'), notebook.add(frame_nb2, text='选项卡2')

# 21.画布Canvas
canvas = tk.Canvas(root, bg='white', height=300, width=300)
canvas.create_line(10, 10, 20, 30, 40, 70)
canvas.bind('<B1-Motion>', paint)


# 控件布局
notebook.pack(pady=2)
canvas.pack(pady=2)


root.mainloop()
