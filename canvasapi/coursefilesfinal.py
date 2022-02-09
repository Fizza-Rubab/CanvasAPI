# from config import *
from canvasapi import *
import os
import shutil
from datetime import datetime
from datetime import timezone
import pdfcrowd
import requests
import sys
API_URL ="https://hulms.instructure.com"
API_KEY = input("Enter API Access token key:\n")
API_KEY = "17361~Mqdn4rB8xG24lXim7kwhCXcpcsQqgSpsBlC4Sv6bJWJtK2QSMQn34GN4SA1cHb7n"
canvas = Canvas(API_URL, API_KEY)
courseUrl = input("Enter course URL:\n")
courseUrl="https://hulms.instructure.com/courses/1262"
courseID = int(courseUrl.split("/")[-1])
# courseID = 1923
course = canvas.get_course(courseID)
courseDict = course.__dict__
print(courseDict)
d = courseDict["created_at"]
dt = datetime.fromisoformat(d[:-1]).astimezone(timezone.utc)
if int(dt.strftime("%m"))>=5:
    term = "Fall"
else:
    term = "Spring"
cname = courseDict['name'] +" " + term +" " + str(dt.year)
parent_dir = "D:/"
path = os.path.join(parent_dir, cname)
os.mkdir(path)
subfolders = ["a. Course Contents", "b.  Course Objectives", "c. Weekly plan of contents of lectures delivered",
"d. Attendance Record", "e. Copy of lecture notes", "f.  List of Reference Material", 
"g. Copy of assignment,Quizzes, Midterm and Final Examination", "h. Model solutions of all assessments tests given in previous section",
"i. Three sample graded assignments, quizzes, midterms and final examination securing max, min and average marks",
"j. Marks distribution and Grading Model", "k.Complete result of the course", "l. Outcomes Assessment",
"m. Detail of technology involved", "n. Design skills-techniques practiced", "o. Complete analysis of effectiveness of course and level of silks ensured in Technology, Emerging Development Paradigms, Pertaining to Industry, Mod",
"Syllabus"]
parent_dir = path
for folder in subfolders:
    os.mkdir(os.path.join(parent_dir,folder))
print("make folders")
inthesyllabus = ["a. Course Contents", "b.  Course Objectives", "c. Weekly plan of contents of lectures delivered",
"f.  List of Reference Material"]
for dest in inthesyllabus:
    shutil.copyfile("./InTheSyllabus.pdf", str(os.path.join(parent_dir,dest+"/InTheSyllabus.pdf")))
print("copied files")
# Get the syllabus
f  = (course.get_files())
for i in f:
    if str(i)=="syllabus.pdf":
        i.download(path+"/Syllabus/" + str(i))
        print("Syllabus downloaded")
        break

print("downloaded syllabus")
# Get Read only copy of all quizzes
quizzespath = path + "/g. Copy of assignment,Quizzes, Midterm and Final Examination/Quizzes"
os.mkdir(quizzespath)
quizzes = course.get_quizzes()
for q in quizzes:
    print(q)
    url = (q.__dict__)["html_url"]
    url+="/read_only"
    try:
        client = pdfcrowd.HtmlToPdfClient('demo', 'ce544b6ea52a5621fb9d55f8b542d14d')
        client.setCookies("log_session_id=bb9a35f0be4a0272c7f0796f3294fb73;canvas_session=kJPps4B5r9yutNE7A9hoeQ+NErECujT5-Ml2nHcxulzIpnATf8KycVDtVmxgd4W3yNXMnQqHzJUDYwsOLA5gUQGuhXZIeMDcvADmRZXGCcVPXnVvY-rQBSwmhWPtbMjP15xyEkswHUopyeb4oLn09kc_qOkrutz4FRkF16Cak8ktj2tSOQMx-VU5V91pciCEwp1hUVPSbpbhS7xCX26yr5t2av4TZsgps-jjLz7m1kuAWopNT9ysDyb_2Usd33p8DebGTF1JpGwGc-_-VIvEPQEcwllMydZVR7JxB-oogNUNIVNoWWJ6tFTalS_rtvJQWvcW5PnnIg6OL4nEv0aypkDMUmxZTDEWkKrku32M-6rxI013Eb3qso3JK5gUcaEfX2yBrQmqUoo1LqBeNg4lk7B_u7zCaamQ8DqWL8HgCon3nl-vAsnMZpN6CzOW8T1mXnVjd9IZP1XUwveOs7cQLBn1O2mrfVujtfnFmDA_RROMgWI_AUlV8hWEiFNkbSybo4Ex89MtMbrl7FeiEPGPfLsTkuMPfjm1XvbmWDCBDE8JPkOYQ3YSaD5beXpv8YJM_OZj606GZBOmoj01zX13bQnXhjL7h8mKjRfFYOb0aI3mwlHRks1EmRDerF9AGTPICxVntpgqwZceMe_HbmTaD0MO8LbunayqPjxi_c-Ixe_lWGzMkdkj20RfJuZm4UOqDUENQeT_PdE5rQImw4ucWm4nSbiLmoMx06a1nmuoDeryNPaoZctKH44RoN9QGFL0gX3fONW-XSRn_e0CeyGGkoF.5jQW_aj_tleV2fbB6ePrq-FSeck.YgNOpg")
        client.setCustomJavascript("document.getElementById('questions').classList.remove('brief');")
        client.convertUrlToFile(url, quizzespath+'/'+str((q.__dict__)["title"])+'.pdf')
    except pdfcrowd.Error as why:
        sys.stderr.write('Pdfcrowd Error: {}\n'.format(why))
        raise

print("Quizzes done")



# Get model solution for all quizzes
# quizzesmodelpath = path + "/h. Model solutions of all assessments tests given in previous section/Quizzes"
# os.mkdir(quizzesmodelpath)
# for q in quizzes:
#     try:
#         client = pdfcrowd.HtmlToPdfClient('demo', 'ce544b6ea52a5621fb9d55f8b542d14d')
#         client.setCookies("log_session_id=bb9a35f0be4a0272c7f0796f3294fb73;canvas_session=kJPps4B5r9yutNE7A9hoeQ+NErECujT5-Ml2nHcxulzIpnATf8KycVDtVmxgd4W3yNXMnQqHzJUDYwsOLA5gUQGuhXZIeMDcvADmRZXGCcVPXnVvY-rQBSwmhWPtbMjP15xyEkswHUopyeb4oLn09kc_qOkrutz4FRkF16Cak8ktj2tSOQMx-VU5V91pciCEwp1hUVPSbpbhS7xCX26yr5t2av4TZsgps-jjLz7m1kuAWopNT9ysDyb_2Usd33p8DebGTF1JpGwGc-_-VIvEPQEcwllMydZVR7JxB-oogNUNIVNoWWJ6tFTalS_rtvJQWvcW5PnnIg6OL4nEv0aypkDMUmxZTDEWkKrku32M-6rxI013Eb3qso3JK5gUcaEfX2yBrQmqUoo1LqBeNg4lk7B_u7zCaamQ8DqWL8HgCon3nl-vAsnMZpN6CzOW8T1mXnVjd9IZP1XUwveOs7cQLBn1O2mrfVujtfnFmDA_RROMgWI_AUlV8hWEiFNkbSybo4Ex89MtMbrl7FeiEPGPfLsTkuMPfjm1XvbmWDCBDE8JPkOYQ3YSaD5beXpv8YJM_OZj606GZBOmoj01zX13bQnXhjL7h8mKjRfFYOb0aI3mwlHRks1EmRDerF9AGTPICxVntpgqwZceMe_HbmTaD0MO8LbunayqPjxi_c-Ixe_lWGzMkdkj20RfJuZm4UOqDUENQeT_PdE5rQImw4ucWm4nSbiLmoMx06a1nmuoDeryNPaoZctKH44RoN9QGFL0gX3fONW-XSRn_e0CeyGGkoF.5jQW_aj_tleV2fbB6ePrq-FSeck.YgNOpg")
#         client.setCustomJavascript("document.getElementById('questions').classList.remove('brief');sp = document.getElementsByClassName('correct_answer');for(var i = 0; i < sp.length; i++){sp[i].style.backgroundColor = 'Aquamarine';}")
#         client.convertUrlToFile(q.__dict__["html_url"]+'/edit#questions_tab', quizzesmodelpath+'/'+str((q.__dict__)["title"])+'-solution.pdf')
#     except pdfcrowd.Error as why:
#         sys.stderr.write('Pdfcrowd Error: {}\n'.format(why))
#         raise

# Get 3 sample graded student submissions of each quiz
quizsubmissionspath = path + "/i. Three sample graded assignments, quizzes, midterms and final examination securing max, min and average marks/Quizzes"
os.mkdir(quizsubmissionspath)
for q in quizzes:
    submissions = q.get_submissions()
    s = sorted([i for i in submissions if i.score!=None], key=lambda d: d.__dict__['score'])
    if s==[]:
        continue
    lowestsub = s[0]
    highestsub = s[-1]
    Sum = 0
    count = 0
    for i in s:
        if i.score!=None:
            Sum+=i.score
            count+=1
    average = Sum/count
    averagesub = min(s, key=lambda x:abs(x.score-average))
    try:
        client = pdfcrowd.HtmlToPdfClient('demo', 'ce544b6ea52a5621fb9d55f8b542d14d')
        client.setCookies("log_session_id=bb9a35f0be4a0272c7f0796f3294fb73;canvas_session=kJPps4B5r9yutNE7A9hoeQ+NErECujT5-Ml2nHcxulzIpnATf8KycVDtVmxgd4W3yNXMnQqHzJUDYwsOLA5gUQGuhXZIeMDcvADmRZXGCcVPXnVvY-rQBSwmhWPtbMjP15xyEkswHUopyeb4oLn09kc_qOkrutz4FRkF16Cak8ktj2tSOQMx-VU5V91pciCEwp1hUVPSbpbhS7xCX26yr5t2av4TZsgps-jjLz7m1kuAWopNT9ysDyb_2Usd33p8DebGTF1JpGwGc-_-VIvEPQEcwllMydZVR7JxB-oogNUNIVNoWWJ6tFTalS_rtvJQWvcW5PnnIg6OL4nEv0aypkDMUmxZTDEWkKrku32M-6rxI013Eb3qso3JK5gUcaEfX2yBrQmqUoo1LqBeNg4lk7B_u7zCaamQ8DqWL8HgCon3nl-vAsnMZpN6CzOW8T1mXnVjd9IZP1XUwveOs7cQLBn1O2mrfVujtfnFmDA_RROMgWI_AUlV8hWEiFNkbSybo4Ex89MtMbrl7FeiEPGPfLsTkuMPfjm1XvbmWDCBDE8JPkOYQ3YSaD5beXpv8YJM_OZj606GZBOmoj01zX13bQnXhjL7h8mKjRfFYOb0aI3mwlHRks1EmRDerF9AGTPICxVntpgqwZceMe_HbmTaD0MO8LbunayqPjxi_c-Ixe_lWGzMkdkj20RfJuZm4UOqDUENQeT_PdE5rQImw4ucWm4nSbiLmoMx06a1nmuoDeryNPaoZctKH44RoN9QGFL0gX3fONW-XSRn_e0CeyGGkoF.5jQW_aj_tleV2fbB6ePrq-FSeck.YgNOpg")
        client.convertUrlToFile(lowestsub.__dict__["html_url"], quizsubmissionspath+'/'+str((q.__dict__)["title"])+'-min.pdf')
        client.convertUrlToFile(highestsub.__dict__["html_url"], quizsubmissionspath+'/'+str((q.__dict__)["title"])+'-max.pdf')
        client.convertUrlToFile(averagesub.__dict__["html_url"], quizsubmissionspath+'/'+str((q.__dict__)["title"])+'-avg.pdf')
    except pdfcrowd.Error as why:
        sys.stderr.write('Pdfcrowd Error: {}\n'.format(why))
        raise
        
# #  Get read only copy for an assignments
assignpath = path + "/g. Copy of assignment,Quizzes, Midterm and Final Examination/Assignments"
os.mkdir(assignpath)
assigns = course.get_assignments()  

for i in assigns:
    if i.__dict__["is_quiz_assignment"]==False:
        print(i)
        url = i.__dict__["html_url"]
        t = str(i.__dict__["name"]) + '.pdf'
        t = t.replace(":", "")
        try:
            client = pdfcrowd.HtmlToPdfClient('demo', 'ce544b6ea52a5621fb9d55f8b542d14d')
            client.setCookies("log_session_id=bb9a35f0be4a0272c7f0796f3294fb73;canvas_session=kJPps4B5r9yutNE7A9hoeQ+NErECujT5-Ml2nHcxulzIpnATf8KycVDtVmxgd4W3yNXMnQqHzJUDYwsOLA5gUQGuhXZIeMDcvADmRZXGCcVPXnVvY-rQBSwmhWPtbMjP15xyEkswHUopyeb4oLn09kc_qOkrutz4FRkF16Cak8ktj2tSOQMx-VU5V91pciCEwp1hUVPSbpbhS7xCX26yr5t2av4TZsgps-jjLz7m1kuAWopNT9ysDyb_2Usd33p8DebGTF1JpGwGc-_-VIvEPQEcwllMydZVR7JxB-oogNUNIVNoWWJ6tFTalS_rtvJQWvcW5PnnIg6OL4nEv0aypkDMUmxZTDEWkKrku32M-6rxI013Eb3qso3JK5gUcaEfX2yBrQmqUoo1LqBeNg4lk7B_u7zCaamQ8DqWL8HgCon3nl-vAsnMZpN6CzOW8T1mXnVjd9IZP1XUwveOs7cQLBn1O2mrfVujtfnFmDA_RROMgWI_AUlV8hWEiFNkbSybo4Ex89MtMbrl7FeiEPGPfLsTkuMPfjm1XvbmWDCBDE8JPkOYQ3YSaD5beXpv8YJM_OZj606GZBOmoj01zX13bQnXhjL7h8mKjRfFYOb0aI3mwlHRks1EmRDerF9AGTPICxVntpgqwZceMe_HbmTaD0MO8LbunayqPjxi_c-Ixe_lWGzMkdkj20RfJuZm4UOqDUENQeT_PdE5rQImw4ucWm4nSbiLmoMx06a1nmuoDeryNPaoZctKH44RoN9QGFL0gX3fONW-XSRn_e0CeyGGkoF.5jQW_aj_tleV2fbB6ePrq-FSeck.YgNOpg")
            client.convertUrlToFile(url, assignpath+'/'+t)
        except pdfcrowd.Error as why:
            sys.stderr.write('Pdfcrowd Error: {}\n'.format(why))
            raise


# #  Get 3 submissions for each assignments
assignsubmissionspath = path + "/i. Three sample graded assignments, quizzes, midterms and final examination securing max, min and average marks/Assignments"
os.mkdir(assignsubmissionspath)
for a in assigns:
    # print(a.__dict__)
    if (not a.__dict__['is_quiz_assignment']) or ("none" not in a.__dict__['submission_types']):
        submissions = a.get_submissions()
        s = [x for x in submissions if x.score!=None]
        if len(s)==0: continue
        lowestsub = min(s, key=lambda x: x.score)
        highestsub = max(s, key=lambda x: x.score)
        Sum = 0
        count = 0
        for i in s:
            if i.score!=None:   
                Sum+=i.score
                count+=1
        average = Sum/count
        averagesub = min(s, key=lambda x:abs(x.score-average))
        if a.__dict__["id"]==11565:
            print(lowestsub.__dict__)
        if lowestsub.__dict__["submission_type"]=="online_text_entry":
            try:
                client = pdfcrowd.HtmlToPdfClient('demo', 'ce544b6ea52a5621fb9d55f8b542d14d')
                client.setCookies("log_session_id=bb9a35f0be4a0272c7f0796f3294fb73;canvas_session=kJPps4B5r9yutNE7A9hoeQ+NErECujT5-Ml2nHcxulzIpnATf8KycVDtVmxgd4W3yNXMnQqHzJUDYwsOLA5gUQGuhXZIeMDcvADmRZXGCcVPXnVvY-rQBSwmhWPtbMjP15xyEkswHUopyeb4oLn09kc_qOkrutz4FRkF16Cak8ktj2tSOQMx-VU5V91pciCEwp1hUVPSbpbhS7xCX26yr5t2av4TZsgps-jjLz7m1kuAWopNT9ysDyb_2Usd33p8DebGTF1JpGwGc-_-VIvEPQEcwllMydZVR7JxB-oogNUNIVNoWWJ6tFTalS_rtvJQWvcW5PnnIg6OL4nEv0aypkDMUmxZTDEWkKrku32M-6rxI013Eb3qso3JK5gUcaEfX2yBrQmqUoo1LqBeNg4lk7B_u7zCaamQ8DqWL8HgCon3nl-vAsnMZpN6CzOW8T1mXnVjd9IZP1XUwveOs7cQLBn1O2mrfVujtfnFmDA_RROMgWI_AUlV8hWEiFNkbSybo4Ex89MtMbrl7FeiEPGPfLsTkuMPfjm1XvbmWDCBDE8JPkOYQ3YSaD5beXpv8YJM_OZj606GZBOmoj01zX13bQnXhjL7h8mKjRfFYOb0aI3mwlHRks1EmRDerF9AGTPICxVntpgqwZceMe_HbmTaD0MO8LbunayqPjxi_c-Ixe_lWGzMkdkj20RfJuZm4UOqDUENQeT_PdE5rQImw4ucWm4nSbiLmoMx06a1nmuoDeryNPaoZctKH44RoN9QGFL0gX3fONW-XSRn_e0CeyGGkoF.5jQW_aj_tleV2fbB6ePrq-FSeck.YgNOpg")
                client.convertStringToFile(lowestsub.__dict__["body"], assignsubmissionspath+'/'+str((a.__dict__)["name"])+'-min.pdf')
                client.convertStringToFile(highestsub.__dict__["body"], assignsubmissionspath+'/'+str((a.__dict__)["name"])+'-max.pdf')
                client.convertStringToFile(averagesub.__dict__["body"], assignsubmissionspath+'/'+str((a.__dict__)["name"])+'-avg.pdf')
            except pdfcrowd.Error as why:
                sys.stderr.write('Pdfcrowd Error: {}\n'.format(why))
                raise
        elif lowestsub.__dict__["submission_type"]=="online_upload":
            attachments = lowestsub.__dict__["attachments"]
            for j in attachments:
                url = j["url"]
                r = requests.get(url, allow_redirects=True)
                open("min- " + j["filename"], 'wb').write(r.content)
            attachments = highestsub.__dict__["attachments"]
            for j in attachments:
                url = j["url"]
                r = requests.get(url, allow_redirects=True)
                open("max- " + j["filename"], 'wb').write(r.content)
            attachments = averagesub.__dict__["attachments"]
            for j in attachments:
                url = j["url"]
                r = requests.get(url, allow_redirects=True)
                open("avg- " + j["filename"], 'wb').write(r.content)

# Make an empty folder for model solutions of assignments - To be added by instructor
assignmodelpath = path + "/h. Model solutions of all assessments tests given in previous section/Assignments"
os.mkdir(assignmodelpath)