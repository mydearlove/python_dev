# -*- coding: utf-8 -*-
import scrapy
from   copy import   deepcopy
#from   yg.items import  YgItem

class YangguangSpider(scrapy.Spider):
    name = 'yangguang'
    allowed_domains = ['sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=0']

    def parse(self, response):
        #tr_list = response.xpath("/div/[@class='greyframe'/table[2]/tr/td/table/tr")
        tr_list = response.xpath("//div[@class='greyframe']/table[2]/tr/td/table/tr")
       # print(tr_list)
        for tr  in tr_list:
            item = {}
            item["title"] = tr.xpath("./td[2]/a[@class='news14']/@title").extract_first()
            item["href"] = tr.xpath("./td[2]/a[@class='news14']/@href").extract_first()
            item["publish_date"] = tr.xpath("./td[last()]/text()").extract_first()

            yield  scrapy.Request(
                item["href"],  ###callback函数访问这个url
                callback=self.parse_detail,
                meta={"item":deepcopy(item)}
            )
        next_url = response.xpath("//a[text()='>']/@href").extract_first()
        if next_url is not None:
            yield  scrapy.Request(
                next_url,
                callback=self.parse
            )
    def parse_detail(self,response):
        item = response.meta["item"]
        item["content"]= response.xpath("//div[@class='wzy1']/table[2]/tr/td//text()").extract()
        item["content_img"] = response.xpath("//div[@class='wzy1']/table[2]/tr/td//img/@src").extract()
        item["content_img"] = ["http://wz.sun0769.com"+ i for i in item["content_img"]]
        #print(item)
        yield  item   #将数据传递给pipeline
