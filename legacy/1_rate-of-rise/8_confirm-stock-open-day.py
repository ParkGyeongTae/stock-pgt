import datetime
import exchange_calendars as ecals 

# 우리나라 국가 코드
XKRX = ecals.get_calendar("XKRX")

# 해당 날짜가 주식을 하는 날인가?
# Result : True / False
# print(XKRX.is_session("2022-05-04"))
# print(XKRX.is_session("2022-05-05"))
# print(XKRX.is_session("2022-05-06"))

# 오늘이 주식을 하는 날인가? 
# Result : True / False
# print(XKRX.is_session(datetime.date.today()))

# 오늘을 기준으로 다음 주식 개장일은 언제인가?
# Result : yyyy-mm-dd
# print(XKRX.next_open(datetime.date.today()).strftime("%Y-%m-%d"))


# 특정 날짜를 기준으로 다음 개장일과 다다음 개장일은 언제인가?

date = '20220504'
format = '%Y%m%d'

dt_date = datetime.datetime.strptime(date, format).strftime(format)
st_date = XKRX.next_open(dt_date).strftime(format)
dt_next_date = datetime.datetime.strptime(st_date, format)
st_next_date = XKRX.next_open(dt_next_date).strftime(format)

print(dt_date)
print(st_date)
print(st_next_date)