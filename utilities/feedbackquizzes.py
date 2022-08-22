from time import sleep
from canvasapi import *

API_URL ="https://hulms.instructure.com"
API_KEY = ""
canvas = Canvas(API_URL, API_KEY)

# Set the course
course_id = 2008
course = canvas.get_course(course_id)

# Identify the quiz to be duplicated (Create one sample quiz)
quiz_id = 6078

# Fetch the quiz
q = course.get_quiz(quiz_id)

total_weeks = 4

for w in range(1, total_weeks+1):

    # Set the title
    title = "Feedback for Week %02d"%w

    # Create the quiz with the same settings as the one to be duplicated
    newquiz = course.create_quiz(quiz={"title":title, "description":q.__dict__["description"], 
    "quiz_type":q.__dict__["quiz_type"], "allowed_attempts":q.__dict__["allowed_attempts"],
    "scoring_policy":q.__dict__["scoring_policy"],"published":q.__dict__["published"],
    })

    # Ensure that it is created
    print(newquiz)

    # Fetch the questions
    ques = q.get_questions()

    for i in ques:
        # For each question, create a new question in the new quiz
        d = {"position":i.__dict__["position"],"question_name":i.__dict__["question_name"],
        "question_type":i.__dict__["question_type"],"question_text":i.__dict__["question_text"],
        "points_possible":i.__dict__["points_possible"]}
        print(newquiz.create_question(question=d))
    sleep(2)
