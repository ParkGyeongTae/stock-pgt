import pandas as pd
import warnings
warnings.simplefilter("ignore")

# result = pd.DataFrame()

df = pd.read_excel('./stock-data/kospi_20220520.xlsx')

result = df[['종목명', '종가']]

print(result)