# using python 7.2
# selenium
# firefox 46.0
from selenium import webdriver # for using selenuim webdriver
import sys # for getting args
import unittest # for implementing as unittest
import json # for saving users in external file (and enable to script on it)
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities # for working with firefox 46.0
from MainPage import MainPage

TIME_OUT = 10


# main test class as unittest, including all tests scenarios
class MoodleTest(unittest.TestCase):
    url = ""
    user_name = ""
    password = ""
    ver = ""
    users_json = json.load(open('usersfile.json'))

    # setting up testing env and right browser
    def setUp(self):
        if self.ver == "":
            # need to false marionette for working with firefox 46
            # adding firefox path manually cuz of custom installation
            cap = DesiredCapabilities().FIREFOX
            cap["marionette"] = False
            self.driver = webdriver.Firefox(capabilities=cap, executable_path="E:\Projects\Python\geckodriver.exe")
        elif self.ver == "--new":
            self.driver = webdriver.Firefox()
        elif self.ver == "--chrome":
            self.driver = webdriver.Chrome()
        else:
            print "wrong browser flag"
            self.assertTrue(False)
        self.driver.set_page_load_timeout(TIME_OUT)

    # help function for shurtcut logging procces when needed
    def getLoggedMenuPage(self, un, pss):
        main_page = MainPage(self.driver, self.url)
        main_page.open()
        main_page.is_loaded()
        login_page = main_page.click_login()
        login_page.is_loaded()
        login_page.set_user(un)
        login_page.set_password(pss)
        main_user_page = login_page.click_enter()
        return main_user_page

    # test0
    @unittest.skip("demonstrating skipping")
    def test_valid_login_logout(self):
        main_page = MainPage(self.driver, self.url)
        main_page.open()
        self.assertTrue(main_page.is_loaded())
        login_page = main_page.click_login()
        self.assertTrue(main_page.is_login_clicked())
        self.assertTrue(login_page.is_loaded())
        login_page.set_user(self.user_name)
        login_page.set_password(self.password)
        main_user_page = login_page.click_enter()
        self.assertTrue(login_page.is_enter_clicked())
        self.assertTrue(main_user_page.is_loaded())
        main_user_page.click_logout()
        self.assertTrue(main_user_page.is_logged_out())

    # test1
    @unittest.skip("demonstrating skipping")
    def test_wrong_username_login(self):
        main_page = MainPage(self.driver, self.url)
        main_page.open()
        self.assertTrue(main_page.is_loaded())
        login_page = main_page.click_login()
        self.assertTrue(main_page.is_login_clicked())
        self.assertTrue(login_page.is_loaded())
        # login_page.set_user(self.users_json['BadUser']['user'])
        # login_page.set_password(self.users_json['BadUser']['password'])
        login_page.set_user(self.user_name)
        login_page.set_password(self.password)
        main_user_page = login_page.click_enter()
        self.assertTrue(login_page.is_enter_clicked())
        self.assertFalse(main_user_page.is_loaded())

    # test2
    @unittest.skip("demonstrating skipping")
    def test_wrong_password_login(self):
        main_page = MainPage(self.driver, self.url)
        main_page.open()
        self.assertTrue(main_page.is_loaded())
        login_page = main_page.click_login()
        self.assertTrue(main_page.is_login_clicked())
        self.assertTrue(login_page.is_loaded())
        # login_page.set_user(self.users_json['BadStudentPass']['user'])
        # login_page.set_password(self.users_json['BadStudentPass']['password'])
        login_page.set_user(self.user_name)
        login_page.set_password(self.password)
        main_user_page = login_page.click_enter()
        self.assertTrue(login_page.is_enter_clicked())
        self.assertFalse(main_user_page.is_loaded())

    # test3
    @unittest.skip("demonstrating skipping")
    def test_change_to_english(self):
        main_page = MainPage(self.driver, self.url)
        main_page.open()
        self.assertTrue(main_page.is_loaded())
        main_page.click_eng_lng_btn()
        self.assertTrue(main_page.is_eng_loaded())

    # test4
    @unittest.skip("demonstrating skipping")
    def test_pl_cant_edit_course(self):
        # un = self.users_json['PracticalLecture']['user']
        # pss = self.users_json['PracticalLecture']['password']
        # main_user_page = self.getLoggedMenuPage(un,pss)
        main_user_page = self.getLoggedMenuPage(self.user_name, self.password)
        course_page = main_user_page.click_course(self.users_json['PracticalLecture']['editUnable'])
        self.assertTrue(course_page.is_loaded())
        self.assertFalse(course_page.is_editable())

    # test5
    @unittest.skip("demonstrating skipping")
    def test_pl_can_edit_course(self):
        # un = self.users_json['PracticalLecture']['user']
        # pss = self.users_json['PracticalLecture']['password']
        # main_user_page = self.getLoggedMenuPage(un,pss)
        main_user_page = self.getLoggedMenuPage(self.user_name, self.password)
        # here i got a course number from the json, the idea is to attach to every user a course number
        # save everything in json
        # and import information from there
        # you can see the technic in a commented line over the code
        course_page = main_user_page.click_course(self.users_json['PracticalLecture']['editEnable'])
        self.assertTrue(course_page.is_loaded())
        self.assertTrue(course_page.is_editable())

    # test6
    #@unittest.skip("demonstrating skipping")
    def test_change_main_tab(self):
        main_page = MainPage(self.driver, self.url)
        main_page.open()
        self.assertTrue(main_page.is_loaded())
        main_page.click_updates_button()
        self.assertTrue(main_page.is_updates_button_clicked())

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        exit("Too less arguments calling script")
    if len(sys.argv) == 5:
        MoodleTest.ver = sys.argv.pop()
    MoodleTest.password = sys.argv.pop()
    MoodleTest.user_name = sys.argv.pop()
    MoodleTest.url = sys.argv.pop()
    suite = unittest.TestLoader().loadTestsFromTestCase(MoodleTest)
    unittest.TextTestRunner(verbosity=2).run(suite)