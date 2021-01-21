#-*- coding:utf-8 -*-

from tkinter.tix import *

window = Tk()
window.title('Tix的部件详解')
window.geometry('1550x930+165+50')
# window.state('zoomed')  # 直接最大化

# 1.添加带滚动条的窗口
scrolledwindow = ScrolledWindow(window, scrollbar='both')   #x、y滚动条
scrolledwindow.pack(fill='both', expand=1)

button = Button(scrolledwindow, text='状态栏按钮')
button.grid(row=1, column=0, padx=5, pady=5)

# 2.用气泡建立状态栏
status_frame = Frame(window, height=20)
status_frame.pack(side='bottom', fill='x')
status_label_name = Label(status_frame, text='状态栏')
status_label_name.pack(side='left',padx=5)
status_label = Label(status_frame, text='')
status_label.pack(side='left', padx=20)
# 3.建立气泡
balloon = Balloon(scrolledwindow, statusbar=status_label)
balloon.bind_widget(button, balloonmsg='一个按钮', statusmsg='一个按钮')

# 4.建立层级列表
hlist = HList(scrolledwindow, height=15, width=20)
hlist.grid(row=1, column=0, padx=5, pady=5)
# 添加子项
hlist.add('CL1', text='水果')
hlist.add('CL1.Item1',text='苹果'),\
hlist.add('CL1.Item2',text='香蕉'),\
hlist.add('CL1.Item3',text='桃子')

# 5.选择列表
checklist = CheckList(scrolledwindow, options='hlist.columns1',\
    highlightthickness=3, highlightcolor='pink')
checklist.grid(row=2, column=0, padx=5, pady=5)
# 配置列表
checklist.hlist.config(bg='yellow', bd=1, drawbranch=True, pady=5, header=True)
# 创建表头和项目
checklist.hlist.header_create(0, itemtype='text', text='表头')
checklist.hlist.add('CL1', text='选择列表')
checklist.hlist.add('CL1.Item1', text='项目1'),\
checklist.hlist.add('CL1.Item2', text='项目2'),\
checklist.hlist.add('CL1.Item3', text='项目3')
checklist.setstatus("CL1","on")
checklist.setstatus("CL1.Item1","off")

# 6.按钮框
buttonbox = ButtonBox(scrolledwindow, height=20, width=20)
buttonbox.grid(row=3, column=0, padx=5, pady=5)
# 添加按钮
buttonbox.add('ok', text='确定'),buttonbox.add('cancel', text='取消'),\
buttonbox.add('sleep', text='睡觉')

# 7.下拉式列表
combobox = ComboBox(scrolledwindow, editable=True, history=True)
combobox.grid(row=4, column=0, padx=5, pady=5)

# 8.选值按钮
control = Control(scrolledwindow, label='标签输入')
control.grid(row=5, column=0, padx=5, pady=5)

# 9.带有标签的输入框
labelentry = LabelEntry(scrolledwindow, label='标签输入')
labelentry.grid(row=6, column=0, padx=5, pady=5)

# 10.进度条
meter = Meter(scrolledwindow)
meter.grid(row=7, column=0, padx=5, pady=5)

# 11.选择按钮
optionmenu = OptionMenu(scrolledwindow)
optionmenu.add_command('item1', label='选项1'),\
optionmenu.add_command('item2', label='选项2'),\
optionmenu.add_command('item3', label='选项3')
optionmenu.grid(row=0, column=1, padx=5, pady=5)

# 12.文件选择器
# 列表目录文件夹
dirlist = DirList(scrolledwindow, width=200, height=240)
dirlist.grid(row=1, column=1, padx=5, pady=5)
# 树形目录文件夹
dirtree = DirTree(scrolledwindow, width=200, height=240)
dirtree.grid(row=2, column=1, padx=5, pady=5)
# 目录选择器
dirselectbox = DirSelectBox(scrolledwindow)
dirselectbox.grid(row=1, column=2, padx=5, pady=5)
# 文件选择器
exfileselectbox = ExFileSelectBox(scrolledwindow)
exfileselectbox.grid(row=2, column=2, padx=5, pady=5)
fileselectbox = FileSelectBox(scrolledwindow)
fileselectbox.grid(row=1, column=3, padx=5, pady=5)
fileentry = FileEntry(scrolledwindow)
fileentry.grid(row=2, column=3, padx=5, pady=5)

window.mainloop()