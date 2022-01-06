import requests
import json
import os

# Fetch all quizzes
url = "https://hulms.instructure.com/api/v1/courses/1923/quizzes"
headers ={"authorization":"Bearer ygCxdvuMbLXDtgiCpEdqLrRRZ02kASevZHl9vddtJPtBDS7MGs8WvT5wlPcapUcB"}
r =requests.get(url, headers=headers)
print(r.status_code)
print(r.text)
print(r.json)

# Fetch a particular quiz
quizid = "4946"
url = "https://hulms.instructure.com/api/v1/courses/1923/quizzes/"+quizid
headers ={"authorization":"Bearer ygCxdvuMbLXDtgiCpEdqLrRRZ02kASevZHl9vddtJPtBDS7MGs8WvT5wlPcapUcB"}
r =requests.get(url, headers=headers)
print(r.status_code)
print(r.text)
print(r.json)

# Edit a particular quiz
quizid = "4946"
url = "https://hulms.instructure.com/api/v1/courses/1923/quizzes/"+quizid
headers ={"authorization":"Bearer ygCxdvuMbLXDtgiCpEdqLrRRZ02kASevZHl9vddtJPtBDS7MGs8WvT5wlPcapUcB"}
r =requests.put(url, headers=headers, data=json.dumps({''}))
print(r.status_code)
print(r.text)
print(r.json)