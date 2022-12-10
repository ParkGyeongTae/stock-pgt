import pandas as pd
import warnings
import datetime
import exchange_calendars as ecals 
import sys
from tabulate import tabulate

tabulate.WIDE_CHARS_MODE = False
warnings.simplefilter("ignore")

XKRX = ecals.get_calendar("XKRX")

my_list = ['20220502', '20220503', '20220504', '20220506', '20220509', '20220510', '20220511', 
'20220512', '20220513', '20220516', '20220517', '20220518', '20220519', '20220520', '20220523', 
'20220524', '20220525', '20220526', '20220527', '20220530']

for select_day in my_list:

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
    result_open_high_percent = round((sum_high_price - sum_open_price) / sum_open_price * 100, 2)

    print(f'{second_day} 상위10개 시가 : {sum_open_price}원 | {second_day} 상위10개 고가 : {sum_high_price}원 | 이익 : {result_open_high_price}원({result_open_high_percent})%')