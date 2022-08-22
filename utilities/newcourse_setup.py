from time import sleep
from canvasapi import *

API_URL ="https://hulms.instructure.com"
API_KEY = "17361~0yOJPT02iOLJ5ZUoVvSRhYvdf7AAJ4kv4ET95osteKVuf8Jxbynvq0bgFGn37UST"
canvas = Canvas(API_URL, API_KEY)

# Set the course
course_id = 2008
course = canvas.get_course(course_id)

total_weeks = 3

quiz_id = 6078

# Fetch the quiz
q = course.get_quiz(quiz_id)

for w in range(1, total_weeks+1):

    # Set the title
    title = "Week %02d"%w

    # Create the quiz with the same settings as the one to be duplicated
    newmodule = course.create_module(module={"name":title})

    title_discussion = "Week %02d Discussion"%w
    
    # Write the discussion description
    message = "Let us discuss the topics covered in Week %02d."%w

    # Create the published discussion
    discussion = course.create_discussion_topic(title=title_discussion, message=message, published=True, # Published can be set to false to avoid notifications
    discussion_type="threaded")


    newmodule.create_module_item(module_item={"type":"Discussion", "content_id":discussion.__dict__["id"], "title":title_discussion})

    title_quiz = "Feedback for Week %02d"%w

    # Create the quiz with the same settings as the one to be duplicated
    newquiz = course.create_quiz(quiz={"title":title_quiz, "description":q.__dict__["description"], 
    "quiz_type":q.__dict__["quiz_type"], "allowed_attempts":q.__dict__["allowed_attempts"],
    "scoring_policy":q.__dict__["scoring_policy"],"published":q.__dict__["published"],
    })

    # Fetch the questions
    ques = q.get_questions()


    for i in ques:
        # For each question, create a new question in the new quiz
        d = {"position":i.__dict__["position"],"question_name":i.__dict__["question_name"],
        "question_type":i.__dict__["question_type"],"question_text":i.__dict__["question_text"],
        "points_possible":i.__dict__["points_possible"]}
        print(newquiz.create_question(question=d))
        sleep(1)
    
    newmodule.create_module_item(module_item={"type":"Quiz", "content_id":newquiz.__dict__["id"], "title":title_quiz})

    # Ensure that it is created
    print(newmodule)

    sleep(1.5)
