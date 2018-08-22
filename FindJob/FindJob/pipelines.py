# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class FindjobPipeline(object):
    def open_spider(self,spider):
        self.feli = open(spider.name+'.csv','w',encoding='utf-8')

    def process_item(self, item, spider):
        python_str = json.dumps(dict(item),ensure_ascii=False)+'\n'
        self.feli.write(python_str)
        return item

    def close_spider(self,spider):
        self.feli.close()
