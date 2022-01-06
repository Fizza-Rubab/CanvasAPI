from canvas_lms_api import Canvas
grader = Canvas(base="https://hulms.instructure.com", token="17361~ygCxdvuMbLXDtgiCpEdqLrRRZ02kASevZHl9vddtJPtBDS7MGs8WvT5wlPcapUcB", course="1923")
# Find your assignment id number see Get Assignments Example
assignment_id = "19644"
# Find your student id number see Get Course Users Example
student_id = ""

# Set score and comment
score = "100.35"
comment = "The student failed to complete the assignment\nAnd they got thse points wrong\n(-10) for poor guessing"
grader.SubmitGrade(assignment_id, student_id, score, comment, visibility=False)