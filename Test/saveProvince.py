# -*-coding:utf-8-*-
import time
import xlrd
import xlwt
import requests
from bs4 import BeautifulSoup


class SaveProvince():
    def __init__(self):
        title = ['province', 'city', 'country']
        # 新建工作蒲
        self.workbook = xlwt.Workbook()
        # 新建工作表并重命名
        self.worksheet = self.workbook.add_sheet("province")
        # 导入内容
        # worksheet.write(row, col, data)
        col = 0
        for t in title:
            self.worksheet.write(0, col, t)
            col += 1
        # 保存
        self.workbook.save('D:\gitProlan\Test\province.xlsx')


    # def write_pro(self):
    #     title = ['province','city','country']
    #     # 新建工作蒲
    #     workbook = xlwt.Workbook()
    #     # 新建工作表并重命名
    #     worksheet = workbook.add_sheet("province")
    #     # 导入内容
    #     # worksheet.write(row, col, data)
    #     col = 0
    #     for t in title:
    #         worksheet.write(0,col,t)s
    #         col +=1
    #     # 保存
    #     workbook.save('D:\gitProlan\Test\province.xlsx')
    #     return worksheet
    #

    def read_pro(self,row,col):
        # 1 打开工作薄（workbook.xlsx）
        excel_ = xlrd.open_workbook('D:\gitProlan\Test\province.xlsx')

        # 2 定位要读取内容的工作表
        # 两种方法：(1)索引；(2)表的名字
        # Table = excel_.sheet_by_index(0)  # 通过索引定位工作表，索引从0开始
        Table_1 = excel_.sheet_by_name('province')  # 通过表的名字定位工作表
        print("readsheet")
        print(row)
        print(col)
        # 3 读取单元格
        # 根据行列读取内容  3种写法，本质都是读取某行某列的值
        # print(Table.cell_value(row, col))
        print(Table_1.cell(row, col).value)

    def get_response(self,url,attr):
        headers = {
            'Connection': 'close'
        }
        response = requests.get(url,headers = headers) # 发送请求并获得返回
        response.encoding = 'UTF-8'  # 编码转换
        soup = BeautifulSoup(response.text, 'html.parser')  # 分析数据

        table = soup.find_all('tbody')[1].tbody.tbody.table
        if attr:
            trs = table.find_all('tr', attrs={'class': attr})
        else:
            trs = table.find_all('tr')
        return trs

    def deal_data(self):
        base_url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2021/'  # 地址数据url
        trs = self.get_response(base_url, 'provincetr')  # 获取返回值
        # print(trs)
        for tr in trs:  # 循环每一行
            row = 1
            pro_col = 0
            city_col = 1
            country_col = 2

            for tp in tr:  # 循环每个省
                province_name = tp.a.get_text()
                province_url = base_url + tp.a.attrs['href']
                print("province_name:" + province_name)
                print("province_url:" + province_url)
                trs = self.get_response(province_url, None)
                # print(trs)
                self.worksheet.write(row, pro_col, province_name)
                self.read_pro(row, pro_col)
                for tci in trs[1:]:  # 循环每个市
                    print("city")
                    # print(tci)
                    city_name = tci.find_all('td')[1].string
                    print("city_name")
                    print(city_name)
                    city_url = base_url + tci.a.attrs['href']
                    print('city_url')
                    print(city_url)
                    trs = self.get_response(city_url, None)
                    worksheet.write(row, city_col, city_name)
                    self.read_pro(row,city_col)
                    for tco in trs[1:]:
                        country_name = tco.find_all('td')[1].string
                        print("country_name")
                        print(country_name)
                        worksheet.write(row,country_col,country_name)
                        self.read_pro(row, country_col)
                        data = [province_name, city_name, country_name]  # 封装一条数据
                        print(data)

                        pro_col += 1
                        city_col += 1
                        country_col += 1
                        row += 1




SaveProvince().deal_data()
# if __name__ == ('__main__'):
#     read_pro()
