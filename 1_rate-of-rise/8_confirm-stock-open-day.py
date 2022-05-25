import datetime
import exchange_calendars as ecals 

# 우리나라 국가 코드
XKRX = ecals.get_calendar("XKRX")

# 해당 날짜가 주식을 하는 날인가? (True / False)
# print(XKRX.is_session("2022-05-04"))
# print(XKRX.is_session("2022-05-05"))
# print(XKRX.is_session("2022-05-06"))

# 오늘이 주식을 하는 날인가? (True / False)
# print(XKRX.is_session(datetime.date.today()))

# 오늘을 기준으로 다음 주식 개장일은 언제인가? (yyyy-mm-dd)
# print(XKRX.next_open(datetime.date.today()).strftime("%Y-%m-%d"))


# print(XKRX.next_open(datetime.date.today())(XKRX.next_open(datetime.date.today()).strftime("%Y%m%d")))

aaa = XKRX.next_open(datetime.date.today()).strftime("%Y-%m-%d")

format = '%Y-%m-%d'
dt_datetime = datetime.datetime.strptime(aaa, format)

print(dt_datetime)
print(type(dt_datetime))