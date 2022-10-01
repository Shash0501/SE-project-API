from urllib import response
import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "post/111" , {"text" : "shashank is a bad boy"})

print(response.json())


