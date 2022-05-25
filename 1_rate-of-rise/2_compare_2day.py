import pandas as pd
from tabulate import tabulate
import os
import warnings

tabulate.WIDE_CHARS_MODE = False
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

merge_df = pd.merge(merge_df, 
                    globals()['kospi_20220504'], 
                    how = 'left', 
                    left_on = '종목명', 
                    right_on = '종목명')

merge_df['종가등락률'] = round((1 - merge_df['종가_0502'] / merge_df['종가_0503']) * 100, 2)

merge_df = merge_df.sort_values(by = ['종가등락률'], ascending = False)

print(tabulate(merge_df.head(10), headers = 'keys', tablefmt = 'pretty'))

print('<<< Summary >>>')
print('kospi_20220503 상위 10개의 합 :', merge_df['종가_0503'].head(10).sum())
print('kospi_20220504 상위 10개의 합 :', merge_df['종가_0504'].head(10).sum())
print('kospi_20220503 - kospi_20220504 :', merge_df['종가_0504'].head(10).sum() - merge_df['종가_0503'].head(10).sum(), 
                                        round((merge_df['종가_0504'].head(10).sum() - merge_df['종가_0503'].head(10).sum()) 
                                        / merge_df['종가_0503'].head(10).sum() * 100, 2))