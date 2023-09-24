# @Time:2023/9/24 13:11
# @Author:yuxh
# @File:interface_auto.py
from requests import request

req = request(method="post", url="http://127.0.0.1:8080/login", data={
    "password": "123456",
    "username": "123456"

})
print(req.content)