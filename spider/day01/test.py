import urllib.request
response = urllib.request.urlopen('http://www.baidu.com/')
html = response.read().decode("utf-8")
print(html)
# 取响应状态码和头信息
print(response.status)
print(response.getheaders())
print(response.getheader("Server"))