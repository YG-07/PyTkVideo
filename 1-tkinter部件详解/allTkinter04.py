#-*- coding:utf-8 -*-

import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk(className='Tk的所有控件测试')
root.geometry('400x600+100+100')
# 15.下拉式列表OptionMenu(类似下拉的菜单)
# 16.组合框Combobox(类似下拉的选项框)
stringvar1, stringvar2 = tk.StringVar(), tk.StringVar()
optionmenu = ttk.OptionMenu(root, stringvar1, 'Python', 'Python', 'java', 'C\C++')
combobox = ttk.Combobox(root, textvariable=stringvar2, values=('Python', 'java', 'C\C++'))
# 控件布局
optionmenu.pack(pady=2), combobox.pack(pady=2)

root.mainloop()
