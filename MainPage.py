from selenium.common.exceptions import NoSuchElementException, TimeoutException # use selenium execptions
from Page import Page # inheritance page class
from Locators import MainPageLocators
from PageElement import PageElement
from LoginPage import LoginPage

LOGIN_PAGE_POST = "/login/index.php"


# present the main page in the web
class MainPage(Page):
    def __init__(self, driver, url):
        super(MainPage, self).__init__(driver, url)

    def click_updates_button(self):
        update_button = PageElement.__get__(self.driver,*MainPageLocators.UPDT_TB)
        update_button.click()

    def click_login(self):
        self.login_btn.click()
        return LoginPage(self.driver, self.driver.current_url)

    def click_eng_lng_btn(self):
        self.lng_btn.click()
        eng_btn = PageElement.__get__(self.driver,*MainPageLocators.ENG_BTN)
        eng_btn.click()

    def is_eng_loaded(self):
        return self.driver.current_url == 'https://moodlearn.ariel.ac.il/?lang=en'

    def is_login_clicked(self):
        return LOGIN_PAGE_POST in self.driver.current_url

    def is_updates_button_clicked(self):
        try:
            PageElement.__get__(self.driver,*MainPageLocators.TAB4)
        except NoSuchElementException:
            print "page elements have not been loaded"
            return False
        except TimeoutException:
            print "element couldent load"
            return False
        return True

    def is_loaded(self):
        try:
            self.logo = PageElement.__get__(self.driver,*MainPageLocators.LOGO_CSS)
            self.login_btn = PageElement.__get__(self.driver,*MainPageLocators.LOGINBTN)
            self.pageup_btn = PageElement.__get__(self.driver,*MainPageLocators.PGUPBTN)
            self.lng_btn = PageElement.__get__(self.driver,*MainPageLocators.LANG_BTN)
        except NoSuchElementException:
            print "page elements have not been loaded"
            return False
        except TimeoutException:
            print "element couldent load"
            return False
        return True