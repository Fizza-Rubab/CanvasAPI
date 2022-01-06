from canvas_lms_api import Canvas
teacher = Canvas(base="https://hulms.instructure.com", token="17361~ygCxdvuMbLXDtgiCpEdqLrRRZ02kASevZHl9vddtJPtBDS7MGs8WvT5wlPcapUcB", course="1923")
assignments = teacher.GetAssignments()
output = open("Assignments.txt", "w")
for i in assignments:
    output.write(str(i))