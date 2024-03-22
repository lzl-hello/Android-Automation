import time
import unittest
import os
import base64
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.extensions.android.nativekey import AndroidKey
from appium.options.android import UiAutomator2Options


desired_caps = {
  'platformName': 'Android', # 被测手机是安卓
  'platformVersion': '13.0', # 手机安卓版本，如果是鸿蒙系统，依次尝试 12、11、10 这些版本号
  'deviceName': '4f421cb8', # 设备名，安卓手机可以随意填写
  'appPackage': 'com.tencent.mm', # 启动APP Package名称
  'appActivity': 'com.tencent.mm.ui.LauncherUI', # 启动Activity名称
#   'unicodeKeyboard': True, # 自动化需要输入中文时填True
#   'resetKeyboard': True, # 执行完程序恢复原来输入法
  'noReset': True,       # 不要重置App
  'fullReset': False,
  'newCommandTimeout': 6000,
  'automationName' : 'UiAutomator2', 
  "appium:enforceXPath1": True
}

# 连接Appium Server，初始化自动化环境
# driver = webdriver.Remote('http://localhost:4723/wd/hub', 
#   options=UiAutomator2Options().load_capabilities(desired_caps))


class TestAppium(unittest.TestCase):
    def BACK(self):
        self.driver.press_keycode(AndroidKey.BACK)
    def SWIPE(self):
        # 向下滑动
        self.driver.swipe(start_x=self.driver.get_window_size()['width']//2,start_y=self.driver.get_window_size()['height']*0.2,end_x=self.driver.get_window_size()['width']//2,end_y=self.driver.get_window_size()['height']*0.8,duration=500)
    def setUp(self) -> None:

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', 
               options=UiAutomator2Options().load_capabilities(desired_caps))

        self.driver.implicitly_wait(10)#缺省等待时间10s

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()


    def testwx(self) -> None:

# -----------------------------------------------------------------
        # 首页点击搜索，输入hit

        # search = self.driver.find_element(by=AppiumBy.XPATH,value='//android.widget.RelativeLayout[@content-desc="搜索"]')
        # search.click()

        # Mini_programs = self.driver.find_element(by=AppiumBy.XPATH,value='//*[@text="搜索"]')
        # # Mini_programs.click()
        # Mini_programs.send_keys("hit")

        # search_content = self.driver.find_element(by=AppiumBy.XPATH,value="//*[@resource-id='com.tencent.mm:id/m88']")
        # search_content.click()

        # time.sleep(20)
        # 等待activity出现
        # self.driver.wait_activity("/.plugin.appbrand.ui.AppBrandPluginUI", 10)
        # print(self.driver.current_activity)

        # self.driver.implicitly_wait(30)#缺省等待时间

# 这里定位不到  在github上提了issue，他们说不是appium的问题，是uiautomator2和应用程序本身的问题
# error：Caused by: io.appium.uiautomator2.common.exceptions.UiAutomator2Exception: Timed out after 15557ms waiting for the root AccessibilityNodeInfo in the active window. Make sure the active window is not constantly hogging the main UI thread (e.g. the application is being idle long enough), so the accessibility manager could do its work
        # Mini_programs1 = self.driver.find_element(by=AppiumBy.XPATH,value='//*[@text="小程序"]')
        # Mini_programs1.click()


# *************************************************
# 向下滑动点击跳一跳小程序

        # self.SWIPE()
        # test = self.driver.find_element(by=AppiumBy.XPATH,value='//*[@text="跳一跳"]')
        # if test:
        #     print("OK~")
        #     test.click()
        # else:
        #     print("sorry!")

        # time.sleep(3)
        # self.BACK()


        print("------跳转发现页面------")
        discover = self.driver.find_element(by=AppiumBy.XPATH,value='//*[@text="发现"]')
        if discover:
            print("OK~")
            discover.click()

        print("------跳转小程序页面------")
        Mini_programs = self.driver.find_element(by=AppiumBy.XPATH,value='//*[@text="小程序"]')
        if Mini_programs:
            print("OK~")    
            Mini_programs.click()
        # 点击右上角搜索按钮
        os.system("adb shell input tap 888 155")
        time.sleep(2)
        # 输入
        os.system("adb shell am broadcast -a ADB_INPUT_TEXT --es msg '银行'")
        time.sleep(2)
        # 点击搜索
        os.system("adb shell input tap 975 165")
        time.sleep(2)


        os.system("adb shell input tap 500 314")
        time.sleep(5)
        os.system("adb shell input tap 966 175")
        time.sleep(3)

        os.system("adb shell input tap 500 627")
        time.sleep(5)
        os.system("adb shell input tap 966 175")
        time.sleep(3)

        os.system("adb shell input tap 500 925")
        time.sleep(5)
        os.system("adb shell input tap 966 175")
        time.sleep(3)

        os.system("adb shell input tap 500 1251")
        time.sleep(5)
        os.system("adb shell input tap 966 175")
        time.sleep(3)

        os.system("adb shell input tap 500 1566")
        time.sleep(5)
        os.system("adb shell input tap 966 175")
        time.sleep(3)

        os.system("adb shell input swipe 500 1875 500 314 1000")

        # 按理说这边只要写一个循环就可以遍历点击了，可是实际测试中根据位置点击变数太多，效果很差；后续再想想还有什么好办法吧。累了哥！





    




if __name__ == '__main__':
    unittest.main()