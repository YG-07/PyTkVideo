#-*- coding:utf-8 -*-

import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk(className='Tk的所有控件测试')
root.geometry('400x600+100+100')
# 19.树型视图Treeview
treeview_sheet = ttk.Treeview(root, height=10, columns=('图标栏'), selectmode='extended')
treeview_sheet.heading('#0', text='图标栏1'), treeview_sheet.heading('#1', text='图标栏2')
for i in range(30):
    treeview_sheet.insert('', index='end', text=i, values=i*2)
treeview_tree = ttk.Treeview(root, height=10, show='tree')
treeview_tree_parents = treeview_tree.insert('', index='end', text='结构树')
for i in range(30):
    treeview_tree.insert(treeview_tree_parents, index='end', text=i+1)

# 表格的元素，索引'I'+000(16进制数)
# print(treeview_sheet.get_children())


# 控件布局
treeview_sheet.pack(side='left', padx=5), treeview_tree.pack(side='left', padx=5)

root.mainloop()
