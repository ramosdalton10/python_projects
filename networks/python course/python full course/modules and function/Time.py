import datetime
import pytz

local_moscow = pytz.timezone('Europe/Moscow')
# print datetime.datetime.now(tz=local_moscow)

# for x in sorted(pytz.country_names):
#     print '{0}  : {1} ' .format(x ,pytz.country_names[x])

# print pytz.country_names['VA']
# asd =  list (datetime.datetime.now())
# print asd

num = list(x for x in range (10))
print num