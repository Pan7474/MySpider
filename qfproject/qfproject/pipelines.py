# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class QfprojectPipeline:
    def __init__(self):
        self.file = open(r'data.text', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        print('item的值====》', item)
        print('item的类型====》', type(item))  # 这里的item是一个元素

        line = str(item)
        print('line的值————>', line)  # 强转为字符类型，方便做读写操作
        self.file.write(line)

        return item
    def close_spider(self):
        self.file.close()
