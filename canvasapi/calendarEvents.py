from config import *

# Create a calendar event (Look in the monthly agenda)
c = canvas.create_calendar_event({"title": "The start of semester (✖╭╮✖)!","start_at": "2022-10-19T15:00:00-06:00",
  "description": "<b>It's that time again!</b>",
  "location_name": "Habib University",
  "location_address": "Karachi",
  "workflow_state": "active",
  "context_code": "course_1923", # For this course
  "hidden": False})


# Get a particular calendar event
c = canvas.get_calendar_event(59464) #id
c.edit(calendar_event={"end_at": "2022-10-19T15:00:00-08:00"})
c.delete()
print(c)