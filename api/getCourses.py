from canvas_lms_api import Canvas
student = Canvas(base="https://hulms.instructure.com", token="17361~ygCxdvuMbLXDtgiCpEdqLrRRZ02kASevZHl9vddtJPtBDS7MGs8WvT5wlPcapUcB")
courses = student.GetCourses()
print(courses)