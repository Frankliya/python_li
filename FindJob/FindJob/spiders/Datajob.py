# -*- coding: utf-8 -*-
import scrapy
# import random
# import time
from FindJob.items import  FindjobItem


class DatajobSpider(scrapy.Spider):
    name = 'Datajob'
    allowed_domains = ['https://search.51job.com']
    page = 1
    urlA= 'https://search.51job.com/list/000000,000000,0000,00,9,99,Python%2B%25E5%25BC%2580%25E5%258F%2591,2,'
    urlB = '.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='

    start_urls = [urlA + str(page) + urlB]

    def parse_url(self,response):
        print(response.text)
        print("parse_url=============================================",response.url)

        item = response.meta["item"]
        item['work_url'] = response.url
        # 工资
        job_pay = response.xpath('//div[@class="in"]/div[1]/strong/text()').extract()
        # 工作经验
        work_exp = response.xpath('//div[@class="t1"]/span[1]/text()').extract()
        # 学历
        work_edu = response.xpath('//div[@class="t1"]/span[2]/text()').extract()
        # 工作地点
        job_site = response.xpath('//div[@class="bmsg inbox"]/p/text()').extract()
        job_site = "".join(job_site).split()
        # 招聘内容及要求
        job_info = response.xpath('//div[@class="bmsg job_msg inbox"]/p/text() | //div[@class="FoxDIV_20180716144847433"]//div/p/text() | //div[@class="tCompany_main"]//div/text()').extract()
        job_info = "".join(job_info).split()

        item['job_pay'] = job_pay
        item['work_exp'] = work_exp
        item['work_edu'] = work_edu
        item['job_site'] = job_site
        item['job_info'] = job_info
        print(item)

        yield item



    def parse(self, response):

        print("response.url===============",response.url)
        # a = random.choice(range(10, 30))
        # 职位链接
        work_urls = response.xpath('//div[@id="resultList"]//p[1]/span/a/@href').extract()
        # 工作地点
        work_sites = response.xpath('//div[@id="resultList"]/div[position()>3]/span[@class="t3"]/text()').extract()
        # 公司名称
        company_names = response.xpath('//div[@id="resultList"]/div[position()>3]/span[@class="t2"]/a/text()').extract()
        #职位名称
        job_names = response.xpath('//div[@id="resultList"]/div[position()>3]/p/span/a/text()').extract()
        # 发布时间
        release_times = response.xpath('//div[@id="resultList"]/div[position()>3]/span[@class="t5"]/text()').extract()

        items = []

        for i in range(len(work_urls)):
            item = FindjobItem()
            work_site = work_sites[i]
            work_url = work_urls[i]
            company_name = company_names[i]
            job_name = job_names[i]
            job_name = "".join(job_name).split()
            release_time = release_times[i]

            item['work_site'] =work_site
            item['work_url'] = work_url
            item['company_name'] = company_name
            item['job_name'] = job_name
            item['release_time'] = release_time

            items.append(item)
            yield item

        if self.page < 620:
            self.page +=1
            # return

        new_url = self.urlA+str(self.page)+self.urlB

        # for item in items:
        #     print("item========",item)
        #     job_url = item["work_url"]
        #     yield scrapy.Request(job_url,callback=self.parse_url,dont_filter=True,meta={"item":item})

        yield scrapy.Request(new_url,callback=self.parse,dont_filter=True)
