from config import *

courseID = 1262
course = canvas.get_course(courseID)
quizzes = course.get_quizzes()
q = course.get_quiz(2633)

# import requests
# import json
# import os

# # Informing canvas of file upload
# url = "https://hulms.instructure.com/api/v1/courses/1923/files"
# headers ={"authorization":"Bearer ygCxdvuMbLXDtgiCpEdqLrRRZ02kASevZHl9vddtJPtBDS7MGs8WvT5wlPcapUcB"}
# r =requests.post(url, headers=headers, data=json.dumps(
#  {'name': 'images.jpeg', 'size': '5752',
#  'content_type': 'image/jpeg', 'on_duplicate': 'overwrite', 'parent_folder_path':'/'}),)
# r.raise_for_status()
# print("Step 1 Status Code: ", r.status_code, "Post URL: ", url)
# print(r.json())
# print()
# print(q.__dict__)

s = q.get_submissions()
s = [i for i in s]
s = sorted(s, key=lambda d: d.__dict__['score']) 

for i in s:
    print()
    print(i.__dict__)