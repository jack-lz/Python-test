#!/usr/bin/python
#Filename:markup.py
#encoding:utf-8

import  sys, re
from handlers import *
from utils import  *
from rules import *

class Parser:
	# 初始化一些属性
	def __init__(self, handler):
		self.handler = handler
		self.rules = []
		self.filters = []

	# 向规则列表中添加规则
	def addRule(self, rule):
		self.rules.append(rule)

	# 向过滤器列表中添加规则
	def addFilter(self, pattern, name):
		# 创建过滤器，实际上这里return的是一个替换式
		def filter(block, handler):
			return re.sub(pattern, handler.sub(name), block)
		self.filters.append(filter)

	# 对文件进行处理
	def parse(self, file):
		self.handler.start('document')
		# 对文件中的文本快依次执行过滤器和规则
		for block in blocks(file):
			for filter in self.filters:
				block = filter(block, self.handler)
			for rule in self.rules:
				# 判断文本块是否符合相应规则，若符合左执行规则对应的处理方法
				if rule.condition(block):
					last = rule.action(block, self.handler)
					if last:break
		self.handler.end('document')\


class BasicTextParser(Parser):
	def __init__(self, handler):
		Parser.__init__(self, handler)
		self.addRule(ListRule())
		self.addRule(ListItemRule())
		self.addRule(TitleRule())
		self.addRule(HeadingRule())
		self.addRule(ParagraphRule())

		self.addFilter(r'\*(.+?)\*', 'emphasis')
		self.addFilter(r'(http://[\.a-zA-Z/]+)', 'url')
		self.addFilter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)', 'mail')


handler = HTMLRenderer()
parser = BasicTextParser(handler)

parser.parse(sys.stdin)







