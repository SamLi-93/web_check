from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector

from check_web.items import CheckWebItem


class CheckSprider(CrawlSpider):
    name = "check_web_sprider"

    # download_delay = 1

    allowed_domains = []

    start_urls = [
        'http://www.jobgroup.cn/index',
        'http://edunew.jobgroup.cn/admin/login',
        'http://www.nbsafety.org.cn/',
        'http://www.nitjn.com/',
        'http://www.birdclass.com/index',
        'http://www.cnsiyb.com/',
        'http://www.mynep.com/index',
        'http://nb.zjcec.com/index',
        'http://www.zjcec.com/index',
        'http://www.ttxs110.com/index',
        'http://www.zjnep.com/web/index/index',
        'http://www.cjnep.net/index',
        'http://chengji.jobingedu.com/admin/login',
        'http://pt3.cjnep.net/lmsv1/admin/login',
        'http://sxcj.cjnep.net/lmsv1/admin/login',
        'http://sxnu.cjnep.net/lmsv1/admin/login',
        'http://nuc.cjnep.net/lmsv1/admin/login',
        'http://lzjtu.cjnep.net/lmsv1/admin/login',
        'http://gxu.cjnep.net/lmsv1/admin/login',
        'http://zjitccj.cjnep.net/lmsv1/admin/login',
        'http://qzucj.cjnep.net/lmsv1/admin/login',
        'http://wzycj.cjnep.net/lmsv1/admin/login',
        'http://zjsru.cjnep.net/lmsv1/admin/login',
        'http://zjvcc.cjnep.net/lmsv1/admin/login',
        'http://cj.nbutcj.cn/lmsv1/admin/login',
        'http://zgs.cjnep.net/lmsv1/',
        'http://zcmu.cjnep.net/lmsv1/admin/login',
        'http://lszjy.cjnep.net/lmsv1/admin/login',
        'http://lsu.cjnep.net/lmsv1/admin/login',
        'http://hunaneu.cjnep.net/lmsv1/admin/login',

    ]

    rules = (
        # Rule(LinkExtractor(allow=(r'https://movie.douban.com/celebrity/1016930/photo/\d+/#photo')), callback='parse_item',
        #      follow=True),

    )

    def parse(self, response):
        sel = Selector(response)

        body = sel.xpath("//body").extract()

        item = CheckWebItem()

        item['body'] = [n.encode('utf-8') for n in body]

        yield item
        print body
