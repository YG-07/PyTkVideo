#-*- coding:utf-8 -*-

import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk(className='Tk的所有控件测试')
root.geometry('400x600+100+100')

# 1.设置菜单栏Menu-------
menubar = tk.Menu(root)
# tearoff为1时可以提出工具栏
filemenu = tk.Menu(menubar, tearoff=0)
# 设置菜单名和子菜单项
menubar.add_cascade(label='文件', menu=filemenu),\
    filemenu.add_command(label='打开'),\
    filemenu.add_command(label='新建'),\
    filemenu.add_command(label='保存')
# 将菜单布局的窗口上
root.config(menu=menubar)

# 2.面板panedWindow
# orient 分割线方向vertical/horizontal
# sashrelief/relief 分割线样式sunken/raised/flat
pw = tk.PanedWindow(root, orient='vertical', sashrelief='sunken')
pw.pack(fill='both', expand=1)
# 3.状态栏Separator
separator = ttk.Separator(root).pack(fill='x',padx=5)
status_frame = ttk.Frame(root, relief='raised').pack(fill='x')
label_status = ttk.Label(root,text='状态栏').pack(side='left', fill='x')
# 设置分割线和框架空间
pw_1 = tk.PanedWindow(pw, orient='horizontal', sashrelief='sunken')
pw_2 = tk.PanedWindow(pw, orient='horizontal', sashrelief='sunken')
left_frame,right_frame,bottom_frame = \
    ttk.Frame(pw_1, width=100, relief='flat'), \
    ttk.Frame(pw_1, height=200, relief='flat'), \
    ttk.Frame(pw_2, relief='flat')
# 将面板和分割线添加到窗口
pw.add(pw_1),pw.add(pw_2),
pw_1.add(left_frame),pw_1.add(right_frame),pw_2.add(bottom_frame)


root.mainloop()
