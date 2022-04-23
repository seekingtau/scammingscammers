import requests
import random
import json
from threading import Thread

url = 'https://dehandsservices.com/welsc/2fb5d/umail.php'
firstNamesURL = 'https://raw.githubusercontent.com/dominictarr/random-name/master/first-names.json'
lastNamesURL = 'https://raw.githubusercontent.com/rossgoodwin/american-names/master/surnames.json'
passwordURL = 'https://raw.githubusercontent.com/seekingtau/scammingscammers/main/passlist.json'

firstNames = json.loads(requests.get(firstNamesURL).text)
lastNames = json.loads(requests.get(lastNamesURL).text)
passwords = json.loads(requests.get(passwordURL).text)

def genName():
    return random.choice(firstNames).lower() + random.choice(lastNames).lower()

def genPass():
    return random.choice(passwords) + random.choice('!@#$%^&*')
    
def submitInfo(id):
    for i in range(1000):
        name = genName()
        password = genPass()
    
        requests.post(url, allow_redirects = False, data = {
            'user': name,
            'pass': password,
            'save-username': 'true',
            'hdnuserid': '',
            'submit': 'Sign On'
        })
    
        print('Thread %s: Submitted username %s with password %s' % (id, name, password))
    
threads = []

for n in range(10):
    t = Thread(target = submitInfo, args = (n,))
    threads.append(t)
    t.start()
    
for t in threads:
    t.join()
