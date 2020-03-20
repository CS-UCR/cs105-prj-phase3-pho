import scrapy


class ChampSpider(scrapy.Spider):
    name = "champ"
    start_urls = [
        'http://www.lolclass.gg/position/top',
        'http://www.lolclass.gg/position/jungle',
        'http://www.lolclass.gg/position/mid',
        'http://www.lolclass.gg/position/bot',
        'http://www.lolclass.gg/position/support'
    ]

    def parse(self, response):
        for info in response.css('li.flex'):
            yield {
                'lane': response.xpath('body/main/div/div/h1/span/text()').get(),
                'rank': info.css('span.rank::text').get(),
                'name': info.xpath('a/div/span/span/text()').get(),
                'wr': info.xpath('a/div[contains(@class, "stat-winrate")]/span/span/text()').get(),
                'wrd': info.xpath('a/div[contains(@class, "stat-winrate")]/span/span[contains(@class, "subtext")]/text()').get(),
                'pr': info.xpath('a/div[contains(@class, "stat-playrate")]/span/span/text()').get(),
                'prd': info.xpath('a/div[contains(@class, "stat-playrate")]/span/span[contains(@class, "subtext")]/text()').get(),
                'kda': info.xpath('a/div[contains(@class, "stat-kda")]/span/span/text()').get(),
                'kdad': info.xpath('a/div[contains(@class, "stat-kda")]/span/span[contains(@class, "subtext")]/text()').get()
            }
