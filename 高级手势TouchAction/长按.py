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
除了按坐标，也能按元素
long_press(el=None, x=None, y=None, duration=1000)
long_press自带松手
长按<==>按下.等待.抬手
'''
TouchAction(dirver).long_press(x=300 ,y=560,duration=2000).perform()
#TouchAction(dirver).press(x=300 ,y=560).wait(2000).release().perform()
time.sleep(2)
TouchAction(dirver).tap(x=300 ,y=560).perform()






time.sleep(3)
dirver.quit()
