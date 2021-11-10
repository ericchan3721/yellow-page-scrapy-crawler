import scrapy
from datetime import datetime
import clinic_crawler.items as items
import re

class ClinicSpider(scrapy.Spider):
    name = "clinic_spider"
    page_no = 1

    # set filename for each crawl
    clinic_csv_filename = 'company_' + datetime.now().strftime("%Y%m%d_%H%M%S") + '.csv'

    def __init__(self, keyword="%E9%AB%94%E6%AA%A2", **kwargs):
        self.keyword = keyword
        self.start_urls=[f'https://www.yp.com.hk/Keyword/s-{keyword}/zh?Length=15&X-Requested-With=XMLHttpRequest&keyword={keyword}&lang=zh&isfilter=true&pageno={str(self.page_no)}']
        super().__init__(**kwargs)

    def parse(self, response):
        if len(response.css('div.companyInfo.responsiveDesktop')) > 0:

            print('Crawling on page #' + str(self.page_no) + "\n")

            for company in response.css('div.companyInfo.responsiveDesktop'):
                name = company.css("div.companyTitle > a::text").get()
    
                # loop through & extract data from div.companyBasicInfo
                company_basic_info = {}
                company_basic_info_selector = company.css("div.companyBasicInfo > div.companyDataRow")
                if company_basic_info_selector is not None:
                    for data_row in company_basic_info_selector:
                        for data in data_row.css("div.companyDataCellContainer"):
                            company_basic_info[self.get_data_key(data.css("div.companyDataIcon::attr(style)").get())] = re.sub(r"\r|\n|\r\n", " ", data.css("div.companyDataValueContainer > div > a > span::text").get())

                # print("\n")
                # print(company_basic_info)

                # loop through & extract company category tags
                company_categories = []
                company_categories_selector = company.css("div.companyExtraInfo > div.companyTag > a")
                if company_categories_selector is not None:
                    for category in company_categories_selector:
                        category_tag = category.css("span:first-child::text").get()
                        if category_tag is not None:
                            company_categories.append(category_tag)

                # use scrapy.Item
                company_data = items.ClinicCrawlerItem()
                company_data['name'] = name

                for data in ['tel', 'fax', 'website', 'email', 'address', 'time']:
                    if data in company_basic_info:
                        company_data[data] = company_basic_info[data]
                    else:
                        company_data[data] = ''

                company_data['categories'] = ','.join(company_categories)

                yield company_data

            # update next page to be crawled 
            self.page_no += 1
            next_page = f'https://www.yp.com.hk/Keyword/s-{self.keyword}/zh?Length=15&X-Requested-With=XMLHttpRequest&keyword={self.keyword}&lang=zh&isfilter=true&pageno={str(self.page_no)}'
            yield response.follow(next_page, callback=self.parse)

        else:
            print('No more content on this page #' + str(self.page_no))
            print('DONE!~')

    def get_data_key(self, style_attr_value):
        # print("get_data_key: " + style_attr_value)
        filename = re.search("\/(.+)\.svg", style_attr_value)
        # print('filename: ' + filename.group(0).split('/').pop())
        return {
            'phone.svg': 'tel',
            'map.svg': 'address',
            'fax.svg': 'fax',
            'web.svg': 'website',
            'email.svg': 'email',
            'time.svg': 'time',
        }.get(filename.group(0).split('/').pop(), '')