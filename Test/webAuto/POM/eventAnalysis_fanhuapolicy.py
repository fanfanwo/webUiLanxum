from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait #导包等待的对象
from selenium.webdriver.support import expected_conditions as EC #导包的条件集合包（模块）文件

class EventAnalysis_fanhuaPolicy:
    def __init__(self,driver):
        self.driver = driver

    class Button:
        eventAnalysis = (By.XPATH,'//li[text()=" 事件分析 "]')
        fanhua = (By.XPATH,'//a[text()=" 范化 "]')
        policy = (By.XPATH,'//li[text()="策略"]')

        all_policy = (By.XPATH,'//span[text()="全部"]')
        #所有的悬浮操作按钮
        floats = (By.XPATH,'//button[@class="popTipButton ivu-btn ivu-btn-text ivu-btn-small"]')
        # 82组 -全部设备类型没有删除，所以删除是81组
        create_device_types = (By.XPATH,'//li[text()="新建设备类型"]')
        create_son_policy_groups = (By.XPATH, '//li[text()="新建子策略组"]')
        edit_son_policy_groups = (By.XPATH, '//li[text()="编辑设备类型"]')
        delete_device_types = (By.XPATH,'//li[text()="删除设备类型"]')
        #新建策略
        create_policy = (By.XPATH,'//span[text()="新建 "]')
        # edit_policy = (By.XPATH,)

    class Dialog:
        #新建 编辑 删除 设备类型；新建 编辑 删除 策略组
        class Header:
            create_device_type = (By.XPATH,'//div[text()="新建设备类型"]')
            create_policy_group = (By.XPATH, '//div[text()="新建策略组"]')
            edit_device_type = (By.XPATH, '//div[text()="编辑设备类型"]')
            delete_device_type = (By.XPATH, '//span[text()="删除设备类型"]')
            edit_policy_group = (By.XPATH,'//div[text()="编辑策略组"]')
            delete_policy_group = (By.XPATH, '//span[text()="删除策略组"]')
        class Input:
            device_name = (By.XPATH,'//input[@placeholder="名称不超过32个字符"]')
            description = (By.XPATH,'//textarea[@placeholder="描述不超过128个字符"]')
        class Button:
            deletes = (By.XPATH,'//span[text()="删除"]')
            delete_cancel_xs = (By.XPATH,'//i[@class="ivu-icon ivu-icon- ivu-v2 ios-close-empty"]')
            closes = (By.XPATH,'//i[@class="ivu-icon ivu-icon-ios-close"]')
            cancels = (By.XPATH,'//span[text()="取消"]')
            cancels = (By.XPATH,'//span[text()="确认"]')

    class PolicyDrawer:
        policy_names = (By.XPATH,'//input[@placeholder="名称不超过64个字符"]')
        device_types = (By.XPATH,'//i[@class="ivu-icon ivu-icon-ios-arrow-down ivu-cascader-arrow"]')
        device_type_selectors = (By.XPATH,'//li[@class="ivu-cascader-menu-item"]')
        groups = (By.XPATH,'//span[text()="请选择"]')
        enable_state = (By.XPATH,'/html/body/div[12]/div[2]/div/div/div[2]/form/div[4]/div/div/label[1]')
        policy_descriptions = (By.XPATH,'//input[@placeholder="名称不超过128个字符"]')
        log_sample = (By.XPATH,'/html/body/div[12]/div[2]/div/div/div[2]/form/div[6]/div/div/textarea')
        RegExp = (By.XPATH,'/html/body/div[12]/div[2]/div/div/div[2]/form/div[7]/div/div/textarea')
        extract_field = (By.XPATH,'/html/body/div[12]/div[2]/div/div/div[2]/form/div[8]/div/button/span')
        #字段名框
        field_name_selectors = []
        for i in range(1, 5):
            field_name_selectors.append('/html/body/div[12]/div[2]/div/div/div[2]/form/div[9]/form['+str(i)+']/div[3]/div/div/div[1]/div/input')
        field_name_selector1 = (By.XPATH, field_name_selectors[0])
        field_name_selector2 = (By.XPATH, field_name_selectors[1])
        field_name_selector3 = (By.XPATH, field_name_selectors[2])
        field_name_selector4 = (By.XPATH, field_name_selectors[3])
        #字段名下拉选择框： i = 1-206， 3：事件名称，4：事件分类，18：源MAC地址，16：源IP地址，86：标签，33：动作
        '/html/body/div[12]/div[2]/div/div/div[2]/form/div[9]/form[1]/div[3]/div/div/div[2]/ul[2]/li[3]'
        fieldnames = [0]
        for i in range(1,5):
            for j in range(1,207):
                fieldnames.append('/html/body/div[12]/div[2]/div/div/div[2]/form/div[9]/form['+str(i)+']/div[3]/div/div/div[2]/ul[2]/li['+str(j)+']')

        field_name_eventname = (By.XPATH,fieldnames[3])
        field_name_eventtype = (By.XPATH, fieldnames[210])
        field_name_eventSrcMac = (By.XPATH, fieldnames[430])
        field_name_eventSrcIp = (By.XPATH, fieldnames[634])
        #赋值方式 框
        express_value_selectors = []
        for i in range(1, 5):
            express_value_selectors.append(
                '/html/body/div[12]/div[2]/div/div/div[2]/form/div[9]/form[' + str(i) + ']/div[4]/div/div/div[1]/div/span')
        express_value_selector1 = (By.XPATH, express_value_selectors[0])
        express_value_selector2 = (By.XPATH, express_value_selectors[1])
        express_value_selector3 = (By.XPATH, express_value_selectors[2])
        express_value_selector4 = (By.XPATH, express_value_selectors[3])
        #赋值方式下拉选择框
        express_values = []
        for i in range(1, 5):
            for j in range(1,5):
                express_values.append('/html/body/div[12]/div[2]/div/div/div[2]/form/div[9]/form['+ str(i) +']/div[4]/div/div/div[2]/ul[2]/li['+ str(j) +']')

        express_value_dir1 = (By.XPATH, express_values[0])
        # express_value_map = (By.XPATH, express_values[1])
        # express_value_fun = (By.XPATH, express_values[2])
        # express_value_rel = (By.XPATH, express_values[3])
        express_value_dir2 = (By.XPATH, express_values[4])
        express_value_dir3 = (By.XPATH, express_values[8])
        express_value_dir4 = (By.XPATH, express_values[12])

        affirm_button = (By.XPATH,'/html/body/div[12]/div[2]/div/div/div[2]/div/button[2]')
    def create_policy(self):
        print("事件分析")
        # 显性等待
        WebDriverWait(self.driver,10,0.5).until(EC.visibility_of_element_located(self.Button.eventAnalysis)).click()
        # self.driver.find_element(*self.Button.eventAnalysis).screenshot(f"截图/事件分析元素.png")
        WebDriverWait(self.driver,10,0.5).until(EC.visibility_of_element_located(self.Button.fanhua)).click()
        # self.driver.find_element(*self.Button.fanhua).screenshot(f"截图/范化元素.png")
        WebDriverWait(self.driver,10,0.5).until(EC.visibility_of_element_located(self.Button.policy)).click()
        # self.driver.find_element(*self.Button.policy).screenshot(f"截图/策略.png")
        self.driver.find_element(*self.Button.create_policy).click()
        time.sleep(10)
        self.driver.find_elements(*self.PolicyDrawer.policy_names)[1].send_keys("fcy")
        self.driver.find_elements(*self.PolicyDrawer.device_types)[1].click()

        #自定义的设备类型FAN
        self.driver.find_elements(*self.PolicyDrawer.device_type_selectors)[11].click()
        self.driver.find_element(*self.PolicyDrawer.enable_state).click()
        self.driver.find_element(*self.PolicyDrawer.enable_state).screenshot(f"截图/状态.png")
        # self.driver.find_elements(*self.PolicyDrawer.policy_descriptions)[1].screenshot(f"截图/策略描述.png")
        self.driver.find_element(*self.PolicyDrawer.log_sample).send_keys("8|6|Mac|ip|")
        # self.driver.find_element(*self.PolicyDrawer.log_sample).screenshot(f"截图/日志样本.png")
        self.driver.find_element(*self.PolicyDrawer.RegExp).send_keys("\A([^\|]*)\|([^\|]*)\|([^\|]*)\|([^\|]*)\|")
        # self.driver.find_element(*self.PolicyDrawer.RegExp).screenshot(f"截图/正则表达式.png")
        # self.driver.find_element(*self.PolicyDrawer.extract_field).screenshot(f"截图/提取字段.png")
        self.driver.find_element(*self.PolicyDrawer.extract_field).click()
        #字段名赋值
        WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located(self.PolicyDrawer.field_name_selector1)).click()
        WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located(self.PolicyDrawer.field_name_eventname)).click()

        self.driver.find_element(*self.PolicyDrawer.field_name_selector2).click()
        # self.driver.find_element(*self.PolicyDrawer.field_name_eventtype).screenshot(f"截图/事件分类.png")
        self.driver.find_element(*self.PolicyDrawer.field_name_eventtype).click()
        self.driver.find_element(*self.PolicyDrawer.field_name_selector3).click()
        # self.driver.find_element(*self.PolicyDrawer.field_name_eventSrcMac).screenshot(f"截图/源MAC地址.png")
        self.driver.find_element(*self.PolicyDrawer.field_name_eventSrcMac).click()
        self.driver.find_element(*self.PolicyDrawer.field_name_selector4).click()
        # self.driver.find_element(*self.PolicyDrawer.field_name_eventSrcIp).screenshot(f"截图/源IP地址.png")
        self.driver.find_element(*self.PolicyDrawer.field_name_eventSrcIp).click()
        #选择赋值方式
        self.driver.find_element(*self.PolicyDrawer.express_value_selector1).click()
        WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located(self.PolicyDrawer.express_value_dir1)).click()
        self.driver.find_element(*self.PolicyDrawer.express_value_selector2).click()
        WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located(self.PolicyDrawer.express_value_dir2)).click()
        # self.driver.find_element(*self.PolicyDrawer.express_value_dir2).click()
        self.driver.find_element(*self.PolicyDrawer.express_value_selector3).click()
        WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located(self.PolicyDrawer.express_value_dir3)).click()
        # self.driver.find_element(*self.PolicyDrawer.express_value_dir3).click()
        self.driver.find_element(*self.PolicyDrawer.express_value_selector4).click()
        WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located(self.PolicyDrawer.express_value_dir4)).click()
        # self.driver.find_element(*self.PolicyDrawer.express_value_dir4).click()
        #确认按钮
        self.driver.find_element(*self.PolicyDrawer.affirm_button).click()


