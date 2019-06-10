from scrapy.selector import Selector
from scrapy import Spider
from ipaSpider.items import Article

class ArticleSpider(Spider):
    name="article"
    # allowed_domains = ['172.24.215.206:8012']
    # start_urls = ["http://172.24.215.206:8012/V4_develop/Order/Index/180826081841b90c6ea88b4447998c0e84f2"]
    allowed_domains = ['en.wikipedia.org']
    start_urls = ["https://en.wikipedia.org/wiki/Main_Page",
     "https://en.wikipedia.org/wiki/Python_(programming_language)"]

def parse(self, response):
    item = Article()
    title = response.xpath('//h1/texy()')[0].extract()
    print("title is:" + title)
    item['title'] = title
    return item