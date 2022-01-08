from canvas_lms_api import Canvas
grader = Canvas(base="https://hulms.instructure.com", token="17361~ygCxdvuMbLXDtgiCpEdqLrRRZ02kASevZHl9vddtJPtBDS7MGs8WvT5wlPcapUcB", course="1923")
# Find your assignment id number see Get Assignments Example
assignment_id = "19794"
student_id = "1048"

# Set score and comment
score = "0.5"
comment = "Grace marks"
grader.SubmitGrade(assignment_id, student_id, score, comment, visibility=False)