import time
from time import sleep
import os
from tkinter import *
from tkinter import filedialog
from run_sim11 import run_sim11

from func_convert_sim11 import convert_res11
from listowanie_sim11 import sim11_index_unite

root = Tk()
root.filename = filedialog.askdirectory(initialdir="/", title="1210")
main_lok = root.filename

# main_lok = "E:\\Robocze\\model_testowy"
# root.filename = filedialog.askdirectory(initialdir="/", title="Wybierz folder do zapisu raportów")
# folder = root.filename

sim11_L, sim11res_d, res11_L = sim11_index_unite(main_lok)
p = {}

for model in sim11_L:
    print("Model:")
    print(model)
    # breakpoint()
    res11_lok = sim11res_d[model]
    p[model] = run_sim11(model, res11_lok)
    while p[model].poll() is None:
            # print("idzie")
            time.sleep(120)
            p[model].kill()
            p[model].terminate()

    print("Wynik:")
    print(res11_lok)
    # convert_res11(res11_lok)
    sleep(2)

sleep(3)
