# -*-coding:utf-8-*-
import requests
from bs4 import BeautifulSoup
class get_data():
    def get_response(self, url, attr):
        headers = {
            'Connection': 'close'
        }
        response = requests.get(url, headers=headers)  # 发送请求并获得返回
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
        print(trs)
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
                print(trs)
                # self.write_pro(row, pro_col, province_name)
                for tci in trs[1:]:  # 循环每个市
                    print("city")
                    print(tci)
                    city_name = tci.find_all('td')[1].string
                    print("city_name")
                    print(city_name)
                    city_url = base_url + tci.a.attrs['href']
                    print('city_url')
                    print(city_url)
                    trs = self.get_response(city_url, None)
                    # self.write_pro(row, city_col, city_name)
                    for tco in trs[1:]:
                        country_name = tco.find_all('td')[1].string
                        print("country_name")
                        print(country_name)
                        # self.write_pro(row,country_col,country_name)
                        data = [province_name, city_name, country_name]  # 封装一条数据
                        print(data)

            pro_col += 1
            city_col += 1
            country_col += 1
            row += 1

if __name__ == '__main__':
    get_data().deal_data()
