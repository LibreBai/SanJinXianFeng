# SanJinXianFeng自动学习工具

## 最新状态

**三晋先锋已被山西组织部放弃。 2021-10-11**


**好好学习，天天向上。**
**项目仅限用于学习研究。**

如果想尝试自动学习，请移步**使用说明**，根据说明进行操作。

## 入党誓词

>*我志愿加入中国共产党
>拥护党的纲领，遵守党的章程，履行党员义务，执行党的决定，
>严守党的纪律，保守党的秘密，对党忠诚，积极工作，
>为共产主义奋斗终身，
>随时准备为党和人民牺牲一切，永不叛党。*

## 使用说明

**关于如何分析通讯流程，请咨询博主 [RuiKaiWang的github](https://github.com/RuikaiWang/Study)。我目前能够分析通讯流程的办法只有Wireshark抓包分析一种。**

操作流程:

1. Windows 或者 Linux 安装 Git 工具，具体请百度。
1. 执行 `pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple pycryptodome` 获取依赖的三方库。
1. 打开 Windows 下 Git 工具或者打开 Linux 下终端，执行 `https://github.com/FenDou1204/SanJinXianFeng.git` 命令。
1. 生成名为 `SanJinXianFeng` 目录，进入此目录，编辑 `sjxf_user.conf` 文件，完善自己的用户名和密码，保存修改的内容。
3. 执行 `python3 sjxf_main.py` 来完成整个学习流程。

**如果报错请issue。^v^**

## 文件说明

1. 代码的运行依赖于 requests 库、json 库、pycryptodome 库，Centos8 系统前两个库默认都有，需要通过 `pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple pycryptodome` 安装了AES加密所需要的库。
2. sjxf_user.py 文件主要是解析配置文件，获取登陆用户名和密码，并且对于密码进行加密。
3. sjxf_data.py 文件用来完成各种数据的交互获取。
4. sjxf_main.py 文件是学习的主要执行流程，同时加入了执行时延，以避免结果错误或者增加服务器的压力。

## 感谢大佬

感谢 [RuiKaiWang的github](https://github.com/RuikaiWang/Study) 大佬。参考了他很多的内容，并且有部分内容至今还存在疑惑。
**如果侵权，请及时联系，我将第一时间删除。**

我在2021年1月7日-9日仔细抓包分析了当前的三晋先锋 http 交互流程，与大佬的实现方式进行了对比，整个流程目前还完全正常。
为了方便大家使用，对于其中的部分代码进行了修改，方便直接执行获取每日积分。

我主要是写 C++ 语言，Python 语言略知一二，代码风格主要按照 C++ 时候的习惯来完善。

## 存在疑惑

1. 密码的加密过程是如何分析得到的？密钥的来源是哪里？

## windows下安卓模拟器主动学习

1. 下载安装【逍遥模拟器】。
2. 下载三晋先锋 APP，并且在模拟器中安装。
3. 按照正常的学习方式进行学习。

## windows下抓包分析

1. 按照【windows下安卓模拟器主动学习】安装学习环境。
2. 安装 Wireshark 抓包工具。
3. 在学习过程的同时使用 Wireshark 进行抓包。分析其中的数据。
