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
2.1 Label:标签控件,可以显示文本
'''

# 1) 配置项
# window：父窗体
# text：显示的文本内容
# bg：背景色
# fg：字体颜色
# font：字体
# width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高
# wraplength：指定text文本中多宽之后换行
# justify：设置换行后的对齐方式
# anchor：位置 n北，e东，w西，s南，center居中；还可以写在一起：ne东北方向
'''
label = tk.Label(window,
                      text="这是标签控件blabla",
                      bg="pink", fg="red",
                      font=("黑体", 20),
                      width=15,
                      height=2,
                      wraplength=100,
                      justify="center",
                      anchor="center")
# 2）放置标签
# Label内容content区域放置位置，自动调节尺寸
# 放置lable的方法有：1）l.pack(); 2)l.place();
label.pack()  
'''

################################################################################################################ 

'''
2.2 Button：按钮控件
'''

'''
# 1）按钮点击事件
def fuck():
    print("what a fucking day！！！")

# 2）创建按钮
button1 = tk.Button(window, text="说点啥呢？", command=fuck, width=10, height=1)
button1.pack()

button2 = tk.Button(window, text="卧槽", command=lambda: print("一句卧槽走天下"))
button2.pack()

button3 = tk.Button(window, text="退出", command=window.quit)
button3.pack()


# 3）将label标签的内容设置为字符类型，用var来接收hit_me函数的传出内容用以显示在标签上
var = tk.StringVar()    
label2 = tk.Label(window, textvariable=var, bg='green', fg='white', font=('Arial', 12), width=30, height=1)
label2.pack()
 
# 4） 定义一个函数的小demo
# 定义一个函数功能（内容自己自由编写），供点击Button按键时调用，调用命令参数command=函数名
on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('听过了许多道理，依然过不好这一生~')
    else:
        on_hit = False
        var.set('')

button4 = tk.Button(window, text='点我告诉你', font=('Arial', 12), width=10, height=1, command=hit_me)
button4.pack()
'''

################################################################################################################

'''
2.3 Entry：单行文本输入框控件
'''

# 1） 在图形界面上设定输入框控件entry并放置控件
'''
entry1 = tk.Entry(window, show='*', font=('Arial', 14))   # 显示成密文形式
entry2 = tk.Entry(window, show=None, font=('Arial', 14))  # 显示成明文形式
entry1.pack()
entry2.pack()

'''

################################################################################################################

'''
2.4 Text：多行文本域控件
'''
# 1） 这个其实没啥用
entry3 = tk.Entry(window, show = None)
entry3.pack()
 
# 2）定义两个触发事件时的函数insert_point和insert_end
#（注意：因为Python的执行顺序是从上往下，所以函数一定要放在按钮的上面）
	# 在鼠标焦点处插入输入内容
def insert_point(): 
    var = entry3.get()
    text1.insert('insert', var)
	# 在文本框内容最后接着插入输入内容   
def insert_end():   
    var = entry3.get()
    text1.insert('end', var)
 
# 3）创建并放置两个按钮分别触发两种情况
b1 = tk.Button(window, text='在某处插入', width=10,
               height=1, command=insert_point)
b1.pack()
b2 = tk.Button(window, text='在末尾插入', width=10,
               height=1, command=insert_end)
b2.pack()
 
# 4) 创建并放置一个多行文本框text用以显示，指定height=3为文本框是三个字符高度
text1 = tk.Text(window, height=3)
text1.pack()


################################################################################################################
'''
2.5 tk.StringVar()用法
	在这里单独讲一下StringVar的用法。
	简单来说，就是在tkinter的作用域内定义一个全局变量为tk.StringVar()。可以用来随时接受字符串。
'''

'''
str1 = tk.StringVar()
str1.set("天青色等烟雨")
print(str1.get())
str1.set( str(input("请输入：")) )
print(str1.get())
'''

################################################################################################################

'''
2.6 Listbox窗口部件
'''

# 1) 创建Listbox及其选项
var2 = tk.StringVar()
var2.set((1,2,3,4)) 
# 创建Listbox
listBox = tk.Listbox(window, listvariable=var2)  #将var2的值赋给Listbox

# 2）动态增加选项
list_items = ['西安','成都','武汉','南京']
for item in list_items:
    listBox.insert('end', item)  # 从最后一个位置开始加入值
listBox.insert(1, 'first')       # 在第一个位置加入'first'字符
listBox.insert(2, 'second')      # 在第二个位置加入'second'字符
listBox.delete(2)                # 删除第二个位置的字符
listBox.pack()

# 3) 测试选中选项的变量值
var1 = tk.StringVar()  
label3 = tk.Label(window, bg='green', fg='yellow',font=('Arial', 12), width=10, textvariable=var1)
label3.pack()
# 	 按钮点击事件
def print_selection():
    value = listBox.get(listBox.curselection())   # 获取当前选中的文本
    var1.set(value)  
# 	 创建按钮
b1 = tk.Button(window, text='print selection', width=15, height=2, command=print_selection)
b1.pack()
 

################################################################################################################

'''
2.7 Radiobutton：单选按钮
'''

# 1）创建三个radiobutton选项，其中variable=var, value='A'的意思就是，当我们鼠标选中了其中一个选项，
#    把value的值A放到变量var中，然后赋值给variable
#    一组单选框要绑定同一个变量，就能区分出单选框了
r1 = tk.Radiobutton(window, text='Option A', variable=var1, value='A', command=print_selection)
r1.pack()
r2 = tk.Radiobutton(window, text='Option B', variable=var1, value='B', command=print_selection)
r2.pack()
r3 = tk.Radiobutton(window, text='Option C', variable=var1, value='C', command=print_selection)
r3.pack()


################################################################################################################

'''
2.8 Checkbutton：多选框
'''

# 1） 创建一个标签label用来显示——测试
l = tk.Label(window, bg='yellow', width=20, text='empty')
l.pack()

# 2） 定义触发函数功能
def print_selection():
    if (varCheckbutton1.get() == 1) & (varCheckbutton2.get() == 0):     # 如果选中第一个选项，未选中第二个选项
        l.config(text='我要华为手机 ')
    elif (varCheckbutton1.get() == 0) & (varCheckbutton2.get() == 1):   # 如果选中第二个选项，未选中第一个选项
        l.config(text='我要小米手机')
    elif (varCheckbutton1.get() == 0) & (varCheckbutton2.get() == 0):   # 如果两个选项都未选中
        l.config(text='我没钱，都不要')
    else:
        l.config(text='不差钱，全买')             # 如果两个选项都选中
 
# 3） 定义两个Checkbutton选项并放置
varCheckbutton1 = tk.IntVar()  # 定义var1和var2整型变量用来存放选择行为返回值
varCheckbutton2 = tk.IntVar()
c1 = tk.Checkbutton(window, text='华为手机',variable=varCheckbutton1, onvalue=1, offvalue=0, command=print_selection)   
c1.pack()
c2 = tk.Checkbutton(window, text='小米手机',variable=varCheckbutton2, onvalue=1, offvalue=0, command=print_selection)
c2.pack()

################################################################################################################

'''
2.9  Scale：滑块条
'''

# 1） 在图形界面上创建一个标签label用以显示并放置
l2 = tk.Label(window, bg='green', fg='white', width=20, text='empty')
l2.pack()
 
# 2） 定义一个触发函数功能
def print_selection(v):
    l2.config(text='you have selected ' + v)
# 3） 创建一个尺度滑条，长度200字符，从0开始10结束，以2为刻度，精度为0.01，触发调用print_selection函数
s = tk.Scale(window, label='try me', from_=0, to=10, orient=tk.HORIZONTAL, length=200, showvalue=0,tickinterval=2, resolution=0.01, command=print_selection)
s.pack()


################################################################################################################

'''
2.10  Canvas： 画布
'''

# 这个模块暂时不用

'''
# 1）在图形界面上创建 500 * 200 大小的画布并放置各种元素
canvas = tk.Canvas(window, bg='green', height=200, width=500)
# 2） 说明图片位置，并导入图片到画布上
image_file = tk.PhotoImage(file='pic.gif')  # 图片位置（相对路径，与.py文件同一文件夹下，也可以用绝对路径，需要给定图片具体绝对路径）
image = canvas.create_image(250, 0, anchor='n',image=image_file)        # 图片锚定点（n图片顶端的中间点位置）放在画布（250,0）坐标处
# 3） 定义多边形参数，然后在画布上画出指定图形
x0, y0, x1, y1 = 100, 100, 150, 150
line = canvas.create_line(x0-50, y0-50, x1-50, y1-50)                   # 画直线
oval = canvas.create_oval(x0+120, y0+50, x1+120, y1+50, fill='yellow')  # 画圆 用黄色填充
arc = canvas.create_arc(x0, y0+50, x1, y1+50, start=0, extent=180)      # 画扇形 从0度打开收到180度结束
rect = canvas.create_rectangle(330, 30, 330+20, 30+20)                  # 画矩形正方形
canvas.pack()
 
# 4） 触发函数，用来一定指定图形
def moveit():
    canvas.move(rect, 2, 2) # 移动正方形rect（也可以改成其他图形名字用以移动一起图形、元素），按每次（x=2, y=2）步长进行移动
 
# 5） 定义一个按钮用来移动指定图形的在画布上的位置
b = tk.Button(window, text='move item',command=moveit).pack()
'''

################################################################################################################

'''
2.11  Menu ： 菜单项
'''

# 1) 在图形界面上创建一个标签用以显示内容并放置
lMenu = tk.Label(window, text='      ', bg='green')
lMenu.pack()
 
# 2) 定义一个函数功能，用来代表菜单选项的功能，这里为了操作简单，定义的功能比较简单
counter = 0
def do_job():
    global counter
    lMenu.config(text='do '+ str(counter))
    counter += 1
 
# 3) 创建一个菜单栏，这里我们可以把他理解成一个容器，在窗口的上方
menubar = tk.Menu(window)
 
# 4) 创建一个File菜单项（默认不下拉，下拉内容包括New，Open，Save，Exit功能项）
filemenu = tk.Menu(menubar, tearoff=0)
#    将上面定义的空菜单命名为File，放在菜单栏中，就是装入那个容器中
menubar.add_cascade(label='File', menu=filemenu)
 
# 5) 在File中加入New、Open、Save等小菜单，即我们平时看到的下拉菜单，每一个小菜单对应命令操作。
filemenu.add_command(label='New', command=do_job)
filemenu.add_command(label='Open', command=do_job)
filemenu.add_command(label='Save', command=do_job)
filemenu.add_separator()    # 添加一条分隔线
filemenu.add_command(label='Exit', command=window.quit) # 用tkinter里面自带的quit()函数
 
# 6) 创建一个Edit菜单项（默认不下拉，下拉内容包括Cut，Copy，Paste功能项）
editmenu = tk.Menu(menubar, tearoff=0)
#    将上面定义的空菜单命名为 Edit，放在菜单栏中，就是装入那个容器中
menubar.add_cascade(label='Edit', menu=editmenu)
 
# 	同样的在 Edit 中加入Cut、Copy、Paste等小命令功能单元，如果点击这些单元, 就会触发do_job的功能
editmenu.add_command(label='Cut', command=do_job)
editmenu.add_command(label='Copy', command=do_job)
editmenu.add_command(label='Paste', command=do_job)
 
# 7) 创建第二级菜单，即菜单项里面的菜单
submenu = tk.Menu(filemenu) # 和上面定义菜单一样，不过此处实在File上创建一个空的菜单
filemenu.add_cascade(label='Import', menu=submenu, underline=0) # 给放入的菜单submenu命名为Import
 
# 8) 创建第三级菜单命令，即菜单项里面的菜单项里面的菜单命令（有点拗口，笑~~~）
submenu.add_command(label='Submenu_1', command=do_job)   # 这里和上面创建原理也一样，在Import菜单项中加入一个小菜单命令Submenu_1
 
# 9) 创建菜单栏完成后，配置让菜单栏menubar显示出来
window.config(menu=menubar)



################################################################################################################

'''
2.11   Frame :框架容器
'''

# 本windows 装不下了 ，见tkinterDemo2.py







################################################################################################################
'''
3、 主窗口循环显示

'''

# 注意，loop因为是循环的意思，window.mainloop就会让window不断的刷新，如果没有mainloop,就是一个静态的window,
# 传入进去的值就不会有循环，mainloop就相当于一个很大的while循环，有个while，每点击一次就会更新一次，所以我们必须要有循环
# 所有的窗口文件都必须有类似的mainloop函数，mainloop是窗口文件的关键的关键。
window.mainloop()
