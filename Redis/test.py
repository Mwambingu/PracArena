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

print(power)