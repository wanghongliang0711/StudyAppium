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
driver = webdriver.Remote('http://localhost:4723/wd/hub' , desired_caps)


#设置好了，程序接着跑， time.sleep是程序不接着跑
driver.implicitly_wait(10)#单位是秒

print("------准备找‘所在地’关键字进行点击")
driver.find_element_by_xpath("//*[@text='所在地']").click()
print("------点完了")


'''
针对所有定位元素的超时时间设置为同一个值的时候
超出时长抛出异常NoSuchElementException

在获取driver对象后调用implicitly_wait方法


'''

time.sleep(2)
driver.quit()





