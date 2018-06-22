import requests
import re
import json

url = "https://www.bilibili.com/video/av20138082"
r = requests.get(url)
rr = re.compile(r'TATE__=.*};')
data = json.loads(rr.findall(r.text)[0].replace("TATE__=", "", -1).replace(";", "", -1))
videoData = data["videoData"]
upData = data["upData"]
play = requests.get("https://api.bilibili.com/x/web-interface/archive/stat?aid=20138082").json()["data"]["view"]
print(videoData["title"], videoData["tname"], videoData["pubdate"], videoData["duration"], videoData["owner"]["name"],
      videoData["owner"]["mid"],
      videoData["aid"], upData["fans"], upData["friend"], upData["level_info"]["current_level"],
      upData["nameplate"]["name"], upData["archiveCount"], play)
