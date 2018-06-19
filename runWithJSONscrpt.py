import subprocess
import sys
import json

if __name__ == '__main__':
    json_file_name = sys.argv.pop()
    with open(json_file_name) as f:
        data = json.load(f)
    for item in data:
        user = data.get(item).get('user')
        password = data.get(item).get('password')
        line = 'python MoodleTest.py https://moodlearn.ariel.ac.il/ ' + user + ' ' + password
        # print 'python MoodleTest.py https://moodlearn.ariel.ac.il/ ' + user + ' ' + password
        subprocess.Popen(line).wait()