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

'''轻敲
模拟手指对元素或坐标的轻敲操作
参数：
    element: 元素
    x: x坐标
    y: y坐标
    count： 点击次数，默认是1
tap(element=None, x=None, y=None, count=1)

'''
#找到要点击的元素
phon = dirver.find_element_by_xpath("//*[@text='本人']")
# #1. 创建touchaction对象
# touch_action = TouchAction(dirver)
# #2. 调用想要执行的动作
# touch_action = touch_action.tap(phon)
# #3. 使用perform执行动作
# touch_action.perform()

#简化版  点击元素
# TouchAction(dirver).tap(phon).perform()

#简化版  点击坐标
TouchAction(dirver).tap(x=300 ,y=560 ).perform()











time.sleep(8)
dirver.quit()