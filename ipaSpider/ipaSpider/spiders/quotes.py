# -*- coding: utf-8 -*-
import scrapy
from ipaSpider.items import Article
import logging
import logging.config
import os
import time

try:
    os.remove("request.log")
except OSError:
    pass

logging.config.fileConfig("./ipaSpider/logging_debug.conf")
logger = logging.getLogger()

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['www.fe-siken.com']
    start_urls = []
    no_list = [1,
               2,
               4,
               6,
               7,
               8,
               10,
               11,
               12,
               13,
               14,
               15,
               16,
               17,
               19,
               20,
               23,
               25,
               26,
               27,
               28,
               29,
               30,
               31,
               32,
               33,
               34,
               36,
               38,
               39,
               40,
               41,
               42,
               43,
               44,
               45,
               46,
               47,
               48,
               49,
               50,
               51,
               52,
               54,
               55,
               56,
               57,
               58,
               59,
               60,
               61,
               62,
               63,
               64,
               66,
               67,
               69,
               71,
               72,
               73,
               74,
               77,
               78,
               79,
               80]
    no_list.sort()
    for i in no_list:
        url = 'https://www.fe-siken.com/kakomon/31_haru/q' + str(i) + '.html'
        start_urls.append(url)
        logger.info(url)

    #start_urls.sort()

    def parse(self, response):
        print("---------------response")
        #time.sleep(1)
        #print(response.file)
        for quote in response.css('div.main.kako'):
            #print(quote.xpath('//*[@id="mainCol"]/div[2]/h2/text()')[0].extract())
            logger.info("問: " + quote.xpath('h2/text()')[0].extract())
            logger.info(quote.xpath('div[2]/text()')[0].extract())
            logger.info("")
            logger.info(
                "ア: " + quote.xpath('//*[@id="select_a"]/text()')[0].extract())
            logger.info(
                "イ: " + quote.xpath('//*[@id="select_i"]/text()')[0].extract())
            logger.info(
                "ウ: " + quote.xpath('//*[@id="select_u"]/text()')[0].extract())
            logger.info(
                "エ: " + quote.xpath('//*[@id="select_e"]/text()')[0].extract())
            logger.info("--------------------------")

            item = Article()
            #item['author'] = quote.css('small.author::text').extract_first()
            #item['text'] = quote.css('span.text::text').extract_first()
            #item['tags'] = quote.css('div.tags a.tag::text').extract()
        return scrapy.Request(url=self.start_urls[0], callback=self.parse, property=1)
