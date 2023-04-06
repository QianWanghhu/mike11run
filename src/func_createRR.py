import os
import pandas as pd
import numpy as np

def update_nam(input_dir, f_mdata, rr_path, rain_type, nam_name, update_evap):
    """
    Read txt files for forming the NAM model.
    """
    
    file_mdata = input_dir + f_mdata
    model_mdata = pd.read_excel(file_mdata)
    model_mdata = model_mdata[model_mdata['Area']>0.0]
    f_start=open(f'{input_dir}start.txt','r')
    f_end=open(f'{input_dir}end.txt','r')
    f_para=open(f'{input_dir}para.txt','r')
    f_inputs=open(f'{input_dir}inputs.txt','r')
    f_eva=open(f'{input_dir}eva.txt','r')
    text_start=f_start.read()
    text_para=f_para.read()
    text_final=f_end.read()
    text_inputs = f_inputs.read()
    text_eva=f_eva.read()

    # Replace rainfall with given rain_type
    rain_pairs = list(rain_type.keys())
    text_inputs = text_inputs.replace(rain_pairs[0], rain_pairs[1])
    text_inputs = text_inputs.replace(rain_type[rain_pairs[0]], rain_type[rain_pairs[1]])

    #update evap
    if update_evap:
        text_eva = text_eva.replace(rain_pairs[0], rain_pairs[1])

    # get catchment information
    Catchment = {}
    Catchment["Catchment_Name"] = model_mdata.loc[:,"MingCheng"]
    Catchment["Catchment_Model"] = model_mdata.loc[:,"Catchment_model"]
    Catchment["Catchment_Area"] = np.round(model_mdata.loc[:,"Area"], 2)
    Catchment["Number_ID"] = model_mdata.loc[:,"ID"]

    # create str
    insert_1 = ""
    insert_2 = ""
    insert_3 = ""

    for i in model_mdata.index: 
        insert_1 += "\n[Catchment] \n Catchment_Name = \'" + str(Catchment["Catchment_Name"][i])+'\'\n Catchment_Model =\''\
            + str(Catchment["Catchment_Model"][i]) + '\'\n Catchment_Area=' + str(Catchment["Catchment_Area"][i])+ \
                '\n Number_ID=' + str(Catchment["Number_ID"][i])+ \
                "\n Additional_output = true \n Calibration_plot = false \n EndSect // Catchment"

        insert_2 +=  text_para + "\n"
        # Creat str for timeseries
        insert_3 += "\n[Condition] \n Catchment_Name = \'" + str(Catchment["Catchment_Name"][i]) + '\'\n' + text_inputs + \
             "\n"+"\n[Condition] \n Catchment_Name = \'" + str(Catchment["Catchment_Name"][i]) + '\'\n' + text_eva + "\n"        
    
    insert_1 = insert_1 + "\nEndSect // CatchList\n [CombinedList] \n EndSect // CombinedList \n[ParameterList] \n"
    insert_2 = insert_2 + "\nEndSect  // ParameterList \n [TimeseriesList]\n Max_Comb_Number = 8"
    insert_3 = insert_3 + '\nEndSect  // TimeseriesList \n'

    combin = text_start + insert_1 + insert_2 + insert_3 + '\n' + text_final
    
    model=open(rr_path + nam_name +'.txt','w')
    model.write(combin) 
    newname=rr_path + nam_name + ".rr11"
    model.close()
    os.rename(rr_path + nam_name + ".txt", newname)
    f_start.close()
    f_para.close()
    f_end.close()
    f_eva.close()
    f_inputs.close()


def update_mike11(input_dir, output_dirt, sim11_file, sim11_output_name, \
    old_text, replace_text):
    f_sim11 = open(input_dir+sim11_file,'r')
    text_sim11 = f_sim11.read()
    for t1, t2 in zip(old_text, replace_text):
        text_sim11 = text_sim11.replace(t1, t2)

    with open(f'{output_dirt}{sim11_output_name}.txt', 'w', encoding='UTF-8') as f:
        f.write(text_sim11)

    os.rename(f'{output_dirt}{sim11_output_name}.txt', \
        f'{output_dirt}{sim11_output_name}.sim11')
    f_sim11.close()
    f.close()
