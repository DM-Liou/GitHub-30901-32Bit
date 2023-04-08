import requests


#2.HTTP GET
r = requests.get('https://api.github.com/events')

#3.HTTP POST
r = requests.post('http://httpbin.org/post', data = {'key':'value'})

#4.PUT, DELETE, HEAD, OPTIONS 請求
r = requests.put('http://httpbin.org/put', data = {'key':'value'})
r = requests.delete('http://httpbin.org/delete')
r = requests.head('http://httpbin.org/get')
r = requests.options('http://httpbin.org/get')

#5.傳遞 URLs 參數 當 URLs 參數的 dictionary 裡可以把 list 當成一個項目，但不可以加入 None的項目。
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('http://httpbin.org/get', params=payload)
print(r.url) #查看傳送的 URL

#6.回應資料分析 從回應中取出各種我們需要的資料
print(r.text)  # 列出文字
print(r.encoding)  # 列出編碼
print(r.status_code)  # 列出 HTTP 狀態碼
print(r.headers)  # 列出 HTTP Response Headers
print(r.headers['Content-Type'])  # 印出 Header 中的 Content-Type

#7.解析 JSON 資料 如果取得的是 json 格式資料，requests 有內建解析函式。
r = requests.get('https://api.github.com/events')
r.json()

#8.自訂 Header 許多時候網站會擋掉 UA 是 python-request 的請求，因此我們很常需要自訂 Header
url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'Mozilla/5.0'}
r = requests.get(url, headers=headers)

#9.設定 Timeout 避免程式在維修中或故障的網站停留太久，或是用來檢查是否可存取時很方便。
SECOND=5
requests.get('http://github.com', timeout=[SECOND])

#10.指定編碼 通常網站會使用 UTF-8 編碼，但若不是，可用這個方法修改讀取編碼。
r.encoding = 'ISO-8859-1'

#11.取得 Cookie
url = 'http://example.com/some/cookie/setting/url'
r = requests.get(url)
r.cookies['example_cookie_name']

#12 .修改 Cookie
url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)
r.text

