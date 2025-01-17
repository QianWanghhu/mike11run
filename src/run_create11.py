import os
from func_createRR import update_nam, update_mike11

# Define dirs and fnames
rr_dir = 'NAM/'
# bnd_dir = 'output/4 Bnd/'
input_dir = ''
f_mdata = 'model_mdata.xlsx'

# Create NAM 
# For now, assume NAM are created already.
# Write a file
old_rain = '200nianjiangyu.dfs0'
replace_rain = ['rainfall2007-2009.dfs0']
old_item = '200NIAN'
replace_item = ['2007-2009']
update_evap = True
if not os.path.exists(rr_dir):
    os.mkdir(rr_dir)
for rain_new, item_new in zip(replace_rain, replace_item):
    rain_info = {old_rain: old_item, rain_new: item_new}
    nam_name = f'RR{rain_new[:-5]}'
    print(nam_name)
    update_nam(input_dir, f_mdata, rr_dir, rain_info, nam_name, update_evap)

# # Loop over RR and Bnd
# rr_list = [rr for rr in os.listdir(rr_dir) if '.rr11' in rr]
# bnd_list  =[bnd for bnd in os.listdir(bnd_dir) if '.' in bnd]
# sim11_dir = 'output/'
# sim11_file = 'start_sim11.txt'

# # Loop for creating *.sim11
# for rr in rr_list:
#     for bnd in bnd_list:
#         rr_name = rr.split('.')[0]
#         bnd_name = bnd.split('.')[0]
#         sim11_output_name = f'{rr_name}_{bnd_name}'
#         old_text = ['Bnd1.bnd11', '3 RR\RR1209\RR200.rr11', 'hd.res11', 'rr.res11']
#         replace_text = [f'4 Bnd\{bnd}', f'5 NAM\{rr}', \
#             f'hd_{sim11_output_name}.res11', f'rr_{sim11_output_name}.res11']
        
#         update_mike11(input_dir, sim11_dir, sim11_file, sim11_output_name, old_text, replace_text)
        