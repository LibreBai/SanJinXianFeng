#! -*- utf-8 -*-

import time

from sjxf_user import SanJinXianFengLoginInfo
from sjxf_data import SanJinXianFengData

# 获取登陆用户名称和密码
login_msg=SanJinXianFengLoginInfo()
print(login_msg.LoginName())
print(login_msg.LoginPasswordEncrypt())

sanjin = SanJinXianFengData(login_msg.LoginName(), login_msg.LoginPasswordEncrypt())
sanjin.login()

jifen = sanjin.jifen()
print("学习前积分:"+str(jifen[1]))

time.sleep(3)
article_list = sanjin.getariticle()
time.sleep(3)
sanjin.dianzanshoucang(article_list[5])
time.sleep(3)
sanjin.dianzanshoucang(article_list[6])
time.sleep(3)
sanjin.duwenzhang30s(article_list[5])
time.sleep(3)
sanjin.duwenzhang30s(article_list[6])
time.sleep(3)
sanjin.shitingxuexi()
time.sleep(3)

for i in range(40):
    sanjin.dati(str(i+1))
    time.sleep(2)

time.sleep(5)
jifen = sanjin.jifen()

if jifen[0] != 15:
    print("抱歉，今天未学习够15分，可能是哪里出问题啦")
else:
    print("干的漂亮，代码帮你学习获得了15分^v^")


study_after = sanjin.jifen()
print("学习后总积分:"+str(study_after[1]))
