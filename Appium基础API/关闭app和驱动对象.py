import os
import time

from appium import webdriver


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

# time.sleep(3)
# #dirver相当于一个管家close_app()只是关闭app，没有关闭管家；quit()相当于关闭管家
# #关闭当前操作的app，不会关闭驱动对象
# dirver.close_app()
# #关闭驱动对象，同时关闭所有关联的app
# # dirver.quit()
# time.sleep(3)
#
# #启动close_app()的app
# dirver.launch_app()

#background_app #将app至于后台XX秒
#有了它，就可以不用先close_app()，再launch_app()去唤起app了，一个API就搞定
time.sleep(3)
dirver.background_app(3)
time.sleep(3)
os.system("adb shell am start -n com.bbk.calendar/.MainActivity")
print(dirver.current_package)
print(dirver.current_activity)
'''

#输出当前程序的包名
print(dirver.current_package)
#输出当前程序的界面名
print(dirver.current_activity)
print('time.sleep(5)')
time.sleep(5)

#com.android.settings/.SubSettings 设置WiFi页面的包名和界面名
#启动设置程序
#不知道为什么，有的app不能运行，报错，有的能正常运行
dirver.start_activity("com.android.calendar",".AllInOneActivity")
#输出当前程序的包名
print(dirver.current_package)
#输出当前程序的界面名
print(dirver.current_activity)
print('time.sleep(3)')
time.sleep(3)



#dirver退出
dirver.quit()

'''
















