from config import *

courseID = 1923
course = canvas.get_course(courseID)
print(course)

# Create an empty discussion
# discussion = course.create_discussion_topic()

# Discussion update not working for some reason
# Tried through postman aswell
# discussion.update(discussion_topic={"title":"A tale of two cities",})

# Get a discussion by ID
discussion2 =course.get_discussion_topic(17065)
print(discussion2)


# Fetch all the discussions in the course and also their message
discussions =course.get_discussion_topics()
[print(d + " " +  d.message) for d in discussions]

