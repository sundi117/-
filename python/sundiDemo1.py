#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:sundi

import tkinter as tk
import tkinter.messagebox
import pickle

# 1）实例化object，建立窗口window
window = tk.Tk( )

# 2）给窗口的可视化起名字
window.title('csv批量操作工具')

# 3）定义应用程序窗口的宽高
window_width = 600
window_height = 200

# 4）为了让窗口在屏幕居中，使用一下算法
# 获取屏幕宽度
sw = window.winfo_screenwidth()
# 获取屏幕高度
sh = window.winfo_screenheight()
# 配置窗口的宽高和位置
x = (sw - window_width) / 2
y = (sh - window_height) / 2
window.geometry("%dx%d+%d+%d" % (window_width, window_height, x, y))

# 点击“执行”事件
def fuck():
    print("what a fucking day！！！")


frame1 = tk.Frame(window,width = 20 ,height =1 )
frame1.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)
label2 = tk.Label(window, text="请输入经纬度坐标的范围",  fg='black', font=('Arial', 12) , height=1)
label2.pack(side=tk.TOP, fill=tk.X, expand=tk.YES)


frame2 = tk.Frame(window ,height =1 )
frame2.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES,padx=120)
entry2_1 = tk.Entry(frame2, show=None, font=('Arial', 12) ,width = 15   ).pack(side=tk.LEFT, fill=tk.X, expand=tk.YES)
label2_1 = tk.Label(frame2, text=" < lat < ",  fg='black', font=('Arial', 12), height=1).pack(side=tk.LEFT, fill=tk.X, expand=tk.YES)
entry2_2 = tk.Entry(frame2, show=None, font=('Arial', 12),width = 15  ).pack(side=tk.LEFT, fill=tk.X, expand=tk.YES)

frame3 = tk.Frame(window ,height =1 )
frame3.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES,padx=120)
entry3_1 = tk.Entry(frame3, show=None, font=('Arial', 12) ,width = 15   ).pack(side=tk.LEFT, fill=tk.X, expand=tk.YES)
label3_1 = tk.Label(frame3, text=" < lon < ",  fg='black', font=('Arial', 12), height=1).pack(side=tk.LEFT, fill=tk.X, expand=tk.YES)
entry3_2 = tk.Entry(frame3, show=None, font=('Arial', 12),width = 15  ).pack(side=tk.LEFT, fill=tk.X, expand=tk.YES)


frame4 = tk.Frame(window ,height =1 )
frame4.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES,padx=120)
button4_1 = tk.Button(frame4, text='执行', command=fuck, width=10, height=1 ).pack(side=tk.RIGHT, expand=tk.YES)


# label2.pack(side=tk.TOP, fill=tk.X, expand=tk.YES)




'''
tk.Label(frame2, text='P', fg='red').pack(side='top')    # 上
tk.Label(frame2, text='P', fg='red').pack(side='bottom') # 下
tk.Label(frame2, text='P', fg='red').pack(side='left')   # 左
tk.Label(frame2, text='P', fg='red').pack(side='right')  # 右
'''





# 第10步，主窗口循环显示
window.mainloop()
