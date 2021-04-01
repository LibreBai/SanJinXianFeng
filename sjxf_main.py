#! -*- utf-8 -*-

import time
import random
import sys

from sjxf_user import SanJinXianFengLoginInfo
from sjxf_data import SanJinXianFengData

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
login_msg=SanJinXianFengLoginInfo()
if login_msg.CheckNecessaryParam():
    print("登陆成功")
else:
    print("登录失败")
    sys.exit()

# print(login_msg.LoginName())
# print(login_msg.LoginPasswordEncrypt())

sanjin = SanJinXianFengData(login_msg.LoginName(), login_msg.LoginPasswordEncrypt())
sanjin.login()

jifen = sanjin.jifen()
print("学习前积分:"+str(jifen[1]))

time.sleep(3)

PageNum = random.randint(1, 8)
ArticleNum = random.randint(1, 10)
print("今天学习第{}页,第{}和第{}篇文章".format(PageNum, ArticleNum, ArticleNum+1))

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
print("今天视听学习第{}篇视频".format(MovieOrMusic))
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

# 日常答题以及专题学习
'''
for ExcuteTimeNum in range(2): 
    print("普通答题")
    sanjin.dati()
    time.sleep(5)
    ZhuanTiMoKuaiNum = random.choice(ZhuanTiMoKuaiNumList)
    print("今天专题学习答题{}模块".format(ZhuanTiMoKuai[ZhuanTiMoKuaiNum-1]))
    sanjin.dati(str(ZhuanTiMoKuaiNum))
'''

# 获取学习后的积分
time.sleep(5)
jifen = sanjin.jifen()

if jifen[0] != 15:
    print("抱歉，今天未学习够15分，可能是哪里出问题啦")
else:
    print("干的漂亮，代码帮你学习获得了15分^v^")


study_after = sanjin.jifen()
print("学习后总积分:"+str(study_after[1]))
