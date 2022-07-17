from datetime import datetime, timedelta
import zoneinfo
import pytz
from exchangelib import EWSTimeZone, EWSDateTime, EWSDate, UTC, UTC_NOW
import dateutil.tz
from datetime import datetime, timedelta


start_time_year = 2022
start_time_month = 7
start_time_day = 14

pytz_tz = pytz.timezone('Asia/Jerusalem')
tz = EWSTimeZone.localzone()
py_dt = pytz_tz.localize(datetime(start_time_year, start_time_month, start_time_day))
yesterday = datetime.today() - timedelta(days=-1)
tomorrow = datetime.today() + timedelta(days=1)
# print(type(yesterday))
yesterday = EWSDateTime(yesterday, tzinfo=tz)
print(yesterday)
#
#
# microsoft_now = EWSDateTime.from_datetime(py_dt)
#
# print(microsoft_now)
