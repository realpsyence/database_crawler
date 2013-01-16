from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.utils.markup import remove_tags
import re 
from wood_db.items import WoodDbItem

class WoodSpider(CrawlSpider):
  name = 'wood_db'
  allowed_domains = ['wood-database.com']
  start_urls = ['http://www.wood-database.com/wood-identification/']

  rules = (
    Rule(SgmlLinkExtractor(allow=('lumber-identification', )), callback='parse_item'),
    # Extract links matching 'item.php' and parse them with the spider's method parse_item
  )

  def parse_item(self, response):
    self.log('This is a wood ID page %s' % response.url)

    hxs = HtmlXPathSelector(response)
    DBitem = WoodDbItem()
    values = []
    description = hxs.select('//td/p[@style="text-align: left;"]').extract()
    for i in description:
      values.append(re.split(':', remove_tags(i))[1])
    DBitem['name'] = values[0]
    DBitem['latin'] = values[1]
    DBitem['distribution'] = values[2]
    DBitem['size'] = values[3]
    DBitem['density'] = values[4].split()[0]
    DBitem['sg'] = values[5]
    DBitem['janka'] = values[6]
    DBitem['MoR'] = values[7]
    DBitem['EM'] = values[8].split()[0]
    DBitem['crush_strength'] = values[9]
    DBitem['shrink'] = values[10]

    return DBitem
