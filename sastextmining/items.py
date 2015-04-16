# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ArticleInfoItem(scrapy.Item):
    title = scrapy.Field()
    abstract = scrapy.Field()

class OxfordItem(ArticleInfoItem):
    pass

class AERItem(ArticleInfoItem):
    pass
