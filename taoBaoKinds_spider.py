import scrapy
import re
import json

class TaoBaoKinds(scrapy.Spider):
    name = "TaoBaoKinds"
    start_urls = [
        "https://tce.alicdn.com/api/data.htm?ids=222887%2C222890%2C222889%2C222886%2C222906%2C222898%2C222907%2C222885%2C222895%2C222878%2C222908%2C222879%2C222893%2C222896%2C222918%2C222917%2C222888%2C222902%2C222880%2C222913%2C222910%2C222882%2C222883%2C222921%2C222899%2C222905%2C222881%2C222911%2C222894%2C222920%2C222914%2C222877%2C222919%2C222915%2C222922%2C222884%2C222912%2C222892%2C222900%2C222923%2C222909%2C222897%2C222891%2C222903%2C222901%2C222904%2C222916%2C222924&callback=jsonp1207",
    ]

    def parse(self, response):
        kindlist = []
        pattern = re.compile(r'{"name":".*?","link":".*?",')
        content = response.body_as_unicode()
        self.convert1(kindlist, content, pattern)

        for kind in kindlist:
            itemName = re.search(r'".*?"', kind[7:], )
            index = kind.find("link")
            print(itemName.group(0))
            linkContent = kind[index + 7:-1]
            yield {
                'name': itemName.group(0)[1:-1],
                 'url': linkContent[:-1],
            }

    def convert1(self,kindlist, content, pattern):
        newConetent = self.convert(kindlist, content, pattern, 0)
        if newConetent is not None:
            self.convert1(kindlist, newConetent, pattern)


    def convert(self, kindlist, content, pattern, i):
        i = i + 1;
        if i > 20:
            return content
        match = re.search(pattern, content)
        if match:
            kindlist.append(match.group(0))
            index = match.span()[1]
            newContent = content[index:]
            return self.convert(kindlist, newContent, pattern, i)
        return None



