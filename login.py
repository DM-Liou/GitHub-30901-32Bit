
import requests

url = 'http://apiquote.yuantafutures.com.tw:80/login'
data = {'account': 'E123632952', 'password': '3359ldmYY'}

response = requests.post(url, data=data)

if response.status_code == 200:
    print('登入成功！')
else:
    print('登入失敗。')



'''
import requests

# 登錄用戶名和密碼
username = "your_username"
password = "your_password"

# 設置POST請求的URL和請求體
url = "https://apiquote.yuantafutures.com.tw/api/login"
payload = {"username": username, "password": password}

# 發送POST請求
response = requests.post(url, data=payload)

# 打印回應狀態碼和內容
print(response.status_code)
print(response.content)
'''