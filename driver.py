from appium import webdriver


class Driver:
    def __init__(self):

        desired_cap = {
            "platformName": "android",
            "deviceName": "127.0.0.1:5555",
            "platformVersion": "5.1.1",
            "noReset": False,
            "app": "D:\\br.apk"
        }
        self.instance = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)

