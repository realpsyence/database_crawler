# Scrapy settings for wood_db project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'wood_db'

SPIDER_MODULES = ['wood_db.spiders']
NEWSPIDER_MODULE = 'wood_db.spiders'
DEFAULT_ITEM_CLASS = 'wood_db.items.WoodDbItem'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'wood_db (+http://www.yourdomain.com)'
