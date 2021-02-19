'''
解析用户配置文件
'''

#密码加密
from Crypto.Cipher import AES
import base64
#配置文件解析'
import configparser

class EncryptData:
    def __init__(self):
        self.key = "sanjinxianfengya".encode("utf8")  # 初始化密钥
        # self.key = "1111111111111111".encode("utf8")  # 初始化密钥 这行只是测试密钥对于密码的影响，并无实际意义
        self.length = AES.block_size  # 初始化数据块大小
        self.aes = AES.new(self.key, AES.MODE_ECB)  # 初始化AES,ECB模式的实例
        self.unpad = lambda date: date[0:-ord(date[-1])]

    def pad(self, text):
        count = len(text.encode('utf-8'))
        add = self.length - (count % self.length)
        entext = text + (chr(add) * add)
        return entext

    def encrypt(self, encrData):  # 加密函数
        res = self.aes.encrypt(self.pad(encrData).encode("utf8"))
        msg = str(base64.b64encode(res), encoding="utf8")
        return msg

    def decrypt(self, decrData):  # 解密函数
        res = base64.decodebytes(decrData.encode("utf8"))
        msg = self.aes.decrypt(res).decode("utf8")
        return self.unpad(msg)


class SanJinXianFengLoginInfo:
    # __login_name = ''
    # __login_password = ''

    def __init__(self, Path="sjxf_user.conf"):
        self.__user_conf_path = Path
    
        self.__login_msg = configparser.ConfigParser()
        self.__login_msg.read(self.__user_conf_path, encoding='utf-8')

    def CheckNecessaryParam(self):
        self.__login_name = self.__login_msg["login"]["login_name"]
        self.__login_password = self.__login_msg["login"]["login_password"]
        
        if len(self.__login_name) != 0 and len(self.__login_password) != 0:
            return True
        else:
            return False
    
    def LoginName(self) -> str:
        return self.__login_name

    def LoginPassword(self) -> str:
        return self.__login_password

    def LoginPasswordEncrypt(self) -> str:
        Encrypto = EncryptData()
        return Encrypto.encrypt(self.__login_password)


#login = SanJinXianFengLoginInfo()
#if login.CheckNecessaryParam():
#    print("必要参数合法")
#else:
#    print("错误，未配置必要登录信息，请修改sjxf_user.conf文件")
