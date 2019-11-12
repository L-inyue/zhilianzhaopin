"""
   名称：获取全国城市的id
        
   简介：
        1.智联招聘的全国城市id
"""


class City():
    def __init__(self):
        self.city = [
            {"name": "安徽", "code": "541"},
            {"name": "澳门", "code": "562"},
            {"name": "北京", "code": "530"},
            {"name": "重庆", "code": "551"},
            {"name": "福建", "code": "542"},
            {"name": "甘肃", "code": "557"},
            {"name": "广东", "code": "548"},
            {"name": "贵州", "code": "553"},
            {"name": "海南", "code": "550"},
            {"name": "河北", "code": "532"},
            {"name": "黑龙江", "code": "537"},
            {"name": "河南", "code": "545"},
            {"name": "湖北", "code": "546"},
            {"name": "湖南", "code": "547"},
            {"name": "江苏", "code": "539"},
            {"name": "江西", "code": "543"},
            {"name": "吉林", "code": "536"},
            {"name": "吉林", "code": "536"},
            {"name": "辽宁", "code": "535"},
            {"name": "宁夏", "code": "559"},
            {"name": "青海", "code": "558"},
            {"name": "山东", "code": "544"},
            {"name": "上海", "code": "538"},
            {"name": "陕西", "code": "556"},
            {"name": "山西", "code": "533"},
            {"name": "四川", "code": "552"},
            {"name": "台湾省", "code": "563"},
            {"name": "天津", "code": "531"},
            {"name": "香港", "code": "561"},
            {"name": "新疆", "code": "560"},
            {"name": "西藏", "code": "555"},
            {"name": "云南", "code": "554"},
            {"name": "浙江", "code": "540"},
        ]

    def ret_code(self, name):
        for i in self.city:
            if name == i['name']:
                return i['code']

    def con_code(self):
        c_code = []
        for code in self.city:
            c_code.append(code['code'])
        return c_code
