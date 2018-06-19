from selenium.common.exceptions import NoSuchElementException, TimeoutException # use selenium execptions
from Page import Page
from MainUserPage import MainUserPage
from Locators import LoginPageLocators
from PageElement import PageElement

LOGIN_ADD_POST = "/login/index.php"


# present the loging page in the web
class LoginPage(Page):
    def __init__(self, driver, url):
        super(LoginPage, self).__init__(driver, url)

    def set_user(self, user):
        self.user_txt.clear()
        PageElement.__set__(self.driver, user, *LoginPageLocators.USERTXT)

    def set_password(self, password):
        self.pass_txt.clear()
        PageElement.__set__(self.driver, password, *LoginPageLocators.PASSTXT)

    def click_enter(self):
        self.entr_btn.click()
        return MainUserPage(self.driver, self.driver.current_url)

    def is_enter_clicked(self):
        if LOGIN_ADD_POST in self.driver.current_url:
            return True
        else:
            try:
                PageElement.__get__(self.driver,*LoginPageLocators.ERRICN)
            except NoSuchElementException:
                return "/login/index.php" not in self.driver.current_url
            except TimeoutException:
                return "/login/index.php" not in self.driver.current_url
            return True

    def is_loaded(self):
        try:
            self.user_lbl = PageElement.__get__(self.driver,*LoginPageLocators.USERLBL)
            self.pass_lbl = PageElement.__get__(self.driver,*LoginPageLocators.PASSLBL)
            self.entr_btn = PageElement.__get__(self.driver, *LoginPageLocators.ENTRBTN)
            self.user_txt = PageElement.__get__(self.driver,*LoginPageLocators.USERTXT)
            self.pass_txt = PageElement.__get__(self.driver,*LoginPageLocators.PASSTXT)
        except NoSuchElementException:
            print "coudnt find element"
            return False
        except TimeoutException:
            print "element couldent load"
            return False
        return True