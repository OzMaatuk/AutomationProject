from selenium.common.exceptions import NoSuchElementException, TimeoutException # use selenium execptions
from selenium.webdriver.common.action_chains import ActionChains # for scrolling to element
from Page import Page
from Locators import MainUserLocator
from PageElement import PageElement
from CoursePage import CoursePage


# present the user menu page in the web
class MainUserPage(Page):
    def __init__(self, driver, url):
        super(MainUserPage, self).__init__(driver, url)

    def click_logout(self):
        self.user_profile_dd.click()
        self.logout_btn = PageElement.__get__(self.driver, *MainUserLocator.LOGOUT_BTN)
        self.logout_btn.click()

    def is_logged_out(self):
        try:
            self.driver.find_element(*MainUserLocator.MYCOURSE_BTN)
        except NoSuchElementException:
            return True
        return False

    def click_course(self, cnum):
        course_btn = self.find_course_by_num(cnum)
        if course_btn:
            actions = ActionChains(self.driver)
            actions.move_to_element(course_btn).perform()
            course_btn.click()
            return CoursePage(self.driver, self.driver.current_url)
        return False

    def find_course_by_num(self, cnum):
        try:
            course_btn = self.driver.find_element(*MainUserLocator._getCourseLocator(cnum))
        except NoSuchElementException:
            print "coudnt find course"
            return False
        return course_btn

    def is_loaded(self):
        try:
            self.course_btn = PageElement.__get__(self.driver,*MainUserLocator.MYCOURSE_BTN)
            self.course_ttl = PageElement.__get__(self.driver,*MainUserLocator.MYCOURSE_TTL)
            self.user_profile_dd = PageElement.__get__(self.driver,*MainUserLocator.USER_PROF_DD)
        except NoSuchElementException:
            print "coudnt find element"
            return False
        except TimeoutException:
            print "element couldent load"
            return False
        return self.url in self.driver.current_url