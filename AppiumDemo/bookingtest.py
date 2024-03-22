import time
import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.extensions.android.nativekey import AndroidKey

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    appPackage='com.booking',
    appActivity='.startup.HomeActivity',
    language='en',
    locale='US'
)

appium_server_url = 'http://localhost:4723'

class TestAppium(unittest.TestCase):
    def BACK(self):
        self.driver.press_keycode(AndroidKey.BACK)
    def SWIPE(self):
        self.driver.swipe(start_x=self.driver.get_window_size()['width']//2,start_y=self.driver.get_window_size()['height']*0.8,end_x=self.driver.get_window_size()['width']//2,end_y=self.driver.get_window_size()['height']*0.2,duration=500)
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, capabilities)
        self.driver.implicitly_wait(10)#缺省等待时间10s

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def testbooking(self) -> None:
        f1 = self.driver.find_element(by=AppiumBy.XPATH,value='//*[@text="Agree"]')#同意使用应用
        if f1:
            f1.click()
        f1_1= self.driver.find_element(by=AppiumBy.XPATH,value='//*[@text="Accept"]')#同意Cookie
        if f1_1:
            f1_1.click()
        f2 = self.driver.find_element(by=AppiumBy.ID,value='com.booking:id/bui_input_choice_container_content')#勾选同意框
        if f2:
            f2.click()
        f3 = self.driver.find_element(by=AppiumBy.XPATH,value='//*[@text="Continue with email"]')#使用邮箱登录
        if f3:
            f3.click()
        f4 = self.driver.find_element(by=AppiumBy.CLASS_NAME,value='android.widget.EditText')#定位账号输入框
        if f4:
            f4.send_keys("burdach2568@gmail.com")
        f5 = self.driver.find_element(by=AppiumBy.XPATH,value='//*[@text="Continue"]')#同意使用应用
        if f5:
            f5.click()
        f6 = self.driver.find_element(AppiumBy.ID,value="com.booking:id/identity_text_input_edit_text")#定位密码输入框
        if f6:
            f6.send_keys("5684357951Si")
        f7 = self.driver.find_element(by=AppiumBy.XPATH,value='//*[@text="Sign in"]')#确认登录
        if f7:
            f7.click()
        f8 = self.driver.find_element(by=AppiumBy.XPATH,value='//android.widget.Button[@content-desc="Enter your destination"]') 
        if f8:
            f8.click()
        f9 = self.driver.find_element(by=AppiumBy.ID,value='com.booking:id/facet_with_bui_free_search_booking_header_toolbar_content') #定位输入框
        if f9:
            f9.send_keys('Tokyo')
        time.sleep(3)
        f10 = self.driver.find_element(by=AppiumBy.XPATH,value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]')  #选中搜索结果中的第一个
        if f10:
            f10.click()
        f11 = self.driver.find_element(by=AppiumBy.ID,value='com.booking:id/facet_date_picker_confirm') #选择日期
        if f11:
            f11.click()
        f12 = self.driver.find_element(by=AppiumBy.XPATH,value='//android.view.View[@content-desc="Accommodation search box"]/android.view.View/android.widget.Button') #搜索
        if f12:
            f12.click()
        time.sleep(1)
        f13 = self.driver.find_element(AppiumBy.XPATH,value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.ViewGroup/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.ViewGroup/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.ViewGroup/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]')#点击第一个住宿信息
        if f13:
            f13.click()
        f14 = self.driver.find_element(AppiumBy.CLASS_NAME,value='android.widget.ImageView')  #点击第一个图片
        if f14:
            f14.click()
            time.sleep(2)        
            self.BACK()
        f15 = self.driver.find_element(AppiumBy.ID,value='com.booking:id/select_room_cta') #查看我的选项
        if f15:
            f15.click()
        f16 = self.driver.find_element(AppiumBy.XPATH,value='//*[@text="SELECT"]')  #SELECT
        if f16:
            f16.click()
        f17 = self.driver.find_element(AppiumBy.ID,value='com.booking:id/main_action')  #Reserve
        if f17:
            f17.click()
            time.sleep(2)
            for _ in range(4):
                self.BACK()                         
        time.sleep(2)
        element_texts = ["Saved", "Bookings", "Profile", "Search"]
        for text in element_texts:
            xpath = f'//*[@text="{text}"]'
            element = self.driver.find_element(AppiumBy.XPATH, value=xpath)
            if element:
                element.click()
                time.sleep(2)
        self.SWIPE() #滑动屏幕
        f18 = self.driver.find_element(AppiumBy.XPATH,value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[4]')
        if f18:
            f18.click()
            time.sleep(3)
        #滑动屏幕
        self.SWIPE()
        input('等待')

if __name__ == '__main__':
    unittest.main()