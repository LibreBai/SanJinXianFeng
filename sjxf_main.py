#! -*- utf-8 -*-

import time
import random
import sys

from sjxf_user import SanJinXianFengLoginInfo
from sjxf_data import SanJinXianFengData
from sjxf_logger import SjxfLog
from sjxf_database import SjxfDatabase

WanSui = """
    =============================
    * 伟大的中国人民万岁        *
    * 伟大的中国共产党万岁      *
    * 伟大的毛主席万岁          *
    * 伟大的小平同志万岁        *
    =============================
    """
SanJinXianFeng = """
    =============================
    *       三晋先锋助手        *
    =============================
    """

print(WanSui)
print(SanJinXianFeng)

# 获取登陆用户名称和密码
log = SjxfLog()
login_msg=SanJinXianFengLoginInfo()
if login_msg.CheckNecessaryParam():
    log.debug("配置信息填写正确，即将进行后续操作")
else:
    log.error("请配置相应登陆信息")
    sys.exit(0)

# 以手机号创建数据库
database = SjxfDatabase(login_msg.LoginName())

sanjin = SanJinXianFengData(login_msg.LoginName(), login_msg.LoginPasswordEncrypt())
sanjin.login()


jifen = sanjin.jifen()
if jifen['today_score'] == 15:
    log.info("今日积分已达15分，不再进行学习")
    sys.exit(0)

time.sleep(3)

PageNum = random.randint(1, 8)
ArticleNum = random.randint(3, 6)
#print("今天学习第{}页,第{}和第{}篇文章".format(PageNum, ArticleNum, ArticleNum+1))

# 获取文章信息
article_list = sanjin.getariticle(PageNum)
time.sleep(1)
# 读第一篇文章
sanjin.dianzanshoucang(article_list[ArticleNum])
time.sleep(5)
sanjin.duwenzhang30s(article_list[ArticleNum])
time.sleep(2)

# 读第二篇文章
sanjin.dianzanshoucang(article_list[ArticleNum+1])
time.sleep(5)
sanjin.duwenzhang30s(article_list[ArticleNum+1])
time.sleep(2)

# 视听学习
MovieOrMusic = random.randint(1,20)
#print("今天视听学习第{}篇视频".format(MovieOrMusic))
sanjin.shitingxuexi(MovieOrMusic)
time.sleep(3)

ZhuanTiMoKuai = [
	"十九大精神",
	"平语近人",
	"疫情防控",
	"党章党规",
    "空缺",
	"安全防护"
]

ZhuanTiMoKuaiNumList = [1,2,3,4,6]

"""
# 日常答题以及专题学习
for ExcuteTimeNum in range(2): 
    sanjin.dati()
    time.sleep(5)
    ZhuanTiMoKuaiNum = random.choice(ZhuanTiMoKuaiNumList)
    sanjin.dati(str(ZhuanTiMoKuaiNum))
"""

# 获取学习后的积分
time.sleep(5)
jifen = sanjin.jifen()

if jifen['today_score'] == 15:
    log.info("今日学习已获得15分")
else:
    log.error("今日学习未达到15分")

data = {'total_points': jifen['total_score'], 'today_points': jifen['today_score']}
database.insert_data(data)

