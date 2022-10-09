#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json,random,time

import xlrd
# from faker import Faker
from datetime import datetime
from kafka import KafkaProducer
from concurrent.futures import ProcessPoolExecutor,as_completed


class Test_KafkaProducer():
    def __init__(self):
        # self.fa = Faker(locale='zh_CN')
        self.producer = KafkaProducer(value_serializer=lambda m: json.dumps(m,ensure_ascii=False).encode(),
                                      bootstrap_servers='172.16.16.238:10020')

    def test_action(self):
        """
        0 = 未指定
        1 = 放行
        2 = 报警
        3 = 阻断
        :return:
        """
        Action = [ 1, 2, 3]
        val = random.choice(Action)
        return val

    def test_threat(self):
        """
        0 = 无风险
        1 = 低风险
        2 = 中风险
        3 = 高风险
        4 = 致命风险
        :return:
        """
        Threat = [0, 1, 2, 3, 4]
        val = random.choice(Threat)
        return val

    def data_json(self):
        dataexcel = xlrd.open_workbook('province1.xls')
        protable = dataexcel.sheet_by_name('province')
        ipmactable = dataexcel.sheet_by_name('ip_mac')
        datalis = []
        num = 100
        while num:
            if num % 10 == 0:
                prodata = protable.row_values(num)
            else:
                prodata = protable.row_values(num+1)
            # prodata = protable.row_values(1)
            ipdata = ipmactable.col_values(0)
            macdata = ipmactable.col_values(1)
            t = str(int(round((time.time()*1000))))
            deviceName = prodata[1]+prodata[2]+prodata[3]+'-功率控制系统'
            vendorChn = prodata[1]+'代理'
            # print(deviceName)
            data = {
                "deviceTypeOneName": "设备",
                "businessSoftware": [],
                "internal": "1",
                "isHaveDB": "0",
                "outageTime": "0",
                "deviceScore": "5",
                "licenseExpiredTime": "0",
                "storageTime": t,
                "vendorChn": vendorChn,
                "physicalRegion": "2",
                "deviceTypeTwo": "OWS",
                "inputTime": t,
                "deviceName": deviceName,
                "deviceTypeTwoName": "操作员站",
                "isVirtualMachine": "0",
                "safeDefendSoftware": [],
                "safetyOfTime": "0",
                "commissioningTime": "0",
                "security": "5",
                "database": [],
                "usability": "5",
                "orgCode": "00001000370000500007",
                "isFreeAsset": "0",
                "manageState": "0",
                "sourceCity": prodata[2],
                "ipList": [{
                    "type": "业务",
                    "ipAddr": ipdata[num],
                    "macAddr": macdata[num]
                }],
                "businessSector": "3",
                "sourceFactory": "two",
                "os": [],
                "isDelete": "0",
                "integrality": "5",
                "updateTime": "0",
                "deviceTypeOne": "5",
                "maintenanceTime": "0",
                "createTime": t,
                "sourceProvince": prodata[1],
                "isStandby": "0",
                "isImportantAsset": "0",
                "deviceModel": "SU-GAP2",
                "insertDataBaseFunction": "1",
                "sourcePrefecture": prodata[3],
                "otherSoftware": []

            }
            datalis.append(data)
            num -= 1
        print(len(datalis))
        return datalis


    def kafkaproducer(self):
        starttime = datetime.now()
        print('开始时间',starttime)
        i = 1
        #for i in range(10000):
        while True:
            self.producer.send('asset', self.data_json())
            print(self.data_json())
            i += 1
            if i == 10:
                time.sleep(1)
                i = 0
        #self.producer.close()
        endtime = datetime.now()
        print('进程耗时：', endtime - starttime)

if __name__ == '__main__':
    """
    说明：
        1.修改本地hosts-在hosts中添加数据资产平台的节点信息
            内容如下：
                172.16.8.180	manager.datafort
                172.16.8.181	node1.datafort
                172.16.8.182	node2.datafort
        2.控制数据量-修改kafkaproducer中循环的次数
        3.更换topic-修改kafkaproducer中producer.send的值
    """
    Test_KafkaProducer().kafkaproducer()
    # Test_KafkaProducer().data_json()
