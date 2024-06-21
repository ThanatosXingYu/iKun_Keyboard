import configparser
import os

config = configparser.ConfigParser()

DEFAULT_SYS_VOICE = 80

def read_config():
    global DEFAULT_SYS_VOICE
    config.read('config.ini')
    voice_str = config.get('SystemSettings', 'voice', fallback=str(DEFAULT_SYS_VOICE))
    print(voice_str)

read_config()

"""    try:
        config.read('config.ini')
        # 从配置文件中获取 voice 的值，默认为 DEFAULT_SYS_VOICE
        voice_str = config.get('SystemSettings', 'voice', fallback=str(DEFAULT_SYS_VOICE))
    except Exception as e:
        print(f"读取配置文件时发生错误: {e}")
        return DEFAULT_SYS_VOICE
"""