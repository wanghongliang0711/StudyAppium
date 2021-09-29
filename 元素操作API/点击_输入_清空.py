import time
from appium import  webdriver

#配置基本信息
desired_caps = dict()
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.1.0'
desired_caps['deviceName'] = '6TV44HNV5HAYVWZ9'
#包名/界面名
# desired_caps['appPackage'] = 'com.jkc.mitube'
# desired_caps['appActivity'] = 'com.mitac.mitube.SplashActivity'
desired_caps['appPackage'] = 'com.android.contacts'
desired_caps['appActivity'] = '.DialtactsContactsEntryActivity'
desired_caps['noReset'] = 'True'  #不清空缓存数据
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True


#连接appium服务器
dirver = webdriver.Remote('http://localhost:4723/wd/hub' , desired_caps)

time.sleep(3)

#点击
dirver.find_element_by_xpath("//*[@text='群组']").click()

dirver.find_element_by_class_name("android.widget.Button").click()
#输入
input_label = dirver.find_element_by_id('com.android.contacts:id/edit_group_name')
input_label.send_keys("来了")
print(input_label.text) #来了  获取输入的内容
time.sleep(2)
#清空
input_label.clear()

time.sleep(2)
input_label.send_keys("hello你好")







time.sleep(2)
dirver.quit()
