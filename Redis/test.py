#!/usr/bin/env python3
import redis
r = redis.Redis()

r.mset({
  "fire": "blast",
  "water": "freeze",
  "earth": "stomp",
  "air": "fly"
})

power = r.get("fire")
# Returns Byte Type
print(power)

# Decodes to str
print(power.decode("utf-8"))