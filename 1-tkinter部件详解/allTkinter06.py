#-*- coding:utf-8 -*-

import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk(className='Tk的所有控件测试')
root.geometry('400x600+100+100')
# 18.单选按钮Menubutton(类似于15下拉列表OptionMenu，但18多了一些单选、复选、命名的菜单功能)
menubutton = ttk.Menubutton(root, text='单选按钮')
separator = ttk.Separator(root)
# 设置子菜单列表并绑定主菜单
mb_menu = tk.Menu(menubutton, tearoff=0)
mb_menu.add_command(label='命令按钮'),mb_menu.add_separator(),\
mb_menu.add_radiobutton(label='单选按钮1'), mb_menu.add_radiobutton(label='单选按钮2'), mb_menu.add_radiobutton(label='单选按钮3'),\
mb_menu.add_checkbutton(label='复选按钮[Y/N]'), mb_menu.add_separator(),\
mb_menu.add_command(label='退出', command=root.destroy)
# 主菜单绑定子菜单
menubutton.config(menu=mb_menu)

# 控件布局
menubutton.pack(), separator.pack(fill='x',padx=5)

root.mainloop()
