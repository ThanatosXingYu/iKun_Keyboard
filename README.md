# iKun_Keyboard
为~~小黑子~~ikun们打造的专属键盘--鸡音键盘，非ikun不可用！用上它，你就是千万ikun粉中最靓的仔，无人可敌无人可挡。  

## 项目背景介绍
众所周知，早在1867年Christopher Latham Scholes发明QWER键盘时，地球上就已经存在了~~小黑子~~iKun。备受程序员青睐的Ctrl键，就是由C(唱)、T(跳)、R(Rap)，L(篮球)组合而成。

## 食用方法
>方法1 打包EXE(无Python环境)
### 安装pyinstaller(已安装请忽略)
```
git clone https://github.com/ThanatosXingYu/iKun_Keyboard.git
cd iKun_Keyboard
pyinstaller iKunKeyboard.spec
```

>方法2 有Python环境
```
git clone https://github.com/ThanatosXingYu/iKun_Keyboard.git
cd iKun_Keyboard
pip install -r requirements.txt
python iKun_Keyboard.py
```
>方法3

在[releases](https://github.com/ThanatosXingYu/iKun_Keyboard/releases)中直接下载解压

## 食用说明
首次运行将会弹出配置窗口，可设置下次运行是否隐藏启动和自定义键盘映射等  
如果要自定义键盘映射请将音频格式转为wav或mp3，否则程序无法正常加载，可以在程序配置页自动添加，也可以阅读config.ini文件后根据格式手动添加
### 效果
按下 `J` 键后播放 `audios/ji.wav`  
按下 `N` 键后播放 `audios/ni.wav`  
按下 `T` 键后播放 `audios/tai.wav`  
按下 `M` 键后播放 `audios/mei.wav`  
按下 `K` 键后播放 `audios/kun.wav`  
按下 `W` 键后播放 `audios/wahaha.wav`  
按下 `A` 键后播放 `audios/aiyo.wav`  
按下 `Space` 键后播放 `audios/music.wav`  
按下 `Enter` 键后播放 `audios/niganma.wav`  
按下 `Backspace` 键后播放 `audios/a.wav`  
按下 `Ctrl` 键后播放 `audios/ctrl.wav`  
按下 `Esc` 键退出程序  
