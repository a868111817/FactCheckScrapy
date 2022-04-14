import scrapy


class TfcSpider(scrapy.Spider):
    name = 'tfc'
    allowed_domains = ['tfc-taiwan.org.tw']
    start_urls = ['https://tfc-taiwan.org.tw/articles/report']

    def parse(self, response):
        post_urls = response.xpath(
            "//div[@class='view-content']//h3/a/@href").getall()

        for post_url in post_urls:
            post_url = response.urljoin(post_url)
            yield scrapy.Request(post_url, self.parse_content)

    def parse_content(self,response):
        title = response.xpath("//h2[@class='node-title']/text()").get()
        tag = response.xpath("//div[@class='field-items']/div[@class='field-item odd']/a/text()").get()
        category = response.xpath("//div[@class='field field-name-field-taxo-report-attr field-type-taxonomy-term-reference field-label-hidden']//a/text()").get()
        date = response.xpath("//div[@class='entity-list-date']/text()").get()

        FactcheckItem = {
            "title" : title,
            "tag" : tag,
            "category" : category,
            "date" : date
        }

        return FactcheckItem
