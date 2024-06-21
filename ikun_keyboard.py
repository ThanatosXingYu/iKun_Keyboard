import os
import sys
import threading
import tkinter as tk
from tkinter import messagebox, ttk, filedialog

import keyboard
import configparser
import pystray
from pystray import MenuItem, Menu
from pygame import mixer
from PIL import Image, ImageTk

from StartupSetting import *
from SysVoiceSetting import *

config = configparser.ConfigParser()

DEFAULT_SYS_VOICE = 80
if os.path.exists('config.ini'):
    config.read('config.ini')
    config_voice = config.get('SystemSettings', 'voice', fallback=str(DEFAULT_SYS_VOICE))
    SetSysVoice(int(config_voice))
else:
    config['SystemSettings'] = {
        'voice': DEFAULT_SYS_VOICE,
    }
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

def quit_window(icon: pystray.Icon):
    icon.stop()
    window.destroy()
def show_window():
    window.deiconify()
def on_exit():
    window.withdraw()
def SetSystemVoice():
    voiceEntry = entry1.get()
    try :
        voice = int(voiceEntry)
    except ValueError:
        messagebox.showerror("错误", "输入错误")
    else:

        if voice > 100 or voice < 0:
            messagebox.showerror("错误","输入数值范围错误")
        else:
            SetSysVoice(voice)
            window.title(f'iKun Keyboard Configuration      当前系统音量:{GetSysVoice()}')
            config['SystemSettings'] = {
                'voice': voice,
            }
            with open('config.ini', 'w') as configfile:
                config.write(configfile)

menu = (MenuItem('显示', show_window, default=True),
        Menu.SEPARATOR, MenuItem('隐藏', on_exit),
        Menu.SEPARATOR, MenuItem('退出', quit_window)
        )
image = Image.open("icon.ico")
icon_pystray = pystray.Icon("icon", image, "iKun键盘", menu)

flag_file = "first_run.flag"

def isHideorNot(var):
    if var.get()=='1':
        with open(flag_file, "w") as f:
            f.write("hide")
    if var.get()=='0':
        try:
            os.remove(flag_file)
        except Exception as e:
            pass
def toggle_window(window):
    window.withdraw()

def on_closing(window):
    with open(flag_file, "w") as f:
        f.write("hide")
    window.destroy()

if os.path.exists(flag_file):
    with open(flag_file, "r") as f:
        flag = f.read().strip()
    if flag == "HIDE":
        # 如果标记文件中内容为 "hide"，则隐藏窗口
        window = tk.Tk()
        window.withdraw()
    else:
        # 否则，显示窗口并创建标记文件
        window = tk.Tk()
        window.deiconify()
        window.protocol("WM_DELETE_WINDOW", lambda: on_closing(window))
else:
    # 如果标记文件不存在，说明是第一次运行，显示窗口并创建标记文件
    window = tk.Tk()
    window.deiconify()
    window.protocol("WM_DELETE_WINDOW", lambda: on_closing(window))

#window = tk.Tk()
window.title(f'iKun Keyboard Configuration      当前系统音量:{GetSysVoice()}')
window.iconbitmap('icon.ico')
window.geometry('700x450')
#window.protocol('WM_DELETE_WINDOW', on_exit)
threading.Thread(target=icon_pystray.run, daemon=True).start()


label1=tk.Label(window,text='设置下次启动时系统音量(默认 80):',font=('Arial',10))
label1.grid(column=0,row=0,padx=(0,5),sticky="w")
label2=tk.Label(window,text='设置下次启动是否隐藏窗口运行(默认 是):',font=('Arial',10))
label2.grid(column=0,row=1,padx=(0,5),sticky="w")

entry1=tk.Entry(window,font=('Arial',10),width=7)
entry1.grid(column=1,row=0,pady=(5,0))
entry1.insert(0,"80")

button1=tk.Button(window,text="确定",font=('Arial',10),command=SetSystemVoice)
button1.grid(column=2,row=0,padx=(5,0),pady=(5,0))
button2=tk.Button(window,text="设置开机自启动",font=('Arial',10),command=lambda :execute("set"))
button2.grid(column=3,row=0,padx=(35,0),pady=(5,0),sticky="w")
button3=tk.Button(window,text="取消开机自启动",font=('Arial',10),command=lambda :execute("cancel"))
button3.grid(column=4,row=0,padx=(30,0),pady=(5,0),sticky="w")

var=tk.StringVar()
radiobutton1=tk.Radiobutton(window,text="是",variable=var,value="1",command=lambda :isHideorNot(var))
radiobutton1.grid(column=1,row=1)
radiobutton2=tk.Radiobutton(window,text="否",variable=var,value="0",command=lambda :isHideorNot(var))
radiobutton2.grid(column=2,row=1)

sep1 = ttk.Separator(window, orient='horizontal')
sep1.grid(column=0,row=3, padx=5, pady=45, sticky='ew')
sep2 = ttk.Separator(window, orient='horizontal')
sep2.grid(column=2,  row=3, pady=45,sticky='ew')
sep3 = ttk.Separator(window, orient='horizontal')
sep3.grid(column=3, row=3, pady=45,sticky='ew')
sep_label = tk.Label(window, text="自定义键盘映射",font=('Arial',10))
sep_label.grid(column=1, row=3, padx=10)


#Keyboard mapper
key_entry=tk.Entry(window,width=10)
key_entry.grid(column=0,row=4,padx=10,pady=(0,400),sticky="w")
key_entry.insert(0, "输入按键")


window.mainloop()
