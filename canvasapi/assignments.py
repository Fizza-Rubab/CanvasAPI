
from canvasapi import *
from datetime import datetime

# Setting the parameters
API_URL ="https://hulms.instructure.com"
API_KEY = "17361~ygCxdvuMbLXDtgiCpEdqLrRRZ02kASevZHl9vddtJPtBDS7MGs8WvT5wlPcapUcB"
canvas = Canvas(API_URL, API_KEY)

courseID = 1923
course = canvas.get_course(courseID)
print(course)

# Fetch all the assignments in a paginated lst
assignments = course.get_assignments()
for assignment in assignments:
    print(assignment)

# Fetch all ungraded assignments
assignments = course.get_assignments(bucket='ungraded')
for assignment in assignments:
    print(assignment)

# Retrieve an Assignment
assign = course.get_assignment(19816)

# Create an assignment
assign2 = course.create_assignment({"name":"API Assignment Test", 'submission_types': ['online_upload', "online_text_entry"], 'notify_of_update': True})

# Edit an assignment
assign.edit(assignment={ 'due_at': datetime(2022, 12, 31, 11, 59),
    'description': 'I promise this is the last one.',})
print(assign)

# Delete an assignment
dummyAssign = course.create_assignment({"name":"To be deleted", 'submission_types': ['online_upload', "online_text_entry"], 'notify_of_update': True})
dummyAssign = course.get_assignment(19819)
dummyAssign.delete()
