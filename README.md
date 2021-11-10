# Yellow Page Crawler / Spider
It's a Crawler / Spider for crawling company data on [Yellow Page](https://www.yp.com.hk), it written in Python with Scrapy.

## Installation guide for packages

You should be install the [Scrapy](https://scrapy.org/) first, other packages (e.g. csv, datetime) should be installed by default.

You can check all the packages by the following command:
```sh 
pip3 list
```

Outputs: 
```sh
Package            Version
------------------ ---------
Scrapy             2.5.0
...                ...
```

If `Scrapy` is not on the list, you need to install it by:
```sh
pip3 install scrapy
```

### Required packages

Required Package|
----------------|
csv             |
datetime        |
scrapy          |

### Development Environment
Tools   | Version
--------|--------
Python  | 3.9.6

## Run the cralwer
You can run the crawler by following command, it will crawl the YelloPage with default keyword **體檢** which *encoded as __%E9%AB%94%E6%AA%A2__*:
```sh
scrapy crawl clinic_spider
```

However, you can pass any keyword to it with the `-a` custom arugment flag (e.g. `-a {keyword}`)
```sh
scrapy crawl clinic_spider -a {KEYWORD_TO_BE_SEARCH}
```

## Output files
The crawler will generate the result csv files with filename format `company_YYYYMMDD_HHmmss.csv` when each crawl.

## Development Roadmap
- **Search**: Search by Keyword     (Done)
- **Search**: Search by Category    (Not yet started)