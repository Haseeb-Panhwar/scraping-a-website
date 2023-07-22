import scrapy
import csv
lis = []

class InternshipsSpider(scrapy.Spider):
    name = 'internships'
    allowed_domains = ['pinterest.net']
    start_urls = ['https://pintern.net/2023/06/']

    def parse(self, response):
        with open('internships.csv','w+',newline='') as f:
            write = csv.writer(f)
            for item in response.xpath('//ul')[2].xpath('li'):
                lis.append(item.xpath('a/@href').extract())
            write.writerows(lis)