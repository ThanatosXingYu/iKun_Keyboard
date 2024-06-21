import tkinter as tk
from tkinter import filedialog
import pygame
import keyboard
import os

# 初始化pygame音频系统
pygame.mixer.init()

# 全局变量
mappings = {}
is_listening = False

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

def update_listbox():
    mapping_listbox.delete(0, tk.END)
    for key, file in mappings.items():
        mapping_listbox.insert(tk.END, f"{key}: {file}")

def delete_mapping():
    selection = mapping_listbox.curselection()
    if selection:
        key = mapping_listbox.get(selection[0]).split(":")[0]
        del mappings[key]
        update_listbox()

def toggle_listening():
    global is_listening
    if is_listening:
        stop_listening()
        toggle_button.config(text="启动")
    else:
        start_listening()
        toggle_button.config(text="停止")
    is_listening = not is_listening

def start_listening():
    for key in mappings:
        keyboard.on_press_key(key, lambda e, k=key: play_sound(k))

def stop_listening():
    keyboard.unhook_all()

def play_sound(key):
    sound_file = mappings.get(key)
    if sound_file:
        pygame.mixer.Sound(sound_file).play()

# 初始化Tkinter窗口
root = tk.Tk()
root.title("键盘音效映射器")

# 设置窗口图标
icon_path = os.path.join(os.path.dirname(__file__), 'logo.ico')
if os.path.exists(icon_path):
    root.iconbitmap(icon_path)

# 创建输入框和按钮
key_entry = tk.Entry(root, width=10)
key_entry.grid(row=0, column=0, padx=5, pady=5)
key_entry.insert(0, "按键")

file_button = tk.Button(root, text="选择音频文件", command=choose_file)
file_button.grid(row=0, column=1, padx=5, pady=5)

add_button = tk.Button(root, text="添加映射", command=add_mapping)
add_button.grid(row=0, column=2, padx=5, pady=5)

# 创建列表框显示当前映射
mapping_listbox = tk.Listbox(root, width=50)
mapping_listbox.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

# 创建删除按钮
delete_button = tk.Button(root, text="删除选中映射", command=delete_mapping)
delete_button.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

# 创建启动/停止按钮
toggle_button = tk.Button(root, text="启动", command=toggle_listening)
toggle_button.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

# 进入Tkinter主循环
root.mainloop()
