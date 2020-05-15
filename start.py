import unittest
import time
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from driver import Driver


class AppAutomation(unittest.TestCase):
    def setUp(self):
        self.driver = Driver()

    def test_calculator_launches(self):
        WebDriverWait(self.driver.instance, 30).until(
            EC.element_to_be_clickable((
                MobileBy.XPATH, "//android.widget.Button[@content-desc=\"ACESSAR\"]/android.widget.TextView")))
        self.driver.instance.find_element_by_xpath(
            '//android.widget.Button[@content-desc="ACESSAR"]/android.widget.TextView').click()
        WebDriverWait(self.driver.instance, 30).until(
            EC.element_to_be_clickable((
                MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.widget.ScrollView/android.view.View/android.view.View[1]')))
        self.driver.instance.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.widget.ScrollView/android.view.View/android.view.View[1]').click()
        WebDriverWait(self.driver.instance, 30).until(
            EC.element_to_be_clickable((
                MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[3]')))
        self.driver.instance.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[3]').click()

        self.driver.instance.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.widget.ScrollView/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View').send_keys('JD618768')
        time.sleep(1)
        self.driver.instance.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.widget.ScrollView/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View').send_keys('dupa8717')
        time.sleep(1)

        self.driver.instance.find_element_by_xpath('//android.widget.Button[@content-desc="ENTRAR"]').click()

        WebDriverWait(self.driver.instance, 30).until(
            EC.element_to_be_clickable((
                MobileBy.XPATH,
                '//android.widget.TextView[@content-desc="Senha de 8 dígitos"]')))

        agencia = self.driver.instance.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[3]/android.view.View/android.view.View[3]/android.widget.ScrollView/android.view.View/android.view.View[1]/android.widget.TextView[1]').text
        conta = self.driver.instance.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[3]/android.view.View/android.view.View[3]/android.widget.ScrollView/android.view.View/android.view.View[1]/android.widget.TextView[2]').text
        print('agencia: %s' % agencia)
        print('conta: %s' % conta)
        time.sleep(1)

        self.driver.instance.find_element_by_xpath('//android.widget.TextView[@content-desc="Senha de 8 dígitos"]').send_keys('38986090')
        time.sleep(1)

        self.driver.instance.find_element_by_xpath('(//android.widget.Button[@content-desc="ENTRAR"])[2]').click()
        time.sleep(1)

        WebDriverWait(self.driver.instance, 30).until(
            EC.element_to_be_clickable((
                MobileBy.XPATH,
                '//android.widget.ImageView[@content-desc="Fechar"]')))

        title = self.driver.instance.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout[2]/android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.LinearLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View').text

        subtitle = self.driver.instance.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout[2]/android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[4]/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View').text
        description = self.driver.instance.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout[2]/android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[5]/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View').text

        print('title: %s' % title)
        print('subtitle: %s' % subtitle)
        print('description: %s' % description)

        time.sleep(10)

    def tearDown(self):
        self.driver.instance.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AppAutomation)
    unittest.TextTestRunner(verbosity=2).run(suite)
