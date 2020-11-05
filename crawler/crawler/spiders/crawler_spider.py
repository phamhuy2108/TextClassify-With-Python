from scrapy import Spider
from scrapy.selector import Selector
from crawler.items import CrawlerItem

class CrawlerSpider(Spider):
    name = "crawler"
    allowed_domains = ["thegioididong.com"]
    start_urls = [
        "https://www.thegioididong.com/dtdd/samsung-galaxy-a50/danh-gia",
"https://www.thegioididong.com/dtdd/samsung-galaxy-a50/danh-gia?p=2",
"https://www.thegioididong.com/dtdd/samsung-galaxy-a50/danh-gia?p=3",
"https://www.thegioididong.com/dtdd/samsung-galaxy-a50/danh-gia?p=4",
"https://www.thegioididong.com/dtdd/samsung-galaxy-a50/danh-gia?p=5",
"https://www.thegioididong.com/dtdd/samsung-galaxy-a50/danh-gia?p=6",
"https://www.thegioididong.com/dtdd/samsung-galaxy-a50/danh-gia?p=7",
"https://www.thegioididong.com/dtdd/samsung-galaxy-a50/danh-gia?p=8",
"https://www.thegioididong.com/dtdd/samsung-galaxy-a50/danh-gia?p=9",
"https://www.thegioididong.com/dtdd/samsung-galaxy-a50/danh-gia?p=10",
    ]

    def parse(self, response):
        questions = Selector(response).xpath('//ul[@class="ratingLst"]/li')

        for question in questions:
            item = CrawlerItem()

            item['User'] = question.xpath(
                'div[@class="rh"]/span/text()').extract_first()
            item['Comment'] = question.xpath(
                'div[@class="rc"]/p/i/text()').extract_first()
            item['Time'] = question.xpath(
                'div[@class="ra"]/a[@class="cmtd"]/text()').extract_first()
            item['Rate'] = len(question.xpath(
                'div[@class="rc"]/p/span/i[@class="iconcom-txtstar"]').getall())

            yield item