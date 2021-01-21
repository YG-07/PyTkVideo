#-*- coding:utf-8 -*-

import tkinter as tk
import tkinter.ttk as ttk
import tkinter.scrolledtext

root = tk.Tk(className='Tk的所有控件测试')
root.geometry('400x600+100+100')

# 22.带滚动条的文本框ScrolledText(类似记事本功能)
text = tkinter.scrolledtext.ScrolledText(root, height=5)

# 控件布局
text.pack(fill='both', expand=1)


root.mainloop()
