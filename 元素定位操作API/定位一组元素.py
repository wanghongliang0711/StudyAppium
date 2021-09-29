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
desired_caps['noReset'] = 'True'  #不清空缓存数据
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True


#连接appium服务器
dirver = webdriver.Remote('http://localhost:4723/wd/hub' , desired_caps)

time.sleep(2)

#**********一组元素的获取
#  通过ID获取
# titles = dirver.find_elements_by_id("com.android.contacts:id/cliv_name_textview")
# print(titles)#[<appium.webdriver.webelement.WebElement (session="bb447b55-8486-40c6-bb5e-23a88cc926dc", element="1")>, <appium.webdriver.webelement.WebElement (session="bb447b55-8486-40c6-bb5e-23a88cc926dc", element="2")>, <appium.webdriver.webelement.WebElement (session="bb447b55-8486-40c6-bb5e-23a88cc926dc", element="3")>, <appium.webdriver.webelement.WebElement (session="bb447b55-8486-40c6-bb5e-23a88cc926dc", element="4")>, <appium.webdriver.webelement.WebElement (session="bb447b55-8486-40c6-bb5e-23a88cc926dc", element="5")>, <appium.webdriver.webelement.WebElement (session="bb447b55-8486-40c6-bb5e-23a88cc926dc", element="6")>, <appium.webdriver.webelement.WebElement (session="bb447b55-8486-40c6-bb5e-23a88cc926dc", element="7")>, <appium.webdriver.webelement.WebElement (session="bb447b55-8486-40c6-bb5e-23a88cc926dc", element="8")>, <appium.webdriver.webelement.WebElement (session="bb447b55-8486-40c6-bb5e-23a88cc926dc", element="9")>, <appium.webdriver.webelement.WebElement (session="bb447b55-8486-40c6-bb5e-23a88cc926dc", element="10")>]
# print(len(titles)) #10
# for title in titles:
#     print(title.text)
# titles[1].click()#点击第二个

#  通过class_name获取
# titles = dirver.find_elements_by_class_name("android.widget.TextView")
# print(len(titles))
# for title in titles:
#     print(title.text)
# titles[19].click()
# time.sleep(2)

#通过Xpath获取
titles = dirver.find_elements_by_xpath("//*[contains(@text,'丁')]")
print(len(titles))
for title in titles:
    print(title.text)
titles[1].click()
time.sleep(2)
'''
-----------定位一组元素
通过id形式，获取所有id为"****"的元素，并且打印文字内容
dirver.find_elements_by_id

通过class_name形式，获取所有class为"****"的元素，并且打印文字内容
dirver.find_elements_by_class_name

通过Xpath形式，获取所有包含"****"的元素，并且打印文字内容
dirver.find_elements_by_xpath


dirver.find_element_by_xxxx如果传入的条件找不到会报一个错

dirver.find_elements_by_xxxx如果传入的条件找不到会等到空列表，不会报错

'''







dirver.quit()


