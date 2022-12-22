import time
from time import sleep
import os
# from func_convert_sim11 import convert_res11
from listowanie_sim11 import sim11_index_unite
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


def call_run_sim11(main_lok, max_num_run):
    sim11_L, sim11res_d, res11_L = sim11_index_unite(main_lok)
    p = {}
    k = 0
    for model in sim11_L:
        # Check whether the given max_num_run has finished 
        while (k % max_num_run) == 0 and (k > 0) :
            file_vol_bal = [fn for fn in os.listdir(main_lok) if 'HTML' in fn]
            time.sleep(10)
            if k == len(file_vol_bal):
                break        

        print(f"-------------Model:{model}-------------")
        res11_lok = sim11res_d[model]
        p[model] = run_sim11(model, res11_lok)
        while p[model].poll() is None:
            time.sleep(5) # change the sleep time to 5s
            p[model].kill()
            p[model].terminate()
        k += 1
        sleep(2)
    sleep(3)

if __name__ == '__main__':
    main_lok = 'E:\\BaiduSyncdisk\\Projects\\mike11run\\output\\'
    max_num_run = 3
    call_run_sim11(main_lok, max_num_run)
