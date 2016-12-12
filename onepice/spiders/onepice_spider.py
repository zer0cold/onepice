#coding:utf-8
import scrapy
from bs4 import BeautifulSoup
import os
import urllib2
import zlib

class OnepiceSpider(scrapy.Spider):
	name = "onepice"
	
	def start_requests(self):
		urls = ['http://op.hanhande.com/mh/']
		for url in urls:
			yield scrapy.Request(url=url,callback=self.parse)
	def parse(self,respone):
		filename = 'onepice.html'
		with open(filename,'wb') as f:
			f.write(respone.body)
		self.log('Saved filed %s' % filename)
