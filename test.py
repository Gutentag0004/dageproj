# -*- coding:utf-8 -*-
import re

context=str("健步随意行，轻松拿大奖！在大家积极参与第二届南京地铁垂直马拉松的同时，也可以参与有奖昂问答哦，第一位答对的朋友将获得精美保温杯一个！快来参与吧！\"<br>\"今天有奖问答的题目是：南京地铁开展了一系列的企业文化活动，尤其是在运营服务上打造了企业文化的璀璨亮点。开展了“春满车厢、夏送清凉、秋\"<div node-type=\"feed_list_content_full\" class=\"WB_text W_f14\"> 健步随意行，轻松拿大奖！在大家积极参与第二届南京地铁垂直马拉松的同时，也可以参与有奖昂问答哦，第一位答对的朋友将获得精美保温杯一个！快来参与吧！<br>&nbsp;&nbsp;&nbsp;今天有奖问答的题目是：南京地铁开展了一系列的企业文化活动，尤其是在运营服务上打造了企业文化的璀璨亮点。开展了“春满车厢、夏送清凉、秋造活动、冬显浪漫”的四季服务活动；还开出了全国首列主题列车，请问这辆主题列车的名字是什么答对一个即可)</div>")
ontext="哈哈adsadaha哈哈哈"
print(context)
pattern=re.compile(u"[\u4e00-\u9fa5]+")
result = pattern.findall(context)
print(result)