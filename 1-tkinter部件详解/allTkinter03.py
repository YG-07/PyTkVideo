#-*- coding:utf-8 -*-

import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk(className='Tk的所有控件测试')
root.geometry('400x600+100+100')
# 12.标签框架LabelFrame(一个有名字的框架区域)
# 13.滚动条Scrollbar(与列表框绑定使用的滚动条，有横纵方向)
# 14.列表框Listbox(一行一行的列表框，可与滚动条绑定使用)
labelframe = ttk.LabelFrame(root, text='标签框架')
scrollbar = ttk.Scrollbar(labelframe)
listbox = tk.Listbox(labelframe, height=6, width=5,\
    yscrollcommand=scrollbar.set)
for i in range(30):
    listbox.insert('end', i)
scrollbar.config(command=listbox.yview)
# 列表框和滚动条要双向绑定yscrollcommand和command
# 控件布局
labelframe.pack(pady=2),\
scrollbar.pack(side='right', pady=2, fill='y'),\
listbox.pack(side='left', pady=2)

root.mainloop()
