import customtkinter
import json
import time
import os
import sys
import ctypes

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from functions import *
from tg_bot import *

from windows import MainWindow


customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')
customtkinter.set_widget_scaling(1)


try:
    if ctypes.windll.shell32.IsUserAnAdmin():
        os.system('CLS')
        main_window = MainWindow()
        tg_msg('Работа программы завершена')
    else:
        import py_win_keyboard_layout
        py_win_keyboard_layout.change_foreground_window_keyboard_layout(0x04090409)
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
except Exception as ex:
    tg_msg(ex)
    print(ex)
