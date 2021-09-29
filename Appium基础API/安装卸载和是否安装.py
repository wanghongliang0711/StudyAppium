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

print(r"D:\Study\appium\DRV_JKC\miTube-jkc-release_production_1.5.37.1.apk")
#如果DRV Link安装了就卸载，如果没安装，就安装
if dirver.is_app_installed('com.jkc.mitube'):
    dirver.remove_app('com.jkc.mitube')
else:
    dirver.install_app(r"D:\Study\appium\DRV_JKC\miTube-jkc-release_production_1.5.37.1.apk")

dirver.quit()







