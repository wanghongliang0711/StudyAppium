import time
from appium import  webdriver
from appium.webdriver.common.touch_action import TouchAction
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
'''
模拟手指一直按下，模拟手指抬起。可以用来组合成轻敲或长按的操作
除了按坐标，也能按元素

'''
#---按下和抬起
#两次按下不会进去，这是正常的
# TouchAction(dirver).press(x=270 ,y=1400).perform()
# time.sleep(2)
# TouchAction(dirver).press(x=270 ,y=1400).perform()


# TouchAction(dirver).press(x=270 ,y=1400).perform()
# time.sleep(2)
# TouchAction(dirver).press(x=450 ,y=1400).release().perform()

#----等待操作 单位ms
TouchAction(dirver).press(x=300 ,y=560).wait(2000).release().perform()
time.sleep(2)
TouchAction(dirver).tap(x=300 ,y=560).perform()


time.sleep(3)
dirver.quit()

