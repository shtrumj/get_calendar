from datetime import datetime,timedelta
from exchangelib import DELEGATE, Account, Credentials, Configuration, CalendarItem, ExtendedProperty, Folder, \
    FolderCollection, EWSDateTime, EWSTimeZone
from exchangelib import EWSTimeZone, EWSDateTime, EWSDate, UTC, UTC_NOW
import dateutil.tz
import pytz
import zoneinfo
tz =EWSTimeZone.localzone()

year = datetime.now().year
month = datetime.now().month
day = datetime.now().day

tomorrowY = (datetime.now() + timedelta(days=1)).year
tomorrowM = (datetime.now() + timedelta(days=1)).month
tomorrowD = (datetime.now() + timedelta(days=1)).day

yesterdayY =(datetime.now()+ timedelta(days=-1)).year
yesterdayM =(datetime.now()+ timedelta(days=-1)).month
yesterdayD =(datetime.now()+ timedelta(days=-1)).day

yesterdayEWS = EWSDateTime(int(yesterdayY), int(yesterdayM), int(yesterdayD), tzinfo=tz)
tomorrowEWS = EWSDateTime(int(tomorrowY), int(tomorrowM), int(tomorrowD), tzinfo=tz)
todayEWS = EWSDateTime(int(year),int(month),int(day), tzinfo=tz)
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

root = account.public_folders_root
pubs = (root.glob('*סידור עבודה'))
for occurrence in pubs.view(start=yesterdayEWS, end=tomorrowEWS):
    print(occurrence.start, occurrence.subject)
