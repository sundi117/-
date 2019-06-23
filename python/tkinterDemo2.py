#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:sundi
 
import tkinter as tk  # 使用Tkinter前需要先导入

################################################################################################################ 
'''
1、初始化windows frame

'''
 
# 1）实例化object，建立窗口window
window = tk.Tk()

# 2）给窗口的可视化起名字
window.title('给窗口起个名字')

# 3）定义应用程序窗口的宽高
window_width  = 800
window_height = 600

# 4）为了让窗口在屏幕居中，使用一下算法
# 获取屏幕宽度
sw = window.winfo_screenwidth()
# 获取屏幕高度
sh = window.winfo_screenheight()
# 配置窗口的宽高和位置
x = (sw-window_width) / 2
y = (sh-window_height) / 2
window.geometry("%dx%d+%d+%d" %(window_width,window_height,x,y))


################################################################################################################ 
'''
2、组件
2.11   Frame :框架容器
'''

# 1) 语法糖！支持链式操作！
tk.Label(window, text='on the window', bg='red', font=('Arial', 16)).pack()   # 和前面部件分开创建和放置不同，其实可以创建和放置一步完成
 
# 2）创建一个主frame，长在主window窗口上
frame = tk.Frame(window)
frame.pack() 


# 3）创建第二层框架frame，长在主框架frame上面
frame_l = tk.Frame(frame)# 第二层frame，左frame，长在主frame上
frame_r = tk.Frame(frame)# 第二层frame，右frame，长在主frame上
frame_l.pack(side='left')
frame_r.pack(side='right')
 
# 4）创建三组标签，为第二层frame上面的内容，分为左区域和右区域，用不同颜色标识
tk.Label(frame_l, text='on the frame_l1', bg='green').pack()
tk.Label(frame_l, text='on the frame_l2', bg='green').pack()
tk.Label(frame_l, text='on the frame_l3', bg='green').pack()
tk.Label(frame_r, text='on the frame_r1', bg='yellow').pack()
tk.Label(frame_r, text='on the frame_r2', bg='yellow').pack()
tk.Label(frame_r, text='on the frame_r3', bg='yellow').pack()

################################################################################################################ 
'''
2.12 messageBox：弹框
'''
import tkinter.messagebox  # 要使用messagebox一定先要导入模块！！！

# 1）定义触发函数功能
def click():
    tkinter.messagebox.showinfo(title='Hi', message='你好！')              # 提示信息对话窗
    # tkinter.messagebox.showwarning(title='Hi', message='有警告！')       # 提出警告对话窗
    # tkinter.messagebox.showerror(title='Hi', message='出错了！')         # 提出错误对话窗
    # print(tkinter.messagebox.askquestion(title='Hi', message='你好！'))  # 询问选择对话窗return 'yes', 'no'
    # print(tkinter.messagebox.askyesno(title='Hi', message='你好！'))     # return 'True', 'False'
    # print(tkinter.messagebox.askokcancel(title='Hi', message='你好！'))  # return 'True', 'False'
 
# 2）在图形界面上创建一个标签用以显示内容并放置
tk.Button(window, text='点我呀', bg='green', font=('Arial', 14), command=click).pack()


################################################################################################################ 

'''
2.13  窗口组件的三种布局方式：pack/grid/place
'''

'''
anchor：当可用空间大于组件所需求的大小时，该选项决定组件被放置在容器的何处。该选项支持 N（北，代表上）、E（东，代表右）、S（南，代表下）、W（西，代表左）、NW（西北，代表左上）、NE（东北，代表右上）、SW（西南，代表左下）、SE（东南，代表右下）、CENTER（中，默认值）这些值。
expand：该 bool 值指定当父容器增大时才是否拉伸组件。
fill：设置组件是否沿水平或垂直方向填充。该选项支持 NONE、X、Y、BOTH 四个值，其中 NONE 表示不填充，BOTH 表示沿着两个方向填充。
ipadx：指定组件在 x 方向（水平）上的内部留白（padding）。
ipady：指定组件在 y 方向（水平）上的内部留白（padding）。
padx：指定组件在 x 方向（水平）上与其他组件的间距。
pady：指定组件在 y 方向（水平）上与其他组件的间距。
side：设置组件的添加位置，可以设置为 TOP、BOTTOM、LEFT 或 RIGHT 这四个值的其中之一。
'''

# 1）创建一个主frame，长在主window窗口上
frame2 = tk.Frame(window)
frame2.pack() 

# 2）pack 放置方法
tk.Label(frame2, text='P', fg='red').pack(side='top')    # 上
tk.Label(frame2, text='P', fg='red').pack(side='bottom') # 下
tk.Label(frame2, text='P', fg='red').pack(side='left')   # 左
tk.Label(frame2, text='P', fg='red').pack(side='right')  # 右


# 未完待续。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。

################################################################################################################
'''
3、 主窗口循环显示

'''

# 注意，loop因为是循环的意思，window.mainloop就会让window不断的刷新，如果没有mainloop,就是一个静态的window,
# 传入进去的值就不会有循环，mainloop就相当于一个很大的while循环，有个while，每点击一次就会更新一次，所以我们必须要有循环
# 所有的窗口文件都必须有类似的mainloop函数，mainloop是窗口文件的关键的关键。
window.mainloop()
