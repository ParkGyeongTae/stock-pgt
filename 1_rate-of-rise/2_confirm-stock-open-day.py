import datetime
import exchange_calendars as ecals 

XKRX = ecals.get_calendar("XKRX")

print(XKRX.is_session("2022-05-04"))
print(XKRX.is_session("2022-05-05"))
print(XKRX.is_session("2022-05-06"))

print(XKRX.is_session(datetime.date.today()))
print(XKRX.next_open(datetime.date.today()).strftime("%Y-%m-%d"))