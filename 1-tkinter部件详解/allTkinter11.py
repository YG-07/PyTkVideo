#-*- coding:utf-8 -*-

import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image,ImageTk

def show_popupmenu(event):
    popupmenu.post(event.x_root, event.y_root)

def toplevel():
    top = tk.Toplevel()
    top.title('显示图片')
    top.geometry('1024x560')
    img = Image.open('wiki-Tkinter.jpg')
    img_tk = ImageTk.PhotoImage(img)
    label = tk.Label(top, image=img_tk)
    label.pack()

    top.mainloop()

root = tk.Tk()
root.title('Tk的所有控件测试')
root.geometry('400x600+100+100')

# 23.弹出式窗口Menu+bind(通过监听事件，弹出一个菜单的弹窗)
popupmenu = tk.Menu(root, tearoff=0)
popupmenu.add_command(label='最小化', command=root.iconify),\
popupmenu.add_command(label='退出', command=root.destroy)
# 单击右键，弹出菜单
root.bind('<Button-3>', show_popupmenu)

# 24.顶层窗口tk.Toplevel
button_top = ttk.Button(root, text='子窗口 显示图片', command=toplevel)

# 控件布局
button_top.pack()


root.mainloop()
