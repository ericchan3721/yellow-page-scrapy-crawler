# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ClinicCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    tel = scrapy.Field()
    fax = scrapy.Field()
    website = scrapy.Field()
    email = scrapy.Field()
    address = scrapy.Field()
    time = scrapy.Field()
    categories = scrapy.Field()
    pass
