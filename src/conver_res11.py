import os
import pandas as pd

pd.options.mode.chained_assignment = None  # default='warn'

read11res_lok = "\"C:\\Program Files (x86)\\DHI\\2014\\bin\\x64\\res11read.exe\""
res11_lok = '../output/'
res_dirs = [res for res in os.listdir(res11_lok) if 'Result Files' in res]

# for res in res_dirs:
res_fns = [hd for hd in os.listdir(res11_lok + res_dirs[0]) if 'hd' in hd]

res_lok = res_fns[1]

nazwa =  os.path.splitext(res_lok)[0]

# os.system(read11res_lok + " -xyh " + res11_lok + " " + res_lok + "\"")
 
# os.system(read11res_lok + " -xyh " + res11_lok + " " + res_lok + "\\" + nazwa + ".csv")
#     # for hd_res in res_fns:
# with open(res11_lok + res_dirs[0] + "/" + res_fns[0], 'r', encoding='utf-8', errors='ignore') as fin:
#     f_text = fin.read().splitlines(True)

# with open(res11_lok + nazwa + ".csv", 'r') as fin:
#         data = fin.read().splitlines(True)


from mikeio1d.res1d import Res1D
res_lok = res_fns[1]
filename = res11_lok +  res_dirs[0] + '/' + res_lok
df1d=Res1D(filename)



NAME_DELIMITER = ':'
def read_all(df_obj):
    df = pd.DataFrame(index=df_obj.time_index)
    for data_set in df_obj.data.DataSets:
        for data_item in data_set.DataItems:
            for values, col_name in get_values(
                data_set, data_item, NAME_DELIMITER, df_obj._put_chainage_in_col_name
            ):
                df[col_name] = values
    return df.reindex(sorted(df.columns), axis=1)

def get_values(
        data_set, data_item, col_name_delimiter=":", put_chainage_in_col_name=False
    ):
        """ Get all time series values in given data_item. """
        name = data_set.Name if hasattr(data_set, "Name") else data_set.Id
        print(name)
        if data_item.IndexList is None:
            col_name = col_name_delimiter.join([data_item.Quantity.Id, name])
            yield data_item.CreateTimeSeriesData(0), col_name
        else:
            for i in range(0, data_item.NumberOfElements):
                postfix = str(i)

                col_name_i = col_name_delimiter.join(
                    [data_item.Quantity.Id, name, postfix]
                )
                yield data_item.CreateTimeSeriesData(i), col_name_i


df_out = read_all(df1d)