# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class AreaspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    area=scrapy.Field()
    oil89=scrapy.Field()
    oil92=scrapy.Field()
    oil95=scrapy.Field()
    oil0=scrapy.Field()
    province=scrapy.Field()
    updatetime=scrapy.Field()