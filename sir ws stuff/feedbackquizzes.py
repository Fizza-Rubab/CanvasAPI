from config import *
course = canvas.get_course(1923)

# Identify the quiz to be duplicated
quizid = 4946

# Fetch the quiz
q = course.get_quiz(quizid)

# The week no
week = 2

# Set the title
title = "Feedback for Week" + str(week)

# Create the quiz with the same settings as the one to be duplicated
newquiz = course.create_quiz(quiz={"title":title + " Copy", "description":q.__dict__["description"], 
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