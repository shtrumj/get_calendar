from datetime import datetime, timedelta
import zoneinfo
import pytz
from exchangelib import EWSTimeZone, EWSDateTime, EWSDate, UTC, UTC_NOW
import dateutil.tz

start_time_year = 2022
start_time_month = 7
start_time_day = 14

pytz_tz = pytz.timezone('Asia/Jerusalem')
tz = EWSTimeZone.localzone()
py_dt = pytz_tz.localize(datetime(start_time_year, start_time_month, start_time_day))

ews_bfr = EWSDateTime.from_datetime(py_dt)

print(ews_bfr)
##2022-07-16 18:55:12.851642
# today = datetime.now()
# yesterday = datetime.strftime(datetime.now() - timedelta(1).
# yesterday = EWSDateTime(yesterday,tzinfo=tz)
#
# print(yesterday)
# yesterday= EWSDateTime(yesterday)
#
# tz = EWSTimeZone.localzone()
# right_now = EWSDateTime.now(tz)
# starttime = EWSDateTime(yesterday,  tzinfo=tz)
#
# print(right_now)