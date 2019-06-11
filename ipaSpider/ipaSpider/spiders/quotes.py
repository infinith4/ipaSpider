# -*- coding: utf-8 -*-
import scrapy
from ipaSpider.items import Article
import logging
import logging.config
import os
import time
from scrapy.http import FormRequest

logging.config.fileConfig("./ipaSpider/logging_debug.conf")
logger = logging.getLogger()

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['www.fe-siken.com']
    start_urls = []
    
    # for i in no_list:
    #     url = 'https://www.fe-siken.com/kakomon/31_haru/q' + str(i) + '.html'
    #     start_urls.append(url)
    #     logger.info(url)

    #start_urls.sort()
    #url = 'https://www.fe-siken.com/kakomon/31_haru/q1.html'
    #start_urls.append(url)
    #i = 1
    def __init__(self, i=0, *args, **kwargs):
        super(QuotesSpider, self).__init__(*args, **kwargs)
        print("arg---------------" + str(i))
        self.i = i

    def start_requests(self):
        print("start_requests---------------" + str(self.i))
        #for i in self.no_list:
        time.sleep(1)
        url = 'https://www.fe-siken.com/kakomon/31_haru/q' + str(self.i) + '.html'
        print(url)
        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        #if('q1.html' in response.request.url):
        #for i in self.no_list:
        print("---------------response:" + response.request.url)
        #time.sleep(1)
        #print(response.file)
        for quote in response.css('div.main.kako'):
            #print(quote.xpath('//*[@id="mainCol"]/div[2]/h2/text()')[0].extract())
            logger.warning("問: " + quote.xpath('h2/text()')[0].extract())
            logger.warning(quote.xpath('div[2]/text()')[0].extract())
            logger.warning("")
            logger.warning(
                "ア: " + quote.xpath('//*[@id="select_a"]/text()')[0].extract())
            logger.warning(
                "イ: " + quote.xpath('//*[@id="select_i"]/text()')[0].extract())
            logger.warning(
                "ウ: " + quote.xpath('//*[@id="select_u"]/text()')[0].extract())
            logger.warning(
                "エ: " + quote.xpath('//*[@id="select_e"]/text()')[0].extract())
            logger.warning(
                "----------------------------------------------------------------------")

            item = Article()
            #item['author'] = quote.css('small.author::text').extract_first()
            #item['text'] = quote.css('span.text::text').extract_first()
            #item['tags'] = quote.css('div.tags a.tag::text').extract()
            # url = 'https://www.fe-siken.com/kakomon/31_haru/q' + \
            #     str(i) + '.html'
            # logger.info("---------------" + url)
                #self.start_urls.append(url)
        #return scrapy.Request(url=url, callback=self.parse, property=1)
        #url = 'https://www.fe-siken.com/kakomon/31_haru/q2.html'
        #yield scrapy.Request(url, callback=self.parse)
        #yield scrapy.Request(url, callback=self.parse)
        return item
