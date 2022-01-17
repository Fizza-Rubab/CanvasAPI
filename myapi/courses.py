from xml.etree.ElementInclude import include
import requests
import json

# Get Courses
# url = "https://hulms.instructure.com/api/v1/courses"
# headers ={"Authorization":"Bearer ygCxdvuMbLXDtgiCpEdqLrRRZ02kASevZHl9vddtJPtBDS7MGs8WvT5wlPcapUcB"}
# r =requests.get(url, headers=headers)
# print(r.status_code)
# print(r.text)
# print(r.json)

# Get a particular Course
url2 = "https://hulms.instructure.com/api/v1/courses/1921"
headers ={"Authorization":"Bearer ygCxdvuMbLXDtgiCpEdqLrRRZ02kASevZHl9vddtJPtBDS7MGs8WvT5wlPcapUcB"}
r =requests.get(url2, headers=headers, params={"include":"syllabus_body"})
print(json.loads(r.text)["syllabus_body"])



# Update a particular Course (Not working for some reason)
# url4 = "https://hulms.instructure.com/api/v1/courses/1923?"
# headers ={"Authorization":"Bearer ygCxdvuMbLXDtgiCpEdqLrRRZ02kASevZHl9vddtJPtBDS7MGs8WvT5wlPcapUcB"}
# r =requests.put(url4, headers=headers, params=json.dumps({
#   "course" : {
#     "name" : "Fizza Canvas 101"
#   }
# }))
# print(r.status_code)
# print(r.text)
# print(r.json)


# Please Dont test this
# Delete/Conculde a course
# url3 = "https://hulms.instructure.com/api/v1/courses/1956?event=conclude"
# headers ={"Authorization":"Bearer ygCxdvuMbLXDtgiCpEdqLrRRZ02kASevZHl9vddtJPtBDS7MGs8WvT5wlPcapUcB"}
# r =requests.delete(url3, headers=headers)
# print(r.status_code)
# print(r.text)
# print(r.json)



