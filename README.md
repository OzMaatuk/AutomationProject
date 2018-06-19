# AutomationProject
Automation Testing - Moodle Ariel

using Python2.7, Selenium 3.12 Client & WebDriver
task was tested with FireFox 46.0

 download & installing Python2.7
    https://www.python.org/downloads/release/python-2715/
    
 download & installing Pip
    https://www.makeuseof.com/tag/install-pip-for-python/
    
 download & installing Selenium3.12
    http://selenium-python.readthedocs.io/installation.html
    
 dont forget webdrivers for your chosen browser
    http://selenium-python.readthedocs.io/installation.html
    


## this project is an automated testunit for ariel university moodlearn webpage

for starting up use the following commandline and args

        python MoodleTest.py https://moodlearn.ariel.ac.il/ username password
    
for working with newer version of firefox run with --new

        python MoodleTest.py https://moodlearn.ariel.ac.il/ username password --new
    
for working with chrome run with --chrome

        python MoodleTest.py https://moodlearn.ariel.ac.il/ username password --chrome







###introducing tests scenarios in TestCases.py



## Background


the tests implemented as a unittest followed python unittest package,
where every test implement a simple scenario of actions over ariel moodlearn web pages.

enjoying unittest framework features
    https://docs.python.org/2/library/unittest.html
    
the project OOP structure builded following page object desing pattern,
when presenting every page in the web as c class thats include all the actions on thhat page,
testing stategy focus on the index (main) page of ariel moodlearn webpage,
its very powerful when using python object flexibility,
more users and password for the tests are writen in usersfile.json


more comments and explanations over the code.



## EXTRA - runWithJSONscrpt.py
for more efficient way,
i made a script that will run all testsuites over every user in the json file

run it like:
python runWithJSONscrpt.py usersfile.json
