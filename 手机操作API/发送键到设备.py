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
发送键到设备
参数
keycode  发送给设备的关键代码
press_keycode( keycode, metastate=None, flags=None):
百度搜索关键字“android keycode”
KEYCODE_CALL 拨号键5 
KEYCODE_ENDCALL 挂机键6 
KEYCODE_HOME 按键Home3 
KEYCODE_MENU 菜单键82 
KEYCODE_BACK 返回键4 
KEYCODE_SEARCH 搜索键84 
KEYCODE_CAMERA 拍照键27 
KEYCODE_FOCUS 拍照对焦键80 
KEYCODE_POWER 电源键26 
KEYCODE_NOTIFICATION 通知键83 
KEYCODE_MUTE 话筒静音键91 
KEYCODE_VOLUME_MUTE 扬声器静音键164 
KEYCODE_VOLUME_UP 音量增加键24 
KEYCODE_VOLUME_DOWN 音量减小键25
'''
dirver.press_keycode(24)
time.sleep(1)
dirver.press_keycode(24)
time.sleep(1)

dirver.press_keycode(24)
time.sleep(1)
dirver.press_keycode(4)
time.sleep(1)
dirver.press_keycode(25)
time.sleep(1)
dirver.press_keycode(25)



time.sleep(8)
dirver.quit()