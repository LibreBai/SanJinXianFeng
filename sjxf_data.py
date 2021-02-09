import requests
import json
import time
import base64

class SanJinXianFengData:
    __token = ''
    __id = ''
    __token_id_header = {}

    def __init__(self, login_name, login_password):
        self.__server_url="http://221.204.170.88:8184"
        # 只要符合标准的请求头即可，这个是我从模拟器拷贝出来的
        self.__header = \
                {
                    "Content-Type": "application/json; charset=utf-8",
                    "Host": "221.204.170.88:8184",
                    "Connection": "Keep-Alive",
                    "Accept-Encoding": "gzip",
                    "User-Agent": "okhttp/3.10.0"
                }
        self.__login_name = login_name
        self.__login_password = login_password

    def login(self):
        '''登陆账户'''
        post1_url = self.__server_url + "/app/userPrivacy"
        post2_url = self.__server_url + "/app/user/login"
    
        login_data1 = {"accout": self.__login_name}
        login_data2 = {"password": self.__login_password,
                "clientid":"234234",
                "deviceId":"imei862686246682036",
                "password": self.__login_password,
                "userName": self.__login_name,
                # 滑动验证码
                # "verifyCode":"Z2ZlMmZlbmdqaWFiaW4="
                }

        # 第一次post
        response = requests.post(post1_url, json=login_data1, headers=self.__header)
        # print(response.json())
        if not response.ok:
            return False

        # 第二次post
        response = requests.post(post2_url, json=login_data2, headers=self.__header)
        # print(response.json())
        # 解析返回内容，为啥使用base64解码原因暂不清楚
        userInfo = json.loads(response.text)['data']
        info = json.loads(base64.b64decode(userInfo))
        # print(info)
        # print(info['jwtToken'])
        # print(info['id'])
        self.__id = info['id']
        self.__token = info['jwtToken']

        # 组装http头部消息
        self.__token_id_header = {
            "Authorization": "Bearer " + info['jwtToken'],
            "sUserId": str(self.__id),
            "version": "3.3.4",
            "Content-Type": "application/json; charset=utf-8",
            "Connection": "Keep-Alive",
            "Host": "221.204.170.88:8184",
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/3.10.0"
        }

        if response.ok:
#            print("登陆成功")
            return True
#        print("登陆失败")
        else:
            return False
        
    def getariticle(self, pagenum:int=3):

        '''获取一个页面的文章'''
        article_num_list = []
        # 获取文章
        ariticle_list_url = self.__server_url +  \
                    "/app/study/list_article/72?size=10&page=" + str(pagenum)
        # print(ariticle_list_url)

        response = requests.get(ariticle_list_url, headers=self.__token_id_header)

        ariticle_json = json.loads(response.text)['data']

        for i in range(len(ariticle_json)):
            article_num_list.append(int(ariticle_json[i]["id"]))

        return article_num_list

    def duwenzhang30s(self, ArticleId:int):
        '''读一篇文章30s'''
        url = self.__server_url + "/app/businessScore"
        endtime = int(time.time())
        starttime = endtime - 35
        payload = {'userId': self.__id,
                   'time':'35',
                   'type': '1',
                   'articleId': str(ArticleId),
                   'ifScore':'1',
                   "appStartTime": starttime
                   }

        study_response = requests.post(url, headers=self.__token_id_header, json=payload)
        if study_response.ok:
            return True
        else:
            return False

    def dianzanshoucang(self, ArticleId:int):
        '''点赞收藏一篇文章'''
        data = {
            "type": "1",
            "userId": self.__id,
            "uniqueId": str(ArticleId),
        } 
        dianzan_url = self.__server_url + "/app/love"
        shoucang_url = self.__server_url + "/app/collect"
        quxiaodianzan_url = self.__server_url + "/app/loveCancelDelete"
        quxiaoshoucang_url = self.__server_url + "/app/collectCancelDelete"

        quxiaodianzan_respone = requests.post(quxiaodianzan_url, json=data, headers=self.__header)
        time.sleep(1)
        quxiaoshoucang_respone = requests.post(quxiaoshoucang_url, json=data, headers=self.__header)
        time.sleep(1)
        dianzan_respone = requests.post(dianzan_url, json=data, headers=self.__token_id_header)
        time.sleep(1)
        shoucang_respone = requests.post(shoucang_url, json=data, headers=self.__token_id_header)
        time.sleep(1)
        if quxiaodianzan_respone.ok and quxiaoshoucang_respone.ok and \
           dianzan_respone.ok and shoucang_respone.ok:
            return True
        else:
            return False

    def shitingxuexi(self, MovieOrMusicId:int):
        '''视听学习'''
        shiting_url = self.__server_url + "/app/businessScore"
        endtime = int(time.time())
        starttime = endtime - 10
        payload = {
                   'userId': str(self.__id),
                   'time':'35',
                   'type': '2',
                   'articleId': str(MovieOrMusicId),
                   'ifScore':'1',
                   "appStartTime": starttime
                   }

        response = requests.post(shiting_url, headers=self.__token_id_header, json=payload)
        if response.ok:
            return True
        else:
            return False

    def jifen(self):
        '''积分明细'''
        get_jifen_url = self.__server_url + "/app/home/totayScore"
        payload = {
                    'userId': self.__id,
                    'type': '2'
                  }

        headers = {
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Authorization': "Bearer "+self.__token,
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; Redmi K20 Pro Premium Edition Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045224 Mobile Safari/537.36',
            'Content-Type': 'application/json',
            'Origin': 'http: // sxzhdjkhd.sxdygbjy.gov.cn: 8081',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'Keep-Alive',
            'X-Requested-With': 'io.dcloud.H5B1841EE',
            'Accept-Encoding': 'gzip, deflate',
            'Accept': '*/*',
            'Referer': 'http: // sxzhdjkhd.sxdygbjy.gov.cn: 8081 / zhdj - pre / index.html',
            'Host': '221.204.170.88:8184',
        }
        s = requests.session()
        t = s.post(get_jifen_url, headers=headers, data=json.dumps(payload))
        todayScore = json.loads(t.text)
        # print("今天增加的分数是:"+str(todayScore['data']['todayScore']))
        # print("今年累计的分数是:"+str(todayScore['data']['yearScore']))

        return {'today_score': todayScore['data']['todayScore'],
                'total_score': todayScore['data']['yearScore']}

    def dati(self, themeId:str=""):
        '''
            "id:"",
            "name":"普通答题"
			"id":1,
			"name":"十九大精神"
			"id":2,
			"name":"平语近人"
			"id":3,
			"name":"疫情防控"
			"id":4,
			"name":"党章党规"
			"id":6,
			"name":"安全防护"
        '''

        tiku_url = self.__server_url + "/app/questionLib"
        uuid_url = self.__server_url + "/app/uuid"

        pageData = {"page": 1, "pageSize": 10, "themeId": themeId}
        dati_headers = {
            "Host": "221.204.170.210:8184",
            "Connection": "keep-alive",
            #"Content-Length": "37"
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Authorization": "Bearer "+self.__token,
            "Origin": "http://sxzhdjkhd.sxdygbjy.gov.cn:8081",
            "Content-Type": "application/json",
            "sUserId": str(self.__id),
            "User-Agent": "Mozilla/5.0 (Linux; Android 7.1.2; \
            G011C Build/N2G48H; wv) \
            AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 \
            Chrome/66.0.3359.158 Mobile Safari/537.36",
            "version": "3.3.4",
            "Accept": "*/*",
            "Referer": "http://sxzhdjkhd.sxdygbjy.gov.cn:8081/zhdj-pre/",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,en-US;q=0.9",
            "X-Requested-With": "io.dcloud.H5B1841EE",
        }

        answerList = []
        response = requests.post(tiku_url, json=pageData, headers=dati_headers)
        if not response.ok:
#            print("获取题库成功")
            return False

        list1 = json.loads(response.text)

        for data in list1['data']['list']:
            time.sleep(1)
            answerList.append({"selectAnswer": data['correctAnswer'], "grade": data['grade'], "ifCorrect": 1,
                               "questionCode": data['code'], "questionType": data['type']})

        uuidResponse = requests.get(uuid_url, headers=dati_headers).text
        uuidData = json.loads(uuidResponse)
        uuid = '"' + uuidData['data'] + '"'

        # 普通答题和模块答题返回码有差异
        if themeId == "":
            method = "1"
        else:
            method = "4"

        answer = {
                    "userId": str(self.__id),
                    "method": method,
                    "totalGrade": "100",
                    "list": answerList,
                    "summaryCode": uuid
                 }

        dumps = json.dumps(answer)
        answerResponse = requests.post("http://221.204.170.88:8184/app/question", data=dumps, headers=dati_headers)
        if answerResponse.ok:
#            print("答题成功")
            return True
        else:
#            print("答题失败")
            return False
