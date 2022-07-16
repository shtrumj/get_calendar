from exchangelib import DELEGATE, Account, Credentials, Configuration, CalendarItem, ExtendedProperty, Folder, \
    FolderCollection, EWSDateTime, EWSTimeZone
from dateutil.tz import gettz

from zoneinfo import ZoneInfo
from exchangelib import EWSTimeZone, EWSDateTime, EWSDate, UTC, UTC_NOW
import time
from datetime import datetime
import datetime as dt
from datetime import timedelta
import dateutil.tz
import pytz
# f = open("tree.txt", "w")


from exchangelib.ewsdatetime import EWSDateTime

# year, month, day = 2022, 7, 16
dateutil_tz = gettz('America/Chicago')
tz_name = '/'.join(dateutil_tz._filename.split('/')[-2:])

creds = Credentials(
    username="trot\\jonathan",
    password="Gib$0n579!"
)

config = Configuration(server='mail.trot.co.il', credentials=creds)

account = Account(
    primary_smtp_address="jonathan@trot.co.il",
    autodiscover=False,
    config=config,
    access_type=DELEGATE
)

try:
    import zoneinfo
except ImportError:
    from backports import zoneinfo
from exchangelib import EWSTimeZone, EWSDateTime, EWSDate, UTC, UTC_NOW

tz = EWSTimeZone('Asia/Jerusalem')

localized_dt = EWSDateTime(2017, 9, 5, 8, 30, tzinfo=tz)
right_now = EWSDateTime.now(tz)

today = EWSDate.today()

root = account.public_folders_root
pubs = (root.glob('*סידור עבודה'))

# start = EWSDateTime(2022, 7, 14, 8, 30, tzinfo=EWSTimeZone('Asia/Jerusalem'))
# start =EWSDateTime(2022, 7, 14, tzinfo=EWSTimeZone(tz_name))
# end = EWSDateTime(2022, 7, 16, tzinfo=EWSTimeZone(tz_name))


# start = EWSDateTime.strptime("2022-7-14", "%Y-%m-%d")


# end = EWSDateTime.strptime("2022-07-16", "%Y-%m-%d")
# print(start)

start = account.default_timezone

for occurrence in pubs.view(start=start, end=end):
    print(occurrence.start, occurrence.subject)

# dt_start_time = dt.datetime.strptime('2022-03-13', '%Y-%m-%d')
#
# print(EWSDateTime.from_datetime(dt_start_time).astimezone(tz))
