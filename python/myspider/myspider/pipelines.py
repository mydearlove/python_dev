# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import   logging
logging=logging.getLogger(__name__)

class MyspiderPipeline(object):
    def process_item(self, item, spider):
        logging.warning(item)
        return item
