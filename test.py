import pygame
from pygame.locals import *
import math
import sys


import pygame.mixer
import time

def main():
    pygame.mixer.init(frequency = 44100)    # 初期設定
    pygame.mixer.music.load("bgm.mp3")     # 音楽ファイルの読み込み
    pygame.mixer.music.play(-1)             # 音楽の再生回数(ループ再生)
    time.sleep(1000)                        # 音楽の再生時間
    pygame.mixer.music.stop()               # 再生の終了


if __name__ == '__main__':
    main()