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
'''
scroll滑动事件  有惯性
从一个元素滑动到另一个元素，直到页面自动停止
dirver.scroll(origin_el, destination_el)
origin_el  滑动开始的元素     destination_el 滑动结束的元素
'''

button1 = dirver.find_element_by_xpath("//*[@text='13']")
button2 = dirver.find_element_by_xpath("//*[@text='丁光鹏']")
# dirver.scroll(button2,button1)
'''
drag_and_drop滑动事件    无惯性
从一个元素滑动到另一个元素，第二个元素替代第一个元素原本屏幕上的位置
dirver.drag_and_drop(origin_el, destination_el)
origin_el  滑动开始的元素     destination_el 滑动结束的元素
'''
dirver.drag_and_drop(button2,button1)


time.sleep(10)
dirver.quit()