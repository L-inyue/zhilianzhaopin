"""
   名称：代理ip

   简介：
        1.从redis数据库中获取出可用的ip
        2.更新redis中的ip
            python3 ./IPproxy-master/proxy.py
"""

from redis import StrictRedis
import random

class Proxy_ip():
    def __init__(self):
        self.redis = StrictRedis(
            host='localhost',
            port=6379,
            db=1,
            password=''
        )

    def get_ip(self):
        # 返回两个列表,一个为http,另一个https
        str_list = self.redis.get('proxies').decode()
        ip_list = str_list.replace("[", "").replace("]", "").split(",")
        http_list = []
        https_list = []
        # eval(ip_list.replace("[","").replace("]","").split(",")[0].replace("'",'"'))
        for ip in ip_list:
            ip = eval(ip.replace("'", '"'))
            if 'http' in ip.keys():
                http_list.append(str(ip).replace(" ",""))
            else:
                https_list.append(str(ip).replace(" ",""))
        http=random.choice(http_list)
        https=random.choice(https_list)
        # print(http.replace("{","").replace("}",""))
        # print(https.replace("{","").replace("}",""))
        dict_ = dict()
        dict_["http"]= eval(http)["http"]
        dict_["https"]= eval(https)["https"]
        return dict_


if __name__ == '__main__':
    pro = Proxy_ip()
    pro.get_ip()
