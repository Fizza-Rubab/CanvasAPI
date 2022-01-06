import requests
import json

# Get Courses
url = "https://hulms.instructure.com/api/v1/courses"
headers ={"Authorization":"Bearer ygCxdvuMbLXDtgiCpEdqLrRRZ02kASevZHl9vddtJPtBDS7MGs8WvT5wlPcapUcB"}
r =requests.get(url, headers=headers)
print(r.status_code)
print(r.text)
print(r.json)

# Get a particular Course
url2 = "https://hulms.instructure.com/api/v1/courses/1956"
headers ={"Authorization":"Bearer ygCxdvuMbLXDtgiCpEdqLrRRZ02kASevZHl9vddtJPtBDS7MGs8WvT5wlPcapUcB"}
r =requests.get(url2, headers=headers)
print(r.status_code)
print(r.text)
print(r.json)

# Delete/Conculde a course
url3 = "https://hulms.instructure.com/api/v1/courses/1956"
headers ={"Authorization":"Bearer ygCxdvuMbLXDtgiCpEdqLrRRZ02kASevZHl9vddtJPtBDS7MGs8WvT5wlPcapUcB"}
r =requests.delete(url3, headers=headers, params=json.dumps({"event":"delete"}))
print(r.status_code)
print(r.text)
print(r.json)


