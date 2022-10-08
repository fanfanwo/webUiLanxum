# -*-coding:utf-8-*-
import time
import xlrd
import xlwt
import requests
from bs4 import BeautifulSoup


class SaveProvince():
    def __init__(self):
        title = ['province', 'city', 'country']
        # �½�������
        self.workbook = xlwt.Workbook()
        # �½�������������
        self.worksheet = self.workbook.add_sheet("province")
        # ��������
        # worksheet.write(row, col, data)
        col = 0
        for t in title:
            self.worksheet.write(0, col, t)
            col += 1
        # ����
        self.workbook.save('D:\gitProlan\Test\province.xlsx')


    # def write_pro(self):
    #     title = ['province','city','country']
    #     # �½�������
    #     workbook = xlwt.Workbook()
    #     # �½�������������
    #     worksheet = workbook.add_sheet("province")
    #     # ��������
    #     # worksheet.write(row, col, data)
    #     col = 0
    #     for t in title:
    #         worksheet.write(0,col,t)s
    #         col +=1
    #     # ����
    #     workbook.save('D:\gitProlan\Test\province.xlsx')
    #     return worksheet
    #

    def read_pro(self,row,col):
        # 1 �򿪹�������workbook.xlsx��
        excel_ = xlrd.open_workbook('D:\gitProlan\Test\province.xlsx')

        # 2 ��λҪ��ȡ���ݵĹ�����
        # ���ַ�����(1)������(2)�������
        # Table = excel_.sheet_by_index(0)  # ͨ��������λ������������0��ʼ
        Table_1 = excel_.sheet_by_name('province')  # ͨ��������ֶ�λ������
        print("readsheet")
        print(row)
        print(col)
        # 3 ��ȡ��Ԫ��
        # �������ж�ȡ����  3��д�������ʶ��Ƕ�ȡĳ��ĳ�е�ֵ
        # print(Table.cell_value(row, col))
        print(Table_1.cell(row, col).value)

    def get_response(self,url,attr):
        headers = {
            'Connection': 'close'
        }
        response = requests.get(url,headers = headers) # �������󲢻�÷���
        response.encoding = 'UTF-8'  # ����ת��
        soup = BeautifulSoup(response.text, 'html.parser')  # ��������

        table = soup.find_all('tbody')[1].tbody.tbody.table
        if attr:
            trs = table.find_all('tr', attrs={'class': attr})
        else:
            trs = table.find_all('tr')
        return trs

    def deal_data(self):
        base_url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2021/'  # ��ַ����url
        trs = self.get_response(base_url, 'provincetr')  # ��ȡ����ֵ
        # print(trs)
        for tr in trs:  # ѭ��ÿһ��
            row = 1
            pro_col = 0
            city_col = 1
            country_col = 2

            for tp in tr:  # ѭ��ÿ��ʡ
                province_name = tp.a.get_text()
                province_url = base_url + tp.a.attrs['href']
                print("province_name:" + province_name)
                print("province_url:" + province_url)
                trs = self.get_response(province_url, None)
                # print(trs)
                self.worksheet.write(row, pro_col, province_name)
                self.read_pro(row, pro_col)
                for tci in trs[1:]:  # ѭ��ÿ����
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
                        data = [province_name, city_name, country_name]  # ��װһ������
                        print(data)

                        pro_col += 1
                        city_col += 1
                        country_col += 1
                        row += 1




SaveProvince().deal_data()
# if __name__ == ('__main__'):
#     read_pro()
