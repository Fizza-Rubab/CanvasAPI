from canvasapi import *
from datetime import datetime

# Setting the parameters
API_URL ="https://hulms.instructure.com"
API_KEY = "17361~ygCxdvuMbLXDtgiCpEdqLrRRZ02kASevZHl9vddtJPtBDS7MGs8WvT5wlPcapUcB"
canvas = Canvas(API_URL, API_KEY)

#  Get the accounnt by providing the ID
acc = canvas.get_account(2)

# It does not give an authority to create a course so I can't verify
print(acc)

# Create the course with the provided details (Course will be unpublished)
l = acc.create_course(course={"name":"Fizza's Course", "course_code":"FR101"})
print(l)
lst = acc.get_courses()
print(lst)