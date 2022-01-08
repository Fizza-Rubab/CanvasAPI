from canvasapi import *
from datetime import datetime

from canvasapi import submission

# Setting the parameters
API_URL ="https://hulms.instructure.com"
API_KEY = "17361~ygCxdvuMbLXDtgiCpEdqLrRRZ02kASevZHl9vddtJPtBDS7MGs8WvT5wlPcapUcB"
canvas = Canvas(API_URL, API_KEY)

courseID = 1923
course = canvas.get_course(courseID)
print(course)

# Fetch the assignment
assignment = course.get_assignment(19665)

# To retrieve a particular submission
s = assignment.get_submission(1048)

# Mark the submission as read
s.mark_read()

# Upload a file as a comment to this submission
# s.upload_comment('./canvasapi/comment.txt')

# Delete the submission
s.edit(submission={"posted_grade":55})
print(s.name)