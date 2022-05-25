import pandas as pd
from tabulate import tabulate
import os
import warnings
import datetime
import exchange_calendars as ecals 
import sys

day = sys.argv[1]

XKRX = ecals.get_calendar("XKRX")

tabulate.WIDE_CHARS_MODE = False
warnings.simplefilter("ignore")

stock_file_list = os.listdir('./stock-data/2022-05')
stock_file_list.sort()

# start_date = '20220509'
start_date = day
format = '%Y%m%d'

dt_date = datetime.datetime.strptime(start_date, format).strftime(format)
st_date = XKRX.next_open(dt_date).strftime(format)
dt_next_date = datetime.datetime.strptime(st_date, format)
st_next_date = XKRX.next_open(dt_next_date).strftime(format)

end_date        = st_date
evaluation_date = st_next_date

for stock_file in stock_file_list:
    df = pd.read_excel(f'./stock-data/2022-05/{stock_file}')
    df = df[['종목명', '종가', '고가', '등락률']]
    df.columns = ['종목명', f'종가_{stock_file[10:14]}', f'고가_{stock_file[10:14]}', f'등락률_{stock_file[10:14]}']
    globals()[f'{stock_file.split(".")[0]}'] = df

merge_df = pd.merge(globals()[f'kospi_{start_date}'], 
                    globals()[f'kospi_{end_date}'], 
                    how = 'left', 
                    left_on = '종목명', 
                    right_on = '종목명')

merge_df = pd.merge(merge_df, 
                    globals()[f'kospi_{evaluation_date}'], 
                    how = 'left', 
                    left_on = '종목명', 
                    right_on = '종목명')

merge_df = merge_df.sort_values(by = [f'등락률_{end_date[4:]}'], ascending = False)

# print(tabulate(merge_df.head(10), headers = 'keys', tablefmt = 'pretty'))

print('<<< Summary >>>')
print(f'{end_date} 상위 10개 종가합 :', merge_df[f'종가_{end_date[4:]}'].head(10).sum()), '원'
print(f'{evaluation_date} 상위 10개 고가합 :', merge_df[f'고가_{evaluation_date[4:]}'].head(10).sum()), '원'
print(f'{end_date} - {evaluation_date} :', merge_df[f'고가_{evaluation_date[4:]}'].head(10).sum() - merge_df[f'종가_{end_date[4:]}'].head(10).sum(), '원', 
                                        round((merge_df[f'고가_{evaluation_date[4:]}'].head(10).sum() - merge_df[f'종가_{end_date[4:]}'].head(10).sum()) 
                                        / merge_df[f'종가_{end_date[4:]}'].head(10).sum() * 100, 2), '%')