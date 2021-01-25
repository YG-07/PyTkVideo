#-*- coding:utf-8 -*-
from sys import getsizeof
from tkinter import messagebox
from tkinter.colorchooser import askcolor
from tkinter.filedialog import *
from tkinter.messagebox import *

# 方法一：pyinstaller打包指令
'''
pyinstaller -F mynote.py -i mynote.ico -n MyNote.exe
'''
# 方法二 使用pipenv打包，安装(国内镜像)：
# pip3 install pipenv -i https://pypi.tuna.tsinghua.edu.cn/simple

class Application(Frame):
    # 一个经典的GUI程序
    def __init__(self, master=None):
        super().__init__(master)    #super()是父类的构造器
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        # 创建组件,创建主菜单
        menubar = Menu(self)

        # 创建子菜单,tearoff为0关闭工具栏
        mFile = Menu(menubar, tearoff=0)
        mEdit = Menu(menubar, tearoff=0)
        mHelp = Menu(menubar, tearoff=0)

        # 并加入主菜单
        menubar.add_cascade(label='文件(F)', menu=mFile)
        menubar.add_cascade(label='编辑(E)', menu=mEdit)
        menubar.add_cascade(label='帮助(H)', menu=mHelp)

        # 1.添加[文件]的子菜单项
        mFile.add_command(label='新建', accelerator='Ctrl+N', command=self.newfile)
        mFile.add_command(label='打开', accelerator='Ctrl+O', command=self.open)
        mFile.add_command(label='保存', accelerator='Ctrl+S', command=self.save)
        mFile.add_command(label='另存为', command=self.saveAs)

        mFile.add_separator()
        mFile.add_command(label='退出', accelerator='Alt+F4', command=self.quit)

        # 2.添加[编辑]的子菜单项
        mEdit.add_command(label='字体增大', accelerator='Ctrl + +', command=lambda :self.chgFont(True,5))
        mEdit.add_command(label='字体缩小', accelerator='Ctrl + -', command=lambda :self.chgFont(False,5))


        # 3.添加[帮助]的子菜单项
        mHelp.add_command(label='关于', command=self.about)

        # 将菜单添加到主窗口
        self.master.config(menu=menubar)

        # 文本编辑区
        self.textpad = Text(self.master, font=('宋体', 17))
        self.textpad.pack(fill='both', expand=1)

        # 创建[上下文](右键)菜单项
        self.contextMenu = Menu(self, tearoff=0)
        self.contextMenu.add_command(label='背景颜色', command=lambda :self.chgColor('bg'))
        self.contextMenu.add_command(label='字体颜色', command=lambda :self.chgColor('fg'))

        # 增加快捷键事件处理
        self.master.bind('<Control-n>', lambda event: self.newfile())
        self.master.bind('<Control-o>', lambda event: self.open())
        self.master.bind('<Control-s>', lambda event: self.save())
        self.master.bind('<Control-F4>', lambda event: self.quit())
        self.master.bind('<Control-plus>', lambda event: self.chgFont(True))
        self.master.bind('<Control-minus>', lambda event: self.chgFont(False))


        # 右键绑定事件
        self.master.bind('<Button-3>', self.createContextMenu)

    def createContextMenu(self, event):
        self.contextMenu.post(event.x_root, event.y_root)

    # 子菜单事件函数
    def newfile(self):
        if not getsizeof(self.textpad.get(1.0, END))==50:
            flag = askquestion(title='保存文件', message='是否先保存文件？')
            if flag=='yes':
                self.saveAs()
            self.textpad.delete(1.0, END)
        self.saveAs()


    def open(self):
        with askopenfile(title='打开文本文件') as f:
            self.textpad.replace(1.0,END,f.read())


    def save(self):
        with open(self.filename, 'w') as f:
            tmp = self.textpad.get(1.0, END)
            f.write(tmp)

    def saveAs(self):
        self.filename = asksaveasfilename(title='保存文件到', initialfile='未命名.txt', \
            filetypes=[('文本文档', '*.txt')], defaultextension='.txt')
        if not self.filename == '':
            self.save()

    def exit(self):
        self.master.destroy()

    def chgFont(self, bool, dlt=1):
        resfont = self.textpad['font'].split(' ')
        tmp = int(resfont[1])
        if bool:
            tmp+=dlt
        else:
            if(tmp-dlt>=8):
                tmp-=dlt
            else:
                tmp=8
        resfont[1] = str(tmp)
        resfont = ' '.join(resfont)
        self.textpad['font'] = resfont

    def about(self):
        messagebox.showinfo(title='帮助和关于', message='哈哈哈')

    def chgColor(self, verb):
        s1 = askcolor(color='green', title='选择新的颜色')
        self.textpad[verb]=s1[1]


if __name__ == '__main__':
    root = Tk()
    root.title('自定义记事本程序')
    root.geometry('700x730+700+160')
    app = Application(master=root)
    root.mainloop()