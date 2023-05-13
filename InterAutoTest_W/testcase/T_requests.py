
import requests

res=requests.get("http://www.baidu.com")
print(res)
print(res.status_code)
print(res.headers)
# print(res.json())
print(res.url)
print(res.cookies)
print(res.text)
print(res.raise_for_status())




































