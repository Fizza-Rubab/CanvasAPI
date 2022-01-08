import requests
import json
import os

# Informing canvas of file upload
url = "https://hulms.instructure.com/api/v1/courses/1923/files"
headers ={"authorization":"Bearer ygCxdvuMbLXDtgiCpEdqLrRRZ02kASevZHl9vddtJPtBDS7MGs8WvT5wlPcapUcB"}
r =requests.post(url, headers=headers, data=json.dumps(
 {'name': 'images.jpeg', 'size': '5752',
 'content_type': 'image/jpeg', 'on_duplicate': 'overwrite', 'parent_folder_path':'/'}),)
r.raise_for_status()
print("Step 1 Status Code: ", r.status_code, "Post URL: ", url)
print(r.json())
print()

# Uploading of file to temporal URL
url2 = r.json()['upload_url']
r2 = requests.post(url2, files={"file": open("images.jpeg", 'rb')})
r2.raise_for_status()
print("Step 2 Status Code: ", r2.status_code, "Post URL: ", url2)
print(r2.json())
print()

# Activation and Retrieval
url3 = r2.json()['location']
r3 = requests.get(url3, headers={"authorization": "Bearer ygCxdvuMbLXDtgiCpEdqLrRRZ02kASevZHl9vddtJPtBDS7MGs8WvT5wlPcapUcB"})
r3.raise_for_status()
print("Step 3 Status Code: ", r3.status_code, "Post URL: ", url3)
print(r3.json())