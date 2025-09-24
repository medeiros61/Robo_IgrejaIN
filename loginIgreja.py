import requests

url = "https://www.liontechieq.com.br/"

#VARpayload = "documento='40.679.627/0001-35'&senha=981141122"

#VARpayload = "Login=datavixcontabil&Senha=datavix040817"
VARpayload = "Login=datavixcontabil&Senha=Dtvcont@040817"

payload = VARpayload

#payload = ""
headers = {
    'sec-ch-ua': "\"Chromium\";v=\"104\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"104\"",
    'sec-ch-ua-mobile': "?0",
    'sec-ch-ua-platform': "\"Windows\"",
    'upgrade-insecure-requests': "1",
    'content-type': "application/x-www-form-urlencoded",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers)
print('INICIO')
print(response.text)
print('------------------------------------------------------------------------------')

for c in response.cookies:
    print(c.name, c.value)

print("-----------------------------------------------------------------------------")
print(response.headers)




