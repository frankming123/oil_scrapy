# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class AreaspiderPipeline(object):
    area_list=[]

    def __init__(self):
        self.file = open('oil_information.json', 'w')

    def process_item(self, item, spider):
        is_exist=False
        #删重
        item['area']=item['area'].replace('今日油价','')
        for dic in self.area_list:
            if dic['area']==item['area']:
                is_exist=True
        if(not is_exist):
            self.area_list.append(dict(item))
        return item

    def close_spider(self, spider):
        #省份排序
        self.area_list.sort(key=lambda d:d['province'])

        content = json.dumps(self.area_list, ensure_ascii=False)
        self.file.write(content)
        self.file.close()