import webbrowser
from time import sleep
import os

a=0

while True:
    webbrowser.open_new("http://youtube.com")
    os.system("killall 'Google Chrome'")
    a=a+0