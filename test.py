#This python file is sending a request
import requests
BASE="http://127.0.0.1:5000/"
DATA_REQUEST_REGISTER="covidRequestregister"
DATA_REQUEST_LOGIN="covidRequestlogin"
DATA_REQUEST_EDIT="covidRequestedit"
# post with an arguments
name = "MarwaJarada"
email = "afnan@gmail.com"
password = "123456"

new_name="newname6"
new_email="newemail6@gmail.com"
new_password="newpass66"
#
# #response=requests.post(BASE+DATA_REQUEST_REGISTER+"/"+name+"/"+email+"/"+password)
response=requests.post(BASE+DATA_REQUEST_LOGIN, json={"email":email,"password":password})
print(response.json())
