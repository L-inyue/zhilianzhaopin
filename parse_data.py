"""
   名称:智联职业数据提取
        
   简介：
        1.从数据库中提取出数据
        2.分析数据
        3.生成每个城市的工资信息放到列表
        4.返回变量名或字典
"""
import csv

import pymysql
from pypinyin import lazy_pinyin


class Parse_data():
    def __init__(self):
        self.db = pymysql.connect(
            host='127.0.0.1',
            user='root',
            password='123456',
            port=3306,
            charset='utf8',
            database='zhilian'
        )
        self.cur = self.db.cursor()
        self.data_dict = {}
        self.average_dict = {}
        self.kw=None

    def select_all_data(self):
        sel = 'select * from zhilian.%s' % self.kw
        self.cur.execute(sel)
        all_data = self.cur.fetchall()
        print(all_data)
        return all_data

    def parse_all_data(self):

        all_data = self.select_all_data()
        for i in all_data:
            if '-' in i[1]:
                city = i[1].split("-")[0]
            else:
                city = i[1]
            if '-' in i[3]:
                # 取最低工资
                salary = i[3].split("-")[0]
            elif i[3] == "薪资面议":
                salary = '薪资面议:待定....此处应该求平局值'
            if city in self.data_dict.keys():
                salary_list = self.data_dict[city]
                salary_list.append(salary)
            else:
                salary_list = []
                salary_list.append(salary)
                self.data_dict[city] = salary_list

        # print(self.data_dict)
        # {'北京':[薪资列表],'杭州':[薪资列表]}         薪资列表中有可能存在 --->  薪资面议

        for city, salary_city_list in self.data_dict.items():
            city, avg_salary = self.average_salary_dict(city, salary_city_list)
            self.average_dict[city] = avg_salary
        print(self.average_dict)
        with open('average_salary.csv', 'w', encoding='utf-8') as f:
            filename = ['城市,平均工资']
            csvwriter = csv.writer(f)
            csvwriter.writerow(filename)
            for c in self.average_dict.items():
                print(c)
                csvwriter.writerow(c)

    def average_salary_dict(self, city, salary_city_list):
        # 面议计数
        negotiable = 0
        salary_one_list = []
        sum_salary = 0
        # salary_list = self.data_dict[city]
        for salary in salary_city_list:
            if salary == '薪资面议:待定....此处应该求平局值':
                negotiable += 1
            else:
                salary_one_list.append(salary.split("K")[0])
            # 脑子炸裂了.缓缓

        # 打印出每个城市,所有工资和薪资面议的个数
        # print(city, salary_one_list, negotiable)

        for one in salary_one_list:
            sum_salary += float(one)
        if not len(salary_one_list) == 0:
            avg_salary = round(sum_salary / (len(salary_one_list)), 2)  # +negotiable
            # avg_salary += avg_salary * negotiable
        else:
            avg_salary = "全是工资面议有点难以置信"
        return city, avg_salary

    def run(self,name):
        self.kw=name
        self.parse_all_data()


if __name__ == '__main__':
    parse_data = Parse_data()
    str_key=input('请输入你要分析的职业信息:')
    name_list = lazy_pinyin(str_key)
    name = ''
    for i in name_list:
        name += i
    parse_data.run(name)
