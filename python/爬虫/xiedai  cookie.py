#author wangzhaoyang
import   requests
cookies= "anonymid=iu1cub2foeh3dy; depovince=GW; _r01_=1; JSESSIONID=abcm0eSyGMObW--MhLR1w; ick_login=11064fa0-9300-45b5-b0b6-39f23a99e519; ick=f09a07ee-6bd0-47ce-a4f9-ad94b7f0b6ba; XNESSESSIONID=366b1c651253; WebOnLineNotice_972336238=1; springskin=set; jebe_key=f64c481f-ecc1-4b71-900b-5d3ed3f67840%7Cf0ea77b295c4cca944280ae1a0228123%7C1569468158214%7C1%7C1569468160544; jebe_key=f64c481f-ecc1-4b71-900b-5d3ed3f67840%7Cf0ea77b295c4cca944280ae1a0228123%7C1569468158214%7C1%7C1569468160549; vip=1; wp_fold=0; jebecookies=ae34887f-f7ca-49a8-8d9e-23488652fedf|||||; _de=8C9C52DB8FC1C486162870864AC3ADCC; p=6eae1d4d9baec91bd35ac082754c86e28; first_login_flag=1; ln_uact=18829291304; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=b08b868318125cfa9de678501c6516608; societyguester=b08b868318125cfa9de678501c6516608; id=972336238; xnsid=946760be; ver=7.0; loginfrom=null"
cookies = {i.split("=")[0]:i.split("=")[1] for i in cookies.split("; ")}
for  k,v   in   cookies.items():
    print(k,v)

