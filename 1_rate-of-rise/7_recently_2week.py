import pandas as pd
import os
import warnings
warnings.simplefilter("ignore")

stock_file_list = os.listdir('./stock-data')
stock_file_list.sort()

for stock_file in stock_file_list:
    df = pd.read_excel(f'./stock-data/{stock_file}')
    df = df[['종목코드', '종목명', '시가', '고가', '저가', '종가', '거래량']]
    df.columns = ['code', 'name', 'o', 'h', 'l', 'c', 'v']
    print(df.columns)



# print(len(file_list))

# df = pd.read_excel('./stock-data/kospi_20220520.xlsx')

# result = df[['종목명', '종가']]

# print(result)