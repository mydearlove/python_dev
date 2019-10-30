# -*- coding: utf-8 -*-
import scrapy
import   logging
logging = logging.getLogger(__name__)

class ItcastSpider(scrapy.Spider):
    name = 'itcast'  #爬虫名
    allowed_domains = ['itcast.cn'] #允许爬取的范围
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml'] #最开始请求的url

    def parse(self, response):
        #处理start_url地址对应的响应
        ####zhuaqqu shuju
        #ret1= response.xpath("//div[@class='tea_con']//h3/ text()").extract()
        #print(ret1)
        li_list = response.xpath("//div[@class='tea_con']//li")

        for  li  in  li_list:
            item={}
            #item["name"]= li.xpath(".//h3/text()").extract()[0]
            item["name"]= li.xpath(".//h3/text()").extract_first()
            #item["title"]= li.xpath(".//h4/text()").extract()[0]
            ###extract_first 取第一个值，如果不存在，返回none值
            item["title"]= li.xpath(".//h4/text()").extract_first()
            ###yield 每次支取一个值，减少内存占用
            yield   item

