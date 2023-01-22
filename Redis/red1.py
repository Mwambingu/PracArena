#!/usr/bin/python3
# Allowed Key Types
# Redis recognizes bytes, str, int or float
# Converts str, int or floats to bytes before
# sending them to the server

import redis
import datetime

r = redis.Redis()
today = datetime.date.today()

heroes = {"deku", "bakugo", "todoroki"}

try:
  r.sadd(today, *heroes)
except redis.exceptions.DataError:
  print("Added data that is not str, int, float or a byte.")

#Converting the time object to a string
stoday = today.isoformat()
print(type(stoday))
print(type(today))

r.sadd(stoday, *heroes)

sis_members = r.smembers(stoday)

print(sis_members)

print(r.scard(stoday))
print(r.scard(today.isoformat()))
print(r.get("leo"))