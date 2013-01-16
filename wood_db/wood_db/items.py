# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class WoodDbItem(Item):
    # define the fields for your item here like:
    # name = Field()
    name = Field()
    latin = Field()
    distribution = Field()
    size = Field()
    density = Field()
    sg = Field()
    janka = Field()
    MoR = Field()
    EM = Field()
    crush_strength = Field()
    shrink = Field()
