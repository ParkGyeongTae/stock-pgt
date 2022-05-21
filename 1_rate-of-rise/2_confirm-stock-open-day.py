import datetime
import pandas as pd
import exchange_calendars as ecals 

XKRX = ecals.get_calendar("XKRX") # 한국 코드 

print(XKRX.is_session("2022-05-04")) # 2021-05-20 은 개장일인지 확인
print(XKRX.is_session("2022-05-05")) # 2021-05-20 은 개장일인지 확인 
print(XKRX.is_session("2022-05-07")) # 2021-05-20 은 개장일인지 확인 

print(XKRX.is_session(datetime.date.today())) # 2021-05-20 은 개장일인지 확인 
print(XKRX.next_open(datetime.date.today()).strftime("%Y-%m-%d")) # 2021-05-20 은 개장일인지 확인 