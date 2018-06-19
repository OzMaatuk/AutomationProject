# base class for all pages in the web
# followed the pagw object DP
# giving a good and cont structe
class Page(object):
    def __init__(self, driver, url):
        self.url = url
        self.driver = driver

    def open(self):
        print self.url
        self.driver.get(self.url)

    def get_url(self):
        return self.driver.current_url

    def get_driver(self):
        return self.driver

    # is loaded function is importent
    # all the duty of setting a basic page tools and element is executed here
    # and if the basic stuff are ready
    # function return the answare of a loaded and ready to use page
    def is_loaded(self):
        pass
