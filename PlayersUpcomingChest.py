import requests
import json
from datetime import datetime, timedelta, time
r=requests.get("https://api.clashroyale.com/v1/players/%92GR9PRV/upcomingchests", headers={"Accept":"application/json", "authorization":"Bearer     eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjAwNzdlMDJjLTVlZGMtNDA1Ni1hZWNhLTZjZWMwMzRiYjQ4NiIsImlhdCI6MTUzNDM0NjYyMCwic3ViIjoiZGV2ZWxvcGVyL2JlYjQ5NzYzLWNhMzMtNTllYy02MTBjLTAzZmM2MzVmN2Y1OCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxOTAuMjI4LjIyMy4xMzMiXSwidHlwZSI6ImNsaWVudCJ9XX0.YAag5hP2ic3-uURi0eqUwHedL9vLaBgVa19BSbEWHdvi2hn4s1QROwqZRQOsKJMTph_G6kHgBUX2vrEmmmQ3vw"}, params = {"limit":20})
chests = r.json()["items"]
chests_hours = 0
first = dict()
last_index = 0
for c in chests:
  if c["index"] > 8:
    filler_chests = c["index"] - last_index - 1
    chests_hours += filler_chests / 240.0 * 180 * 3 # Every 240 chests 180 are silver
    chests_hours += filler_chests / 240.0 * 52 * 8 # Every 240 chests 52 are golden
    chests_hours += filler_chests / 240.0 * 8 * 12 # Every 240 chests 8 are giant/magical
  last_index = c["index"]
  if c["name"] == "Silver Chest":
    chests_hours += 3
  elif c["name"] == "Golden Chest":
    chests_hours += 8
  elif c["name"] == "Giant Chest":
    chests_hours += 12
  elif c["name"] == "Magical Chest":
    chests_hours += 12
  elif c["name"] == "Epic Chest":
    chests_hours += 12
  elif c["name"] == "Legendary Chest":
    chests_hours += 24
  elif c["name"] == "Super Magical Chest":
    chests_hours += 24
  if c["name"] not in first:
    first[c["name"]] = chests_hours
first = sorted(first.items(), key=lambda x: x[1])
now = datetime.now()
for n in first:
  print("Next %s: %s" % (n[0], (now + timedelta(hours=n[1])).strftime("%a, %d %b %Y %H:%M")))
