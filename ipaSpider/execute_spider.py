import scrapy
from scrapy.crawler import CrawlerProcess
from ipaSpider.spiders.quotes import QuotesSpider
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from twisted.internet import reactor, defer
import logging
import sys

# for i in range(0, 10):
#     process = CrawlerProcess(get_project_settings())
#     print(i)
#     process.crawl(ArticleSpider)
# process.start(stop_after_crawl=False) # すべてのクロールジョブが終了するまでスクリプトはここでブロックされます

configure_logging()
configure_logging(install_root_handler=False)
logging.basicConfig(
    filename='log.txt',
    format='%(levelname)s: %(message)s',
    level=logging.WARNING
)

runner = CrawlerRunner()
args = sys.argv
i = args[1]

@defer.inlineCallbacks
def crawl(i):
    yield runner.crawl(QuotesSpider, i)
    reactor.stop()

crawl(i)
reactor.run()  # 最後のクロールコールが終了するまで, スクリプトはここでブロックされます
    
