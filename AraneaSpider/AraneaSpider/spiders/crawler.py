from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class HorseSpider(CrawlSpider):

    name = 'Whirlaway'

    # Method prevent crawler going out of hand and prevent it from crawling unwanted sites.
    allowed_domains = ['treehouse-projects.github.io']

    # We define a place to start
    start_urls = ['https://treehouse-projects.github.io/horse-land']

    # Now we define the rules and links to follow and ignore
    rules = [Rule(LinkExtractor(allow=r'.*'),
                  callback='parse_horses',
                  follow=True)]

    # Then we define the parsing method
    def parse_horses(self, response):
        url = response.url
        title = response.css('title::text').extract()
        print('Page URL: {}'.format(url))
        print('Page title: {}'.format(title))

