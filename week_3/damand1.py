import urllib.request as request
import json
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json"
with request.urlopen(src) as response:
    data=json.load(response)
#解讀資料 
clist=data["result"]["results"]
with open("taipei-data.txt",mode="w",encoding="utf-8") as file:
    for da in clist:
        file.write(da["stitle"]+","+da["longitude"]+","+da["latitude"]+","+"http"+da["file"].split("http")[1]+"\n")
