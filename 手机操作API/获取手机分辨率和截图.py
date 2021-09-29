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

#获取当前设备的分辨率
print(dirver.get_window_size())#{'width': 720, 'height': 1436}
print(dirver.get_window_size()['width'])# int类型
print(dirver.get_window_size()['height'])# int类型

'''手机截图
有些自动化的操作可能没有反应，但是不报错，这时可以截图保留
'''
# dirver.get_screenshot_as_file("screen.png")
dirver.get_screenshot_as_file("E:/code/PycharmPy36Workspaces/Appium/手机操作API/截图/screen.png")


time.sleep(8)
dirver.quit()