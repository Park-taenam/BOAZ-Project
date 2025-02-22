'''
Reference :
    - https://pycaret.readthedocs.io/en/stable/api/regression.html
'''
# %%
import numpy as np
import pandas as pd
from pycaret.regression import *

import warnings
warnings.filterwarnings("ignore")

# %%
def preprocessing(df):
    df = df.astype({'chongjang_big':'int',
                'chongjang_small':'int',
                'shoulder_big':'int',
                'shoulder_small':'int',
                'chest_big':'int',
                'chest_small':'int',
                'arm_big':'int',
                'arm_small':'int'})
    df = df.loc[:, ['gender', 'height', 'weight', 'size', 'content',
                    '총장', '어깨너비', '가슴단면', '소매길이',
                    'chongjang_big', 'chongjang_small',
                    'shoulder_big', 'shoulder_small',
                    'chest_big', 'chest_small',
                    'arm_big', 'arm_small']]
    
    # Make train set
    df_chongjang_big    = df.loc[df['chongjang_big'] == 1, ['height','weight','gender', '총장']]
    df_chongjang_small  = df.loc[df['chongjang_small'] == 1, ['height','weight','gender', '총장']]
    df_chongjang_soso   = df.loc[(df['chongjang_big'] == 0) & (df['chongjang_small'] == 0), ['height','weight','gender', '총장']]

    df_shoulder_big     = df.loc[df['shoulder_big'] == 1, ['height','weight','gender', '어깨너비']]
    df_shoulder_small   = df.loc[df['shoulder_small'] == 1, ['height','weight','gender', '어깨너비']]
    df_shoulder_soso    = df.loc[(df['shoulder_big'] == 0) & (df['shoulder_small'] == 0), ['height','weight','gender', '어깨너비']]

    df_chest_big        = df.loc[df['chest_big'] == 1, ['height','weight','gender', '가슴단면']]
    df_chest_small      = df.loc[df['chest_small'] == 1, ['height','weight','gender', '가슴단면']]
    df_chest_soso       = df.loc[(df['chest_big'] == 0 )& (df['chest_small'] == 0), ['height','weight','gender', '가슴단면']]

    df_arm_big          = df.loc[df['arm_big'] == 1, ['height','weight','gender','소매길이']]
    df_arm_small        = df.loc[df['arm_small'] == 1, ['height','weight','gender','소매길이']]
    df_arm_soso         = df.loc[(df['arm_big'] == 0) & (df['arm_small'] == 0), ['height','weight','gender','소매길이']]

    # Drop Null value
    df_chongjang_big.dropna(axis = 0,inplace = True)
    df_chongjang_small.dropna(axis = 0,inplace = True)
    df_chongjang_soso.dropna(axis = 0,inplace = True)

    df_arm_big.dropna(axis = 0,inplace = True)
    df_arm_small.dropna(axis = 0,inplace = True)
    df_arm_soso.dropna(axis = 0,inplace = True)

    df_chest_big.dropna(axis = 0,inplace = True)
    df_chest_small.dropna(axis = 0,inplace = True)
    df_chest_soso.dropna(axis = 0,inplace = True)

    df_shoulder_big.dropna(axis = 0,inplace = True)
    df_shoulder_small.dropna(axis = 0,inplace = True)
    df_shoulder_soso.dropna(axis = 0,inplace = True)
    
    # train df list
    hood_chongjang_train_lst = [df_chongjang_big, df_chongjang_small, df_chongjang_soso]
    hood_shoulder_train_lst = [df_shoulder_big, df_shoulder_small, df_shoulder_soso]
    hood_chest_train_lst = [df_chest_big, df_chest_small, df_chest_soso]
    hood_arm_train_lst = [df_arm_big, df_arm_small, df_arm_soso]
    
    return hood_chongjang_train_lst, hood_shoulder_train_lst, hood_chest_train_lst, hood_arm_train_lst

# %%
if __name__=='__main__':
    df = pd.read_pickle('../../data/Modeling_DF_230116.pickle')
    
    hood_chongjang_train_lst, hood_shoulder_train_lst, hood_chest_train_lst, hood_arm_train_lst = preprocessing(df)

    ## pycaret
    # 총장
    for i in range(3):
        print("hood_chongjang_train_lst[{}]".format(i))
        s = setup(hood_chongjang_train_lst[i], target = '총장')
        set_config('seed', 2023)
        best = compare_models()
        plot_model(best)
        evaluate_model(best)
    
    # 어깨
    for i in range(3):
        print("hood_shoulder_train_lst[{}]".format(i))
        s = setup(hood_shoulder_train_lst[i], target = '어깨너비')
        set_config('seed', 2023)
        best = compare_models()
        plot_model(best)
        evaluate_model(best)
    
    # 가슴
    for i in range(3):
        print("hood_chest_train_lst[{}]".format(i))
        s = setup(hood_chest_train_lst[i], target = '가슴단면')
        set_config('seed', 2023)
        best = compare_models()
        plot_model(best)
        evaluate_model(best)
    
    # 소매
    for i in range(3):
        print("hood_arm_train_lst[{}]".format(i))
        s = setup(hood_arm_train_lst[i], target = '소매길이')
        set_config('seed', 2023)
        best = compare_models()
        plot_model(best)
        evaluate_model(best)