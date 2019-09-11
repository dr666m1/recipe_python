import requests
import json

url="http://zip.cgis.biz/xml/zip.php"
payload={"zn":"1660003"}
res=requests.get(url,params=payload)
print(res.text)