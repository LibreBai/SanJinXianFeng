# SanJinXianFeng自动学习工具

好好学习，天天向上。

## 重温入党誓词
    我志愿加入中国共产党
    拥护党的纲领，遵守党的章程，履行党员义务，执行党的决定，
    严守党的纪律，保守党的秘密，对党忠诚，积极工作，
    为共产主义奋斗终身，
    随时准备为党和人民牺牲一切，永不叛党。

## 感谢大佬
如果侵权，请提交issue，我将第一时间删除.大佬的github请点击[RuiKaiWang的github](https://github.com/RuikaiWang/Study).

我在2021年1月7日-9日仔细抓包分析了当前的三晋先锋http交互，大佬之前的分析完全可用。为了方便大家使用，对于其中的部分代码进行了修改，满足一些非码农使用

首先对于github大佬@RuikaiWang的突出贡献表达最真诚的致意。没有大佬，也就没有这些功能，同时也没有我对于三晋先锋app的详细，对于python的温习。

## 使用方法
1. 使用`git clone https://github.com/YangWangXingKong1204/SanJinXianFeng.git`命令行获取代码文件，此步骤会在执行命令行的地方生成名为`SanJinXianFeng`的目录名
2. 命令行执行`pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple pycryptodome`
2. 进入此目录，编辑`sjxf_user.conf`, 完善自己的用户名和密码,保存修改的内容
3. 使用`python3 sjxf_main.py`来自动化完成整个流程。整个流程大概使用1分钟。

**如果报错请issue。^v^**
**如果有大佬乐意写个安装依赖的requirement.txt那可在号不过了。本职工作不是python开发，这些内容还需学习才能进行完善**

## 文件说明
1. 代码的运行依赖于requests库、json库、pycryptodome库,我在centos8系统运行时，前两个库默认都有，只通过`pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple pycryptodome`安装了AES加密所需要的库
2. sjxf_user.py 文件主要是解析配置文件，获取登陆用户和密码,并且对于密码进行加密
3. sjxf_data.py 文件是用来完成各种数据的交互
4. sjxf_main.py 文件是学习的主要执行流程，其中加入了时延，实测如果不加时延，可能获取的结果有异常。

## 存在疑惑
1. 密码的加密过程是如何分析得到的？密钥的来源是哪里？

## windows下安卓模拟器主动学习

## windows下抓包分析