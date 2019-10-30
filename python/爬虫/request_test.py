#author wangzhaoyang
import  requests
from   retrying   import   retry
#respons =  requests.get("http://www.baidu.com")
#a= respons.status_code
#print(a)
####伪造请求端
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}
# p="传智播客"-
# url_temp = "http://www.baidu.com"
# respons =  requests.get(url_temp,headers=headers,params=p)
# print(respons.url)
# print(respons.status_code)
# print(type(respons.content.decode()))
# print(type(respons.text))
#@retry(stop_max_attempt_numbe=3)
def _parse_url(url):
    print("*"*20)
    response = requests.get(url,headers=headers,timeout=3)
    assert  response.status_code ==200
    return  response.content.decode()

def paser_url(url):
    try:
        html_str=_parse_url(url)
    except:
        html_str = None
    return   html_str
if __name__ == '__main__':
    url = "www.baidu.com"
    print(paser_url(url))

