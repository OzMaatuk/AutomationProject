from selenium.common.exceptions import NoSuchElementException, TimeoutException # use selenium execptions
from Page import Page
from Locators import CourseLocator
from PageElement import PageElement


# present the course page in the web
class CoursePage(Page):
    def __init__(self, driver, url):
        super(CoursePage, self).__init__(driver, url)

    # is this course page got an edit course button
    def is_editable(self):
        try:
            edit_course_btn = PageElement.__get__(self.driver,*CourseLocator.EDT_CRS_BTN)
        except NoSuchElementException:
            print "coudnt find element"
            return False
        except TimeoutException:
            print "element couldent load"
            return False
        return True

    def is_loaded(self):
        try:
            self.this_course_btn = PageElement.__get__(self.driver,*CourseLocator.THS_CRS_BTN)
        except NoSuchElementException:
            print "coudnt find element"
            return False
        except TimeoutException:
            print "element couldent load"
            return False
        return 'course' in self.driver.current_url