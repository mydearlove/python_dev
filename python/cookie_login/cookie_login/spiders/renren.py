# -*- coding: utf-8 -*-
import scrapy
import   re

class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/972336238/profile']

    def start_requests(self):
        cookies = "anonymid=iu1cub2foeh3dy; _r01_=1; springskin=set; jebe_key=f64c481f-ecc1-4b71-900b-5d3ed3f67840%7Cf0ea77b295c4cca944280ae1a0228123%7C1569468158214%7C1%7C1569468160544; _de=8C9C52DB8FC1C486162870864AC3ADCC; ln_uact=18829291304; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; depovince=SXI; jebecookies=26b46331-28b9-42d9-96e0-fdaa4b134b54|||||; JSESSIONID=abcDcv1E2jOmJ4NZUh71w; ick_login=29423505-ee1c-4f14-b40b-6fe48df31385; p=f87b534a253506bd33c136a27deaa6898; ap=972336238; first_login_flag=1; t=2b42b5b37102229d04f6dc302f4e608f8; societyguester=2b42b5b37102229d04f6dc302f4e608f8; id=972336238; xnsid=84e0b85d; ver=7.0; loginfrom=null; wp_fold=0; jebe_key=f64c481f-ecc1-4b71-900b-5d3ed3f67840%7Cf0ea77b295c4cca944280ae1a0228123%7C1569468158214%7C1%7C1569729127158"
        cookies = {i.split("=")[0]:i.split("=")[1]  for i in  cookies.split("; ") }
        yield scrapy.Request(
            self.start_urls[0],
            callback=self.parse,
            cookies=cookies
        )

    def parse(self, response):
        print(re.findall("王朝阳",response.body.decode()))
