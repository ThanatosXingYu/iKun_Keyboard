from pygame import mixer
import keyboard
import sys

mixer.init()        #假惺惺的初始化一下
mixer.music.set_volume(20)

def ji():
    mixer.music.load('audios/ji.wav')
    mixer.music.play()

def ni():
    mixer.music.load('audios/ni.wav')
    mixer.music.play()

def tai():
    mixer.music.load('audios/tai.wav')
    mixer.music.play()

def mei():
    mixer.music.load('audios/mei.wav')
    mixer.music.play()

def ctrl():
    mixer.music.load('audios/ctrl.wav')
    mixer.music.play()

def music():
    mixer.music.load('audios/music.wav')
    mixer.music.play()

def niganma():
    mixer.music.load('audios/niganma.wav')
    mixer.music.play()


"""hotkey = keyboard.read_hotkey()
keyboard.add_hotkey(hotkey, ji)
print(hotkey)"""

while True:
    if keyboard.is_pressed("J"):
        ji()
    elif keyboard.is_pressed("N"):
        ni()
    elif keyboard.is_pressed("T"):
        tai()
    elif keyboard.is_pressed("M"):
        mei()
    elif keyboard.is_pressed("Ctrl"):
        ctrl()
    elif keyboard.is_pressed("Space"):
        music()
    elif keyboard.is_pressed("Enter"):
        niganma()
    elif keyboard.is_pressed("Esc"):
        sys.exit()