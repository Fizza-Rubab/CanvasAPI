from config import *

# Set the course
courseID = 1923
course = canvas.get_course(courseID)

# Set the week
week = 2

# Adjust the title correspondingly
if week<10:
    title = "Week 0" + str(week) + " Discussion"
else:
    title = "Week " + str(week) + " Discussion"

# Write the discussion description
message = "Let us discuss the topics covered in Week " + str(week) + "."

# Create the published discussion
course.create_discussion_topic(title=title, message=message, published=True, 
discussion_type="threaded")
