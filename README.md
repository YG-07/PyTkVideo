# PyTkVideo
a python desktop video program by the tkinter package

# 资料来源
1. 桌面视频URL解析程序 B站视频：https://www.bilibili.com/video/BV1GA411H7Nr
2. tkinter部件详解 B站视频：https://www.bilibili.com/video/BV1nZ4y1M7F6
3. python的GUI编程之tkinter B站视频：https://www.bilibili.com/video/BV1zE411g7LY?p=1

# Tk案例：画图程序思路
## 一、程序基本结构
### 1.1 使用Tk程序的class封装代码
### 1.2 创建组件
1. 创建画布Canvas，并pack布局，fill横纵轴
```python
self.c = Canvas(self.master, width=450, height=280, bg='#fff')
self.c.pack(fill='both',expand=1)
```
2. 创建各种画图和功能按钮
## 二、处理事件
### 2.1 鼠标事件处理
```python
self.master.bind_class('Button','<1>', self.eventMag)
self.c.bind('<ButtonRelease-1>', self.stopDraw)
```
### 2.2 实现事件管理函数eventMag
```python
# 画图功能函数,事件管理
def eventMag(self, event):
    name = event.widget.winfo_name()
    print(name)
    # 1.画直线
    if name=='line':
        self.c.bind('<B1-Motion>', self.myLine)
```
#### 2.2.1 画直线思路
1. 监听鼠标按住事件`myline()`
2. 先假设从(0,0)开始画线，①先解决重复画线的问题，通过设置一个`lastLine`返回每次画的线，每次调用按住事件时删除一个上一次的线.
3. ②再解决开始画线坐标问题，再设置一个`startLine`的布尔值,在第一次调用按住事件获取点击事件的坐标(x,y),再改变startLine的值.
4. ③解决释放按键后，可以重新开始画线，设置一个`stopDraw`绑定释放鼠标事件，将`startLine和lastLine设置为初始值`
```python
def myLine(self, event):
    self.c.delete(self.lastLine)
    if not self.startLine:
        self.startLine = True
        self.sx = event.x
        self.sy = event.y
    self.lastLine=self.c.create_line(self.sx, self.sy, event.x, event.y, fill=self.v1)
def stopDraw(self, event):
    self.startLine = False
    self.lastLine = 0
```
#### 2.2.2 箭头直线思路
1. 跟画直线结果一模一样，只用在`create_line`函数里添加`arrow=LAST`参数，表示在直线结束添加箭头
2. 将画直线的共同的代码封装成startDraw函数
```python
def myArrLine(self, event):
    self.startDraw(event)
    self.lastLine=self.c.create_line(self.sx, self.sy, event.x, event.y, arrow=LAST, fill=self.v1)
```