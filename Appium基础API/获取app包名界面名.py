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
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'
desired_caps['noReset'] = 'True'

#连接appium服务器
dirver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

#输出当前程序的包名
print(dirver.current_package)
#输出当前程序的界面名
print(dirver.current_activity)
print('time.sleep(5)')
time.sleep(5)

#启动设置程序
#不知道为什么，有的app不能运行，报错，有的能正常运行
print('------开启日历--------')
dirver.start_activity("com.bbk.calendar",".MainActivity")
print(dirver.current_package)
print(dirver.current_activity)
print('time.sleep(3)')
time.sleep(3)

#dirver退出
dirver.quit()

