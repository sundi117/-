import tkinter as tk
import tkinter.messagebox
import time
import threading

# 创建主窗口
window = tk.Tk()
window.title('进度条')
window.geometry('630x150')

# 设置下载进度条
tk.Label(window, text='下载进度:', ).place(x=50, y=60)
canvas_width = 450
canvas_height = 22
canvas = tk.Canvas(window, width=canvas_width, height=canvas_height, bg="white")
canvas.place(x=110, y=60)

# 主方法函数是否执行完毕
isNotEnd = True


def run():
    '''
    点击执行按钮后的触发函数，开启多线程（主方法和进度条）
    '''
    t1 = threading.Thread(target=progress)
    t2 = threading.Thread(target=mainfoo)
    t1.start()
    t2.start()


# 线程1：主方法
def mainfoo():
    for i in range(0, 9999):
        print(i, end=', ')
        time.sleep(0.001)
    global isNotEnd
    isNotEnd = False


# 线程2：下载进度条
def progress():
    # 填充进度条
    def fill():
        '填充进度条'
        '''
        # 原始方法
        fill_line = canvas.create_rectangle(0, 0, 0, 0, width=0, fill="green")
        x = 500  # 未知变量，可更改
        n = 465 / x  # 465是矩形填充满的次数
        for i in range(x):
            n = n + 465 / x
            canvas.coords(fill_line, (0, 0, n, 60))
            window.update()
            time.sleep(0.01)  # 控制进度条流动的速度
        '''

        # 改进方法
        # create_rectangle(）：画矩形 （ （起始坐标），（终点坐标），fill='填充的颜色, outline=边框的颜色）
        fill_line = canvas.create_rectangle(0, 0, 0, 0, width=0, fill="green")
        for i in range(canvas_width):
            canvas.coords(fill_line, (0, 0, i, 60))
            window.update()
            time.sleep(0.001)  # 控制进度条流动的速度

    def clean():
        '清空进度条'
        '''
        clean_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="white")
        x = 500  # 未知变量，可更改
        n = 465 / x  # 465是矩形填充满的次数
     
        for t in range(x):
            n = n + 465 / x
            # 以矩形的长度作为变量值更新
            canvas.coords(clean_line, (0, 0, n, 60))
            window.update()
            time.sleep(0)  # 时间为0，即飞速清空进度条
        '''
        clean_line = canvas.create_rectangle(0, 0, 0, 0, width=0, fill="white")
        for j in range(canvas_width):
            # 以矩形的长度作为变量值更新
            canvas.coords(clean_line, (0, 0, j, 60))
            window.update()
            time.sleep(0)  # 时间为0，即飞速清空进度条

    while isNotEnd:
        clean()
        fill()
    tkinter.messagebox.showinfo(title='温馨提示', message='执行完毕。')


# btn_download = tk.Button(window, text='启动进度条', command=progress)
# btn_download.place(x=400, y=105)

run()
window.mainloop()
