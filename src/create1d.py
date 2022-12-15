#!usr/bin/env/ python
import os

def update_mike11(input_dir, output_dirt, sim11_file, sim11_output_name):
    f_sim11 = open(input_dir+sim11_file,'r')
    text_sim11 = f_sim11.read()
    old_text = ['Bnd1.bnd11', 'RR200.rr11', 'hd.res11', 'rr.res11']
    replace_text = ['Bnd2.bnd11', 'RR100.rr11', 'hd2.res11', 'rr2.res11']
    for t1, t2 in zip(old_text, replace_text):
        text_sim11 = text_sim11.replace(t1, t2)

    with open(f'{output_dirt}{sim11_output_name}.txt', 'w', encoding='UTF-8') as f:
        f.write(text_sim11)

    os.rename(f'{output_dirt}{sim11_output_name}.txt', \
        f'{output_dirt}{sim11_output_name}.sim11')
    f_sim11.close()
    f.close()

if __name__ == '__main__':
    input_dir = '../input/'
    output_dirt = '../output/mike11/'
    sim11_file = 'start_sim11.txt'
    sim11_output_name = 'sim22'
    update_mike11(input_dir, output_dirt, sim11_file, sim11_output_name)
