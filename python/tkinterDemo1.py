#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:sundi
 
import tkinter as tk  # 使用Tkinter前需要先导入
 
# 第1步，实例化object，建立窗口window
window = tk.Tk()

# 第2步，给窗口的可视化起名字
window.title('给窗口起个名字')

# 定义应用程序窗口的宽高
window_width  = 600
window_height = 500

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
Label:标签控件,可以显示文本
'''
# window：父窗体
# text：显示的文本内容
# bg：背景色
# fg：字体颜色
# font：字体
# width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高
# wraplength：指定text文本中多宽之后换行
# justify：设置换行后的对齐方式
# anchor：位置 n北，e东，w西，s南，center居中；还可以写在一起：ne东北方向
label = tk.Label(window,
                      text="这是标签控件blabla",
                      bg="pink", fg="red",
                      font=("黑体", 20),
                      width=20,
                      height=3,
                      wraplength=100,
                      justify="center",
                      anchor="center")
# 第5步，放置标签
# Label内容content区域放置位置，自动调节尺寸
# 放置lable的方法有：1）l.pack(); 2)l.place();
label.pack()  

################################################################################################################ 

'''
Button：按钮控件
'''
# 按钮点击事件
def fuckyou():
    print("what a fucking day！！！")

# 创建按钮
button1 = tk.Button(window, text="fuckyou", command=fuckyou, width=10, height=3)
button1.pack()

button2 = tk.Button(window, text="卧槽", command=lambda: print("一句卧槽走天下"))
button2.pack()

button3 = tk.Button(window, text="退出", command=window.quit)
button3.pack()


# 将label标签的内容设置为字符类型，用var来接收hit_me函数的传出内容用以显示在标签上
var = tk.StringVar()    
label2 = tk.Label(window, textvariable=var, bg='green', fg='white', font=('Arial', 12), width=30, height=2)
label2.pack()
 
# 定义一个函数功能（内容自己自由编写），供点击Button按键时调用，调用命令参数command=函数名
on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('fuck me ~')
    else:
        on_hit = False
        var.set('')

button4 = tk.Button(window, text='hit me', font=('Arial', 12), width=10, height=1, command=hit_me)
button4.pack()


################################################################################################################

'''
Entry：单行文本输入框控件
'''
# 第4步，在图形界面上设定输入框控件entry并放置控件
entry1 = tk.Entry(window, show='*', font=('Arial', 14))   # 显示成密文形式
entry2 = tk.Entry(window, show=None, font=('Arial', 14))  # 显示成明文形式
entry1.pack()
entry2.pack()

################################################################################################################

'''
Text：多行文本域控件
'''
entry3 = tk.Entry(window, show = None)
entry3.pack()
 
# 定义两个触发事件时的函数insert_point和insert_end
#（注意：因为Python的执行顺序是从上往下，所以函数一定要放在按钮的上面）
	# 在鼠标焦点处插入输入内容
def insert_point(): 
    var = entry3.get()
    text1.insert('insert', var)
	# 在文本框内容最后接着插入输入内容   
def insert_end():   
    var = entry3.get()
    text1.insert('end', var)
 
# 第6步，创建并放置两个按钮分别触发两种情况
b1 = tk.Button(window, text='在某处插入', width=10,
               height=2, command=insert_point)
b1.pack()
b2 = tk.Button(window, text='在末尾插入', width=10,
               height=2, command=insert_end)
b2.pack()
 
# 第7步，创建并放置一个多行文本框text用以显示，指定height=3为文本框是三个字符高度
text1 = tk.Text(window, height=3)
text1.pack()


################################################################################################################
# 第6步，主窗口循环显示
# 注意，loop因为是循环的意思，window.mainloop就会让window不断的刷新，如果没有mainloop,就是一个静态的window,
# 传入进去的值就不会有循环，mainloop就相当于一个很大的while循环，有个while，每点击一次就会更新一次，所以我们必须要有循环
# 所有的窗口文件都必须有类似的mainloop函数，mainloop是窗口文件的关键的关键。
window.mainloop()
