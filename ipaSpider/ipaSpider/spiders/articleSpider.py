from scrapy.selector import Selector
from scrapy import Spider
from ipaSpider.items import Article

class ArticleSpider(Spider):
    name="article"
    allowed_domains = ['www.fe-siken.com']
    start_urls = ["https://www.fe-siken.com/kakomon/31_haru/q1.html"]

def parse(self, response):
    item = Article()
    title = response.xpath('//h1/texy()')[0].extract()
    print("title is:" + title)
    item['title'] = title
    return item
