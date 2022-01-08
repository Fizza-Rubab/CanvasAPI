from config import *

# Create a conversation
# c = canvas.create_conversation(recipients=['course_1923'], body="Hello. This is an api generated message.\nSigning off,\nFizza")
# print(c)

# Get Conversations
convos = canvas.get_conversations()
[print(i) for i in convos]

