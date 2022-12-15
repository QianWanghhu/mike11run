import time
from time import sleep
import os
from run_sim11 import run_sim11
# from func_convert_sim11 import convert_res11
from listowanie_sim11 import sim11_index_unite
main_lok = 'E:\\BaiduSyncdisk\\Projects\\mike11run\\output\\'
sim11_L, sim11res_d, res11_L = sim11_index_unite(main_lok)
breakpoint()
p = {}
k = 0
max_num_run = 3
flag = True
for model in sim11_L:
    # Check whether the given max_num_run has finished 
    while (k % max_num_run) == 0 and (k > 0) :
        file_vol_bal = [fn for fn in os.listdir(main_lok) if 'HTML' in fn]
        time.sleep(10)
        if k == len(file_vol_bal):
            break        

    if flag:
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
