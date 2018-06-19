def test_cases(number):
    return testCases[number]

testCases = [
    # [tag, name, conviction ,description]
    ['Test0', 'valid login log out','use valide username and password for loging as student to the web', 'open browser with ariel moodlearn web address, click on login button and move forword to login page. in loging page fill username and password filled with proper args and click enter. if student main page loaded, DONE. click on logout button and check were out (check for missing elements in page)'],
    ['Test1', 'wrong username login','use unvalide username for loging as student to the web', 'open browser with ariel moodlearn web address, click on login button and move forword to login page. in loging page fill wrong username and some password in proper filleds and click enter. if we are still in login page, DONE'],
    ['Test2', 'wrong password login','use valide username and wrong password for loging as student to the web', 'open browser with ariel moodlearn web address, click on login button and move forword to login page. in loging page fill valide username and wrong password in proper filleds and click enter. if we are still in login page, DONE'],
    ['Test3', 'change to english', 'check that change to english button works', 'open browser with ariel moodlearn web address, click on language button and select english. if page context changes to english, DONE'],
    ['Test4', 'practical lecture cant edit course', 'check that when login as practical lecture, uneditable courses cant be edited', '...go there click in the right course and check the edit button not loaded'],
    ['Test5', 'practical lecture can edit course', 'check that when login as practical lecture, editable courses can be edited', '...go there click in the right course and check the edit button is loaded'],
    ['Test6', 'change main tab', 'change the main page inner tab to the other option', 'ckick on the tab button and check frame has changed']
]