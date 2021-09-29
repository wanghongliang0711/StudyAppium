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
desired_caps['noReset'] = True  #不清空缓存数据
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True


#连接appium服务器
dirver = webdriver.Remote('http://localhost:4723/wd/hub' , desired_caps)

time.sleep(3)

qunzu_button = dirver.find_element_by_xpath("//*[@text='群组']")

#获取元素的属性值
print(qunzu_button.get_attribute("text") )
print(qunzu_button.get_attribute("enabled") )

#获取content-desc 或 text  #####name，如果有content-desc用content-desc，else用text
print(qunzu_button.get_attribute("name") )
#获取resource-id
print(qunzu_button.get_attribute("resourceId") )#
#获取class
print(qunzu_button.get_attribute("className") )



time.sleep(2)
dirver.quit()