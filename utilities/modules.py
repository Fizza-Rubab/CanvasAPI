from time import sleep
from canvasapi import *

API_URL ="https://hulms.instructure.com"
API_KEY = ""
canvas = Canvas(API_URL, API_KEY)

# Set the course
course_id = 2008
course = canvas.get_course(course_id)

total_weeks = 4

for w in range(1, total_weeks+1):

    # Set the title
    title = "Week %02d"%w

    # Create the quiz with the same settings as the one to be duplicated
    newmodule = course.create_module(module={"name":title})

    # Ensure that it is created
    print(newmodule)

    sleep(1.5)
