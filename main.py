from exchangelib import DELEGATE, Account, Credentials, Configuration, CalendarItem, ExtendedProperty, Folder, FolderCollection, EWSDateTime, EWSTimeZone
from exchangelib import EWSTimeZone, EWSDateTime, EWSDate, UTC, UTC_NOW
import time
from datetime import datetime
import datetime
from datetime import timedelta
import dateutil.tz
import pytz
# f = open("tree.txt", "w")


from exchangelib.ewsdatetime import EWSDateTime
# year, month, day = 2022, 7, 16
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

try :
    import zoneinfo
except ImportError:
    from backports import zoneinfo
from exchangelib import EWSTimeZone, EWSDateTime, EWSDate, UTC, UTC_NOW


tz = EWSTimeZone('Asia/Jerusalem')
# start = account.default_timezone(EWSDateTime.now())

localized_dt = EWSDateTime(2017, 9, 5, 8, 30, tzinfo=tz)
right_now = EWSDateTime.now(tz)

# print(right_now)
today = EWSDate.today()
# end = start + datetime.timedelta(days=1)
#
root = account.public_folders_root
pubs = (root.glob('*סידור עבודה'))
# print(pubs)

# specificFolder = list(account.public_folders_root.glob('סידור עבודה'))[0]
# print(specificFolder.count())

# for pub in pubs:
#     items_for_2022 = pub.filter(start__range=(
#         EWSDateTime(2022, 7, 14, 8, 30, tzinfo=EWSTimeZone('Europe/Copenhagen')),
#         EWSDateTime(2022, 7, 16, 8, 30, tzinfo=EWSTimeZone('Europe/Copenhagen'))
#     ))
#

start = EWSDateTime(2022, 7, 14, 8, 30, tzinfo=EWSTimeZone('Europe/Copenhagen'))
end = EWSDateTime(2022, 7, 16, 8, 30, tzinfo=EWSTimeZone('Europe/Copenhagen'))

for occurrence in pubs.view(start=start, end=end):
    print(occurrence.start, occurrence.subject)


# for items in items_for_2022:
#     print(items['sunject'])
#     # items = account.pub.calendar.filter(start=start, end=end)