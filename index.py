"""
   名称：首页后台
        
   简介：
        1.从csv文件中获取出数据提交给前端
        2.格式:
            {value: 335, name: '直接访问'},
            {value: 310, name: '邮件营销'},
            {value: 274, name: '联盟广告'},
            {value: 235, name: '视频广告'},
            {value: 400, name: '搜索引擎'}
"""
import json

from django.http import request
from django.shortcuts import render


class Data():
    def __init__(self):
        self.f = open('average_salary.csv', 'r')
        self.original_data_dict = {}
        self.update_data_dict = {}
        self.data_list = []

        self.city = []
        self.original = []

    def get_data(self):
        for i in self.f.readlines():
            # 平均工资"   平均工资右边必须有双引号,
            # 原数据  "城市,平均工资"        以逗号切割后数据:["城市][平均工资"]
            if i.split(",")[1].strip() == '平均工资"':
                continue
            average = i.split(",")[1].strip()
            city = i.split(",")[0].strip()

            self.original_data_dict[average] = city
        for key, val in self.original_data_dict.items():
            temporary = {}
            temporary['value'] = key
            temporary['name'] = val
            self.data_list.append(temporary)
        json_data = json.dumps(self.data_list, ensure_ascii=False)
        print(json_data)
        # return render(request, 'index.html', json_data)
        # print(json_data)
        # print(type(json_data))

    def list_data(self):
        for i in self.f.readlines():
            # 平均工资"   平均工资右边必须有双引号,
            # 原数据  "城市,平均工资"        以逗号切割后数据:["城市][平均工资"]
            if i.split(",")[1].strip() == '平均工资"':
                continue
            average = i.split(",")[1].strip()
            city = i.split(",")[0].strip()
            self.city.append(city)
            self.original.append(average)
        print(self.city)
        print(self.original)


da = Data()
da.list_data()
