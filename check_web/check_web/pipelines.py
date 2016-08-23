# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs
import sys

reload(sys)
sys.setdefaultencoding('utf8')


class CheckWebPipeline(object):
    def __init__(self):
        self.file = codecs.open('test.json', mode='wb', encoding='utf-8')

    def process_item(self, item, spider):
        line = 'the new movie list:' + '\n\n\n'
        for i in range(len(item['body'])):
            body = {'body': str(item['body'][i]).replace(' ', '')}
            line = line + json.dumps(body, ensure_ascii=False) + '\n'
        self.file.write(line)

        # return item

    def close_spider(self, spider):
        self.file.close()
