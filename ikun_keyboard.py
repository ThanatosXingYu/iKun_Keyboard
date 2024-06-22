import io
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
from PIL import Image

from StartupSetting import *
from SysVoiceSetting import *

mixer.init()
config = configparser.ConfigParser()

DEFAULT_SYS_VOICE = 80
mappings = {}
is_listening = True

if os.path.exists('config.ini'):
    with io.open('config.ini', 'r', encoding='utf-8') as f:
        config.read_file(f)
    config_voice = config.get('SystemSettings', 'voice', fallback=str(DEFAULT_SYS_VOICE))
    SetSysVoice(int(config_voice))


    if 'KeySettings' in config:
        for key in config['KeySettings']:
            mappings[key] = config['KeySettings'][key]

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

def isHide(var):
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
button4=tk.Button(window,text="隐藏窗口至托盘",font=('Arial',10),command=on_exit)
button4.grid(column=3,row=1,padx=(35,0),pady=(5,0),sticky="w")

var=tk.StringVar()
radiobutton1=tk.Radiobutton(window,text="是",variable=var,value="1",command=lambda :isHide(var))
radiobutton1.grid(column=1,row=1)
radiobutton2=tk.Radiobutton(window,text="否",variable=var,value="0",command=lambda :isHide(var))
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
def toggle_listening():
    global is_listening
    if is_listening:
        stop_listening()
        toggle_button.config(text="启动")
        status_label = tk.Label(window, text="当前状态：已停止", font=('Arial', 10), fg="red")
        status_label.place(x=570, y=95)
    else:
        start_listening()
        toggle_button.config(text="停止")
        status_label = tk.Label(window, text="当前状态：已启动", font=('Arial', 10), fg="green")
        status_label.place(x=570, y=95)
    is_listening = not is_listening
def choose_file():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[("音频文件", "*.wav *.mp3")])

def add_mapping():
    key = key_entry.get()
    if 'file_path' in globals() and key != "按键":
        mappings[key] = file_path
        update_listbox()
        key_entry.delete(0, tk.END)
        key_entry.insert(0, "按键")
        config = configparser.ConfigParser()
        config.read('config.ini', encoding='utf-8')
        config.set('KeySettings', key, file_path)
        with open('config.ini', 'w', encoding='utf-8') as configfile:
            config.write(configfile)
def update_listbox():
    global mappings
    mapping_listbox.delete(0, tk.END)
    for key, file in mappings.items():
        absolute_path = os.path.abspath(file)
        mapping_listbox.insert(tk.END, f"{key}: {absolute_path}")

def delete_mapping():
    selection = mapping_listbox.curselection()
    if selection:
        key = mapping_listbox.get(selection[0]).split(":")[0]
        del mappings[key]
        update_listbox()
        config = configparser.ConfigParser()
        config.read('config.ini', encoding='utf-8')
        if config.has_option('KeySettings', key):
            config.remove_option('KeySettings', key)
            with open('config.ini', 'w', encoding='utf-8') as configfile:
                config.write(configfile)

def start_listening():
    for key in mappings:
        keyboard.on_press_key(key, lambda e, k=key: play_sound(k))
def stop_listening():
    keyboard.unhook_all()

def play_sound(key):
    sound_file = mappings.get(key)
    if sound_file:
        mixer.Sound(sound_file).play()

key_entry=tk.Entry(window,width=10)
key_entry.place(x=10,y=125)
key_entry.insert(0, "输入按键")

file_button = tk.Button(window, text="选择音频文件",command=choose_file)
file_button.place(x=110,y=120)

add_button = tk.Button(window, text="添加映射",command=add_mapping)
add_button.place(x=220,y=120)

delete_button = tk.Button(window, text="删除选中映射",command=delete_mapping)
delete_button.place(x=300,y=120)

mapping_listbox = tk.Listbox(window, width=95,height=15)
mapping_listbox.place(x=10,y=160)
for key, file in mappings.items():
    absolute_path = os.path.abspath(file)
    mapping_listbox.insert(tk.END, f"{key}: {absolute_path}")

toggle_button=tk.Button(window,text="停止",command=toggle_listening)
toggle_button.place(x=600,y=120)

status_label=tk.Label(window,text="当前状态：已启动",font=('Arial',10),fg="green")
status_label.place(x=570,y=95)

start_listening()
window.mainloop()
