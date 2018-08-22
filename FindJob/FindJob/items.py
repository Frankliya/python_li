# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FindjobItem(scrapy.Item):
    # define the fields for your item here like:
    # 公司名称
    company_name = scrapy.Field()
    # 职位名称
    job_name = scrapy.Field()
    # 招聘内容及要求
    job_info = scrapy.Field()
    # 联系地点
    job_site = scrapy.Field()
    # 发布时间
    release_time =scrapy.Field()
    # 薪资
    job_pay = scrapy.Field()
    # 工作经验
    work_exp = scrapy.Field()
    # 学历
    work_edu = scrapy.Field()
    # 工作地点
    work_site = scrapy.Field()
    # 职位链接
    work_url = scrapy.Field()


