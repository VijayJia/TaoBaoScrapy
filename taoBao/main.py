from scrapy import cmdline
cmdline.execute("scrapy crawl TaoBao -o taobao.xml -t xml".split())