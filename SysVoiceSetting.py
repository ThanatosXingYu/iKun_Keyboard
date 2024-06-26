from ctypes import cast, POINTER

from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)

volume = cast(interface, POINTER(IAudioEndpointVolume))

#Establish a bidirectional mapping between audio volume levels and corresponding dB values

AudioToVolume = {0: -65.25, 1: -56.99, 2: -51.67, 3: -47.74, 4: -44.62, 5: -42.03, 6: -39.82, 7: -37.89, 8: -36.17,
                 9: -34.63, 10: -33.24, 11: -31.96, 12: -30.78, 13: -29.68, 14: -28.66, 15: -27.7, 16: -26.8,
                 17: -25.95, 18: -25.15, 19: -24.38, 20: -23.65, 21: -22.96, 22: -22.3, 23: -21.66, 24: -21.05,
                 25: -20.46, 26: -19.9, 27: -19.35, 28: -18.82, 29: -18.32, 30: -17.82, 31: -17.35, 32: -16.88,
                 33: -16.44, 34: -16.0, 35: -15.58, 36: -15.16, 37: -14.76, 38: -14.37, 39: -13.99, 40: -13.62,
                 41: -13.26, 42: -12.9, 43: -12.56, 44: -12.22, 45: -11.89, 46: -11.56, 47: -11.24, 48: -10.93,
                 49: -10.63, 50: -10.33, 51: -10.04, 52: -9.75, 53: -9.47, 54: -9.19, 55: -8.92, 56: -8.65, 57: -8.39,
                 58: -8.13, 59: -7.88, 60: -7.63, 61: -7.38, 62: -7.14, 63: -6.9, 64: -6.67, 65: -6.44, 66: -6.21,
                 67: -5.99, 68: -5.76, 69: -5.55, 70: -5.33, 71: -5.12, 72: -4.91, 73: -4.71, 74: -4.5, 75: -4.3,
                 76: -4.11, 77: -3.91, 78: -3.72, 79: -3.53, 80: -3.34, 81: -3.15, 82: -2.97, 83: -2.79, 84: -2.61,
                 85: -2.43, 86: -2.26, 87: -2.09, 88: -1.91, 89: -1.75, 90: -1.58, 91: -1.41, 92: -1.25, 93: -1.09,
                 94: -0.93, 95: -0.77, 96: -0.61, 97: -0.46, 98: -0.3, 99: -0.15, 100: 0.0}
VolumeToAudio = {-65.25: 0, -56.99: 1, -51.67: 2, -47.74: 3, -44.62: 4, -42.03: 5, -39.82: 6, -37.89: 7, -36.17: 8,
                 -34.63: 9, -33.24: 10, -31.96: 11, -30.78: 12, -29.68: 13, -28.66: 14, -27.7: 15, -26.8: 16,
                 -25.95: 17, -25.15: 18, -24.38: 19, -23.65: 20, -22.96: 21, -22.3: 22, -21.66: 23, -21.05: 24,
                 -20.46: 25, -19.9: 26, -19.35: 27, -18.82: 28, -18.32: 29, -17.82: 30, -17.35: 31, -16.88: 32,
                 -16.44: 33, -16.0: 34, -15.58: 35, -15.16: 36, -14.76: 37, -14.37: 38, -13.99: 39, -13.62: 40,
                 -13.26: 41, -12.9: 42, -12.56: 43, -12.22: 44, -11.89: 45, -11.56: 46, -11.24: 47, -10.93: 48,
                 -10.63: 49, -10.33: 50, -10.04: 51, -9.75: 52, -9.47: 53, -9.19: 54, -8.92: 55, -8.65: 56, -8.39: 57,
                 -8.13: 58, -7.88: 59, -7.63: 60, -7.38: 61, -7.14: 62, -6.9: 63, -6.67: 64, -6.44: 65, -6.21: 66,
                 -5.99: 67, -5.76: 68, -5.55: 69, -5.33: 70, -5.12: 71, -4.91: 72, -4.71: 73, -4.5: 74, -4.3: 75,
                 -4.11: 76, -3.91: 77, -3.72: 78, -3.53: 79, -3.34: 80, -3.15: 81, -2.97: 82, -2.79: 83, -2.61: 84,
                 -2.43: 85, -2.26: 86, -2.09: 87, -1.91: 88, -1.75: 89, -1.58: 90, -1.41: 91, -1.25: 92, -1.09: 93,
                 -0.93: 94, -0.77: 95, -0.61: 96, -0.46: 97, -0.3: 98, -0.15: 99, 0.0: 100}


def GetSysVoice():
    SysVoiceLevel = round(volume.GetMasterVolumeLevel(), 2)
    voice = VolumeToAudio[SysVoiceLevel]
    return voice


def SetSysVoice(n):
    v = AudioToVolume[n]
    volume.SetMasterVolumeLevel(v, None)

    return

