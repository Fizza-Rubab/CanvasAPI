from config import *

courseID = 1923
course = canvas.get_course(courseID)
f  = (course.get_files())
for i in f:
    if str(i)=="HW 1 Scores.pdf":
        i.download("./canvasapi/"+str(i))
        print("Syllabus downloaded")
        break
