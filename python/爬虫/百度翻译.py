#author wangzhaoyang
import   requests
import    sys
import   json

#query_str = sys.argv[1]
#headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}
headers = {"user-agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Mobile Safari/537.36"}
post_data = {
    "from":"zh",
    "to":"en",
    "query":"你好",
}
post_url = "https://fanyi.baidu.com/v2transapi"
r =  requests.post(post_url,data=post_data,headers=headers)
print(r.content.decode())