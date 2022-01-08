from config import *

############################### Course Retrieval ################################

# Get all courses
# Returns a paginated list of Course objects which can be treated as a python list 
# courses = canvas.get_courses()
# [print(c) for c in courses]

# Get a particular course of the specified id
courseID = 1923
course = canvas.get_course(courseID)
print(course)

############################### Course Users Retrieval ###########################

# Get users in a course
users = course.get_users()
for user in users:
    print(user)

# Retrive students
users = course.get_users(enrollment_type=['student'])
for user in users:
    print(user)
# Retrive TAs and teachers
users = course.get_users(enrollment_type=['teacher', 'ta'])
for user in users:
    print(user)

# Filter the users by state
users = course.get_users(enrollment_state=['active', 'invited'])
for user in users:
    print(user)

########################## Updating the course ################################
# For some reason updation is not happening, I have tried with my own scripts aswell
# Have still added the scripts though

# Updating the name
print(course.name)
course.update(course={'name': 'Fizza\'s Course'})
print(course.name)

# Updating the course start and end dates
start_date = datetime(2022, 1, 1, 0, 1)
end_date = datetime(2022, 12, 31, 11, 59)
course.update(course={'start_at': start_date, 'end_at': end_date})

# Please dont delete or conclude this course. :pleadingface_emoji

# End a Course
course.conclude()

# Delete a course altogether
course.delete()

# Create a course section
sect = course.create_course_section(section={ "name": "S4-The Undiscovered"})#name not updated but section created weird stuff
print(sect)