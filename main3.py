import pandas as pd
import os
from mult_stat import doPCA, doLDA, loo_cv
from helpers import Helpers as hp
from os.path import join
from datetime import datetime




path = 'C:\\Users\\sverme-adm\\Desktop\\data_split2'
eval_ts = datetime.now().strftime("_%m-%d-%Y_%H-%M-%S")
os.environ["ROOT_PATH"] = hp.mkdir_ifnotexits(join(path, 'result'+ eval_ts))

files = hp.get_all_files_in_dir_and_sub(path)
files = [f for f in files if f.find('Peaks.csv') >= 0]

results = []
info = []
for file in files:
    df = hp.read_file(file, skip_header=8)[['Ret.Time', 'Area', 'Height']]
    info.append({'name': file.split('\\')[5], 'date': file.split('\\')[6]})
    results.append(df)
    
print(results)
df = pd.DataFrame(results)

df['merged_col'] = df['Ret.Time'] + ',' + df['Area'] + ',' + df['Height']
print(df)
exit()
hp.save_df(df, join(os.environ["ROOT_PATH"], 'data'), 'extracted_features' )
df_info = pd.DataFrame(info)
hp.save_df(df_info, join(os.environ["ROOT_PATH"], 'data'), 'extracted_features_info' )

df_PC = doPCA(df, df_info)
dfLDA = doLDA(df, df_info)
loo_cv(df, df_info)
