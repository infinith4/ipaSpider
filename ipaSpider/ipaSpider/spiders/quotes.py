# -*- coding: utf-8 -*-
import scrapy
from ipaSpider.items import Article

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['www.fe-siken.com']
    start_urls = ['https://www.fe-siken.com/kakomon/31_haru/q1.html']

    def parse(self, response):
        print("---------------response")
        #print(response.file)
        for quote in response.css('div.main.kako'):
            #print(quote.xpath('//*[@id="mainCol"]/div[2]/h2/text()')[0].extract())
            print(quote.xpath('h2/text()')[0].extract())
            print(quote.xpath('div[2]/text()')[0].extract())
            print(quote.xpath('//*[@id="select_a"]/text()')[0].extract())
            print(quote.xpath('//*[@id="select_i"]/text()')[0].extract())
            print(quote.xpath('//*[@id="select_u"]/text()')[0].extract())
            print(quote.xpath('//*[@id="select_e"]/text()')[0].extract())
            item = Article()
            #item['author'] = quote.css('small.author::text').extract_first()
            #item['text'] = quote.css('span.text::text').extract_first()
            #item['tags'] = quote.css('div.tags a.tag::text').extract()
            yield item
