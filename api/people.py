from canvas_lms_api import Canvas
grader =  Canvas(base="https://hulms.instructure.com", token="17361~ygCxdvuMbLXDtgiCpEdqLrRRZ02kASevZHl9vddtJPtBDS7MGs8WvT5wlPcapUcB", course="1923")
print(grader.GetCourseUsers())