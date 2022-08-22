from time import sleep
from canvasapi import *

API_URL ="https://hulms.instructure.com"
API_KEY = ""
canvas = Canvas(API_URL, API_KEY)

# Set the course
course_id = 2008
course = canvas.get_course(course_id)
total_weeks = 14

for i in range(1, total_weeks+1):
    print("Creating Discussion for week %02d"%i)
    title = "Week %02d Discussion"%i
    
    # Write the discussion description
    message = "Let us discuss the topics covered in Week %02d."%i

    # Create the published discussion
    course.create_discussion_topic(title=title, message=message, published=True, # Published can be set to false to avoid notifications
    discussion_type="threaded")
    
    # Delay added
    sleep(2)
