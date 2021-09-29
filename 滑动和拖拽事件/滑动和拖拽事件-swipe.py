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
swipe滑动事件  从一个坐标位置滑动到另一个坐标位置，只能是两个点之间的滑动
dirver.swipe(start_x, start_y, end_x, end_y, duration=None)
start_x  起始X轴坐标   start_y  起始Y轴坐标
end_x    终点X轴坐标   end_y    终点Y轴坐标
duration 持续时间  单位：ms
距离相同，持续时间越长，惯性越小
'''
#有一定的误差，每次结果不太一样 ，，持续时间不同，结果不同
dirver.swipe(100,1200,100,100)#滑动距离越长，展示效果越靠后





time.sleep(2)
dirver.quit()