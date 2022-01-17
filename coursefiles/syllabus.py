from config import *

courseID = 1923
course = canvas.get_course(courseID)
f  = (course.get_files())

# Iterate over course files
for i in f:
    # Find the one titled syllabus.pdf
    if str(i)=="syllabus.pdf":
        i.download("./"+str(i))
        print("Syllabus downloaded")
        break
