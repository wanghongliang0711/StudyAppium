import time
from appium import  webdriver
from selenium.webdriver.support.wait import WebDriverWait
#配置基本信息
desired_caps = dict()
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6'
desired_caps['deviceName'] = '6TV44HNV5HAYVWZ9'
#包名/界面名
desired_caps['appPackage'] = 'com.jkc.mitube'
desired_caps['appActivity'] = 'com.mitac.mitube.SplashActivity'
# desired_caps['appPackage'] = 'com.android.contacts'
# desired_caps['appActivity'] = '.DialtactsContactsEntryActivity'
desired_caps['noReset'] = 'True'  #不清空缓存数据
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True


#连接appium服务器
dirver = webdriver.Remote('http://localhost:4723/wd/hub' , desired_caps)

time.sleep(3)

search_button = WebDriverWait(dirver, 10).until(
            lambda x: x.find_element_by_id("com.jkc.mitube:id/buttonLeftOnlyImage"))
time.sleep(1)  # 不等待有时候点了没反应
search_button.click()
titles = dirver.find_elements_by_xpath("//*[contains(@text,'設定')]")
# ss = dirver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup[2]/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView")
# ss = dirver.find_element_by_xpath("//*[@text='ライセンス表示']")
print(len(titles))
for title in titles:
    print(title.text)

# dirver.find_element_by_xpath("//*[@text='群组']").click()
#
# dirver.find_element_by_class_name("android.widget.Button").click()
#
# dirver.find_element_by_id('com.android.contacts:id/edit_group_name').send_keys("来了")


time.sleep(3)
#通过id 定位放大镜按钮，点击
'''
这两种写法等价
search_button = dirver.find_element_by_id('****')
search_button.click()

dirver.find_element_by_id('****').click()
'''
#通过class 定位放大镜按钮，输入hello
'''
dirver.find_element_by_class_name("****").send_keys("hello")
'''

#通过Xpath 定位返回按钮
# dirver.find_element_by_xpath("****").click()



dirver.quit()

