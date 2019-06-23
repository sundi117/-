import tkinter as tk
import tkinter.messagebox
import pickle

root =tk.Tk()
root.title("Pack布局")

# 创建第一个容器
fm1 = tk.Frame(root)
# 该容器放在左边排列
fm1.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)
# 向fm1中添加3个按钮
# 设置按钮从顶部开始排列，且按钮只能在垂直（X）方向填充
tk.Button(fm1, text='第一个').pack(side=tk.TOP, fill=tk.X, expand=tk.YES)
tk.Button(fm1, text='第二个').pack(side=tk.TOP, fill=tk.X, expand=tk.YES)
tk.Button(fm1, text='第三个').pack(side=tk.TOP,  fill=tk.X, expand=tk.YES)
# 创建第二个容器
fm2 = tk.Frame(root)
# 该容器放在左边排列，就会挨着fm1
fm2.pack(side=tk.LEFT, padx=10, expand=tk.YES)
fm2.pack(side=tk.LEFT, padx=10, fill=tk.BOTH, expand=tk.YES)
# 向fm2中添加3个按钮
# 设置按钮从右边开始排列
tk.Button(fm2, text='第一个').pack(side=tk.RIGHT, fill=tk.Y, expand=tk.YES)
tk.Button(fm2, text='第二个').pack(side=tk.RIGHT, fill=tk.Y, expand=tk.YES)
tk.Button(fm2, text='第三个').pack(side=tk.RIGHT, fill=tk.Y, expand=tk.YES)
# 创建第三个容器
fm3 = tk.Frame(root)
# 该容器放在右边排列，就会挨着fm1
fm3.pack(side=tk.RIGHT, padx=10, fill=tk.BOTH, expand=tk.YES)
# 向fm3中添加3个按钮
# 设置按钮从底部开始排列，且按钮只能在垂直（Y）方向填充
tk.Button(fm3, text='第一个').pack(side=tk.BOTTOM, fill=tk.Y, expand=tk.YES)
tk.Button(fm3, text='第二个').pack(side=tk.BOTTOM, fill=tk.Y, expand=tk.YES)
tk.Button(fm3, text='第三个').pack(side=tk.BOTTOM, fill=tk.Y, expand=tk.YES)

root.mainloop()