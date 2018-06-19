# here ive placed information for all xpath/css prosess that included in the project
# every locating argumant or method that have been needed
# speciely for find element function
# there is a class for every page
from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGO = (By.XPATH, "//a[@class='brand'][contains(text(),'MoodLearn')]")
    LOGINBTN = (By.XPATH, "//a[@class='loginurl']")
    PGUPBTN = (By.XPATH, "//span[@class='fa fa-angle-up ']")
    LOGO_CSS = (By.CSS_SELECTOR, "a[class*='btn btn-navbar']+a[class*='brand'][href*='//moodlearn.ariel.ac.il']")
    LANG_BTN = (By.CSS_SELECTOR, "div[class='custom_menu'] ul[class*='nav'] li[class*='dropdown langmenu'] a[class*='dropdown-toggle']")
    ENG_BTN = (By.CSS_SELECTOR, "a[href='https://moodlearn.ariel.ac.il/?lang=en'")
    UPDT_TB = (By.CSS_SELECTOR, "a[href='#tab4']")
    TAB4 = (By.CSS_SELECTOR, "div[id='tab4']")

class LoginPageLocators:
    USERTXT = (By.CSS_SELECTOR, "input[id='username'][type='text']")
    PASSTXT = (By.CSS_SELECTOR, "input[id='password'][type='password']")
    USERLBL = (By.CSS_SELECTOR, "label[for='username']")
    PASSLBL = (By.CSS_SELECTOR, "label[for='password']")
    ENTRBTN = (By.CSS_SELECTOR, "input[id='loginbtn'][type='submit']")
    ERRICN = (By.CSS_SELECTOR, "span[class='error'] img[class*='icon-pre'")

class MainUserLocator:
    MYCOURSE_TTL = (By.CSS_SELECTOR, "div[id='frontpage-course-list'] h2")
    MYCOURSE_BTN = (By.CSS_SELECTOR, "a[title='My latest courses']")
    USER_PROF_DD = (By.CSS_SELECTOR, "ul[class*='nav'] li[class*='dropdown'] a[class*='dropdown-toggle']")
    LOGOUT_BTN = (By.CSS_SELECTOR, "li a[href*='/login/logout.php?']")
    EN_CRS_BTN = (By.CSS_SELECTOR, "h3[class='coursename'] a[href*='course/view.php?id=62186']")
    UNA_CRS_BTN = (By.CSS_SELECTOR,"h3[class='coursename'] a[href*='course/view.php?id=44848']")
    @staticmethod
    def _getCourseLocator(cnum):
        return (By.CSS_SELECTOR, "h3[class='coursename'] a[href*='course/view.php?id="+cnum+"']")

class CourseLocator:
    THS_CRS_BTN = (By.CSS_SELECTOR, "ul.nav li.dropdown a.dropdown-toggle span.fa.fa-book")
    EDT_CRS_BTN = (By.CSS_SELECTOR, "a.btn.btn-success span.fa-fw.fa.fa-edit")
