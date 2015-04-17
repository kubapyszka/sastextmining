import scrapy

from sastextmining.items import OxfordItem, AERItem

class ArticleSpider(scrapy.Spider):
    name = "article"
    allowed_domains = ["ideas.repec.org"]
    _base_url = "https://ideas.repec.org/"
    _item_class = OxfordItem

    start_urls = [
        "https://ideas.repec.org/s/oup/qjecon.html",
    ]

    def __init__(self, journal="oxford", *args, **kwargs):
        super(ArticleSpider, self).__init__(*args, **kwargs)
        if journal == "aer":
            self._item_class = AERItem
            self.start_urls = [self._base_url + "s/aea/aecrev.html"]
            for i in xrange(5):
                self.start_urls = [self._base_url + "s/aea/aecrev" + str(i) + ".html"]


    def parse(self, response):
        for sel in response.xpath('//div[@class="panel-body"]/ul/li/b/a'):
            yield scrapy.Request(self._base_url + sel.xpath('@href').extract()[0], callback=self.parse_article)

    def parse_article(self, response):
        item = self._item_class()
        item['title'] = response.xpath('//div[@id="title"]/h1/text()').extract()[0]
        item['abstract'] = response.xpath('//div[@id="abstract-body"]/p/text()').extract()[0]
        yield item

