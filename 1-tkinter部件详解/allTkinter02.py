#-*- coding:utf-8 -*-

import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk(className='Tk的所有控件测试')
root.geometry('400x600+100+100')
# 5.按钮Button 6.标签Label 7.输入框Entry 8.单选按钮Radiobutton 9.复选框Checkbutton
button, label, entry, radio, check = ttk.Button(root, text='按钮'),\
    ttk.Label(root, text='标签'), ttk.Entry(root),\
    ttk.Radiobutton(root, text='选项按钮'),\
    ttk.Checkbutton(root, text='复选框')
# 10.尺寸条(tk(有刻度)/ttk)Scale 11.有刻度的尺寸条LabeldScale
scale, labelscale, spinbox = \
    tk.Scale(root, from_=0, to=10, length=200, orient='horizontal'),\
    ttk.LabeledScale(root, from_=0,to=10),\
    ttk.Spinbox(root, from_=0, to=20)
# 控件布局
button.pack(pady=2), label.pack(pady=2), entry.pack(pady=2),
radio.pack(pady=2), check.pack(pady=2),\
scale.pack(pady=2), labelscale.pack(pady=2), spinbox.pack(pady=2)


root.mainloop()
