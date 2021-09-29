import time
from appium import  webdriver
from selenium.webdriver.support.wait import WebDriverWait


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


print("------准备找‘所在地’关键字进行点击")
# wait = WebDriverWait(driver , 25 , 5)#共找25秒，每5秒找一次 ，默认每0.5秒找一次
# search_button = wait.until(lambda x: x.find_element_by_xpath("//*[@text='所在地']"))
# search_button.click()

search_button = WebDriverWait(driver , 5 , 1).until(lambda x: x.find_element_by_xpath("//*[@text='所在地']"))
search_button.click()

#WebDriverWait(driver , 5 , 1).until(lambda x: x.find_element_by_xpath("//*[@text='所在地']")).click()

print("------点完了")



'''
针对所有定位元素的超时时间设置为不同的值的时候


超出时长抛出异常TimeoutException
'''

time.sleep(2)
driver.quit()
