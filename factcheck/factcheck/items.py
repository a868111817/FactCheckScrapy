# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FactcheckItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    tag = scrapy.Field()
    category = scrapy.Field()
    date = scrapy.Field()
    abstract = scrapy.Field()
    check_result = scrapy.Field()
    background = scrapy.Field()
    check = scrapy.Field()
    conclusion = scrapy.Field()