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

#获取文本内容
# titles = dirver.find_elements_by_class_name("android.widget.TextView")
# for title in titles:
#     print(title.text)



#获取元素的位置和大小
qunzu_button = dirver.find_element_by_xpath("//*[@text='群组']")
print(qunzu_button.location) #{'x': 421, 'y': 1401}
print(qunzu_button.location['x']) #int 类型
print(qunzu_button.location['y'])

print(qunzu_button.size) #{'height': 35, 'width': 58}
print(qunzu_button.size['height']) #int 类型
print(qunzu_button.size['width'])



time.sleep(2)
dirver.quit()