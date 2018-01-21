# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from areaSpider.items import AreaspiderItem
import re

class YoujiaSpider(CrawlSpider):
    name = 'youjia'
    allowed_domains = ['youjia.chemcp.com']
    start_urls = ['http://youjia.chemcp.com/']

    page_city = LinkExtractor(restrict_xpaths=(r'//*[@id="box"]/div[1]/div[1]/div[2]/table//tr/td[1]/a'))
    page_oil=LinkExtractor(restrict_xpaths=(r'//*[@id="box"]/div[1]/div[1]/div[2]/div/table[2]//tr/td/div/ul/li/a'))
    rules = (
        Rule(page_city,follow=True),
        Rule(page_oil,callback='parse_oil',follow=True)
    )

    def parse_oil(self, response):
        for each in response.xpath('//*[@id="box"]/div[1]/div[1]'):
            city=AreaspiderItem()

            #各地级市名称修正
            if response.url == 'http://youjia.chemcp.com/tianjin/tianjinxian.html':
                city['area'] = '天津'+each.xpath('div[1]/span/text()').extract()[0]
            elif response.url == 'http://youjia.chemcp.com/beijing/beijinxian.html':
                city['area'] = '北京'+each.xpath('div[1]/span/text()').extract()[0]
            elif response.url == 'http://youjia.chemcp.com/shanghai/shanghaixian.html':
                city['area'] = '上海'+each.xpath('div[1]/span/text()').extract()[0]
            elif response.url == 'http://youjia.chemcp.com/xinjiang/shengzhixiaxingzhengdanwei.html':
                city['area'] = '新疆'+each.xpath('div[1]/span/text()').extract()[0]
            elif response.url == 'http://youjia.chemcp.com/chongqing/chongqingshi.html':
                city['area'] = '重庆'+each.xpath('div[1]/span/text()').extract()[0]
            elif response.url == 'http://youjia.chemcp.com/anhui/suzhoushi.html':
                city['area'] == '宿州今日油价'
            else:
                city['area']=each.xpath('div[1]/span/text()').extract()[0]

            city['oil89']=each.xpath('div[2]/div/font[1]/text()').extract()[0]
            city['oil92']=each.xpath('div[2]/div/font[2]/text()').extract()[0]
            city['oil95']=each.xpath('div[2]/div/font[3]/text()').extract()[0]
            city['oil0']=each.xpath('div[2]/div/font[4]/text()').extract()[0]
            city['updatetime'] = re.search(r'(\d+?年\d+?月\d+?日).*',each.xpath('div[2]/div/text()[1]').extract()[0]).group(1)

            #匹配省份
            pattern = re.compile(r'com/(.+)/.*html$')
            result = pattern.search(response.url)
            city['province']=result.group(1)

            yield city