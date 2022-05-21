import pandas as pd
import os
import warnings
warnings.simplefilter("ignore")

stock_file_list = os.listdir('./stock-data/2022-05')
stock_file_list.sort()

for stock_file in stock_file_list:
    df = pd.read_excel(f'./stock-data/2022-05/{stock_file}')
    df = df[['종목명', '종가', '등락률']]
    df.columns = ['종목명', f'종가_{stock_file[10:14]}', f'등락률_{stock_file[10:14]}']
    globals()[f'{stock_file.split(".")[0]}'] = df

merge_df = pd.merge(globals()['kospi_20220502'], 
                    globals()['kospi_20220503'], 
                    how = 'left', 
                    left_on = '종목명', 
                    right_on = '종목명')

merge_df['종가비율'] = round((1 - merge_df['종가_0502'] / merge_df['종가_0503']) * 100, 2)

print(merge_df)


# print(len(file_list))

# df = pd.read_excel('./stock-data/kospi_20220520.xlsx')

# result = df[['종목명', '종가']]

# print(result)