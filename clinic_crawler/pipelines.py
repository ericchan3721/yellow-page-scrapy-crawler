# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv
from itemadapter import ItemAdapter


class ClinicCrawlerPipeline:

    def process_item(self, item, spider):
        with open(spider.clinic_csv_filename, mode='a', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=item.keys())
            csv_writer.writerow(item)
        return item

    def open_spider(self, spider):
        header_keys = ['name', 'tel', 'fax', 'website', 'email', 'address', 'time', 'categories']
        with open(spider.clinic_csv_filename, mode='a', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=header_keys)
            csv_writer.writeheader()
