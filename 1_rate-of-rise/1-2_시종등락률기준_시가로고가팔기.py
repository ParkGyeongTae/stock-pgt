import pandas as pd
import warnings
import datetime
import exchange_calendars as ecals 
import sys
from tabulate import tabulate

tabulate.WIDE_CHARS_MODE = False
warnings.simplefilter("ignore")

select_day = sys.argv[1]

XKRX = ecals.get_calendar("XKRX")

first_day = select_day
format    = '%Y%m%d'

dt_date = datetime.datetime.strptime(first_day, format).strftime(format)
st_date = XKRX.next_open(dt_date).strftime(format)

second_day = st_date

df_first_day         = pd.read_excel(f'./stock-data/2022-05/kospi_{first_day}.xlsx')
df_first_day         = df_first_day[['종목명', '시가', '종가', '고가', '등락률']]
df_first_day.columns = ['종목명', f'시가_{first_day[4:8]}', f'종가_{first_day[4:8]}', f'고가_{first_day[4:8]}', f'등락률_{first_day[4:8]}']

df_second_date         = pd.read_excel(f'./stock-data/2022-05/kospi_{second_day}.xlsx')
df_second_date         = df_second_date[['종목명', '시가', '종가', '고가', '등락률']]
df_second_date.columns = ['종목명', f'시가_{second_day[4:8]}', f'종가_{second_day[4:8]}', f'고가_{second_day[4:8]}', f'등락률_{second_day[4:8]}']

merge_df = pd.merge(df_first_day,
                    df_second_date,
                    how      = 'left',
                    left_on  = '종목명',
                    right_on = '종목명')

merge_df = merge_df.sort_values(by = [f'등락률_{first_day[4:]}'], ascending = False)
merge_df = merge_df.head(10)

sum_open_price = int(merge_df[f'시가_{second_day[4:]}'].sum())
sum_high_price = int(merge_df[f'고가_{second_day[4:]}'].sum())

result_open_high_price   = int(sum_high_price - sum_open_price)
result_open_high_percent = round((merge_df[f'고가_{second_day[4:]}'].head(10).sum() - merge_df[f'시가_{second_day[4:]}'].head(10).sum()) / merge_df[f'시가_{second_day[4:]}'].head(10).sum() * 100, 2)

print('<<< Summary >>>')
print(f'{second_day} 상위 10개 시가합 : {sum_open_price}원 | {second_day} 상위 10개 고가합 : {sum_high_price}원')
# print(f'{second_day} 상위 10개 고가합 : {sum_high_price} 원')
print(f'{second_day} - {second_day} : {result_open_high_price}원', 
                                        round((merge_df[f'고가_{second_day[4:]}'].head(10).sum() - merge_df[f'시가_{second_day[4:]}'].head(10).sum()) 
                                        / merge_df[f'시가_{second_day[4:]}'].head(10).sum() * 100, 2), '%')