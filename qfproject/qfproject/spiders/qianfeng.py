import scrapy

from qfproject.items import QfprojectItem


class QianfengSpider(scrapy.Spider):
    name = 'qianfeng'
    allowed_domains = ['www.1000phone.com']
    start_urls = ['http://www.1000phone.com/']

    def parse(self, response):
        print(type(response))
        item = QfprojectItem()
        item['title'] = response.xpath('//head/title/text()')
        print(item['title'])
        item['name'] = response.xpath('//head/meta[@name="keywords"]/@content')
        print(item['name'])
        yield item

