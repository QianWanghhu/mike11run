import os
import time
from subprocess import Popen, call

# Selekcja pliku sim11
"""
root = Tk()
root.filename = filedialog.askopenfilename(initialdir="/", title="Wybierz plik .sim11")
sim11_lok = str(root.filename)
sim11_lok = sim11_lok.replace("/", "\\")
print(sim11_lok)
"""


def run_sim11(sim11_lok, res11_lok):
    licznik = 0
    flag = 1
    # size1 = 0
    # size0 = 0

    cmd = "\"C:\\Program Files (x86)\\DHI\\2014\\bin\\x64\\MzLaunch.exe\"" + " -w -b \"" + sim11_lok + "\""
    while flag == 1 and licznik < 2:
        flag = 0
        p = Popen(cmd, shell=True)
    return p
