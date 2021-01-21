#-*- coding:utf-8 -*-

import tkinter as tk
import tkinter.ttk as ttk
import time
import threading

def progressfun():
    for i in range(100):
        progressbar1['value'] += 1
        root.update()
        time.sleep(0.03)

def progressfun2():
    progressbar2.start(interval=20)
    progressbar2.step(amount=1.0)
    def func():
        progressbar2.stop()
    threading.Timer(5, func).start()

root = tk.Tk(className='Tk的所有控件测试')
root.geometry('400x600+100+100')
button = ttk.Button(root, text='按钮, 3秒', command=progressfun)
button2 = ttk.Button(root, text='按钮2, 5秒', command=progressfun2)
# Tk进度条Progressbar使用介绍：https://blog.csdn.net/weixin_42272768/article/details/100876613
# 17.进度条Progressbar(类似安装程序的进度条)
# 有2种mode(determinate,indeterminate),maximum进度条最大刻度值
progressbar1, progressbar2 = \
    ttk.Progressbar(root, orient='horizontal', value=0, maximum=100, length=200, mode='determinate'),\
    ttk.Progressbar(root, orient='horizontal', value=0, length=200, mode='indeterminate')
label1, label2 = ttk.Label(root, text=str(progressbar1['variable'])+'%'),\
    ttk.Label(root, text=str(progressbar2['variable'])+'%')

# 控件布局
button.pack(pady=2), progressbar1.pack(pady=2), label1.pack(pady=2),\
button2.pack(pady=2), progressbar2.pack(pady=2), label2.pack(pady=2)

root.mainloop()
