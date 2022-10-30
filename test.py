from urllib import response
import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "post/111" , {"text" : "shashank is a good boy"})
# response = requests.get(BASE + "test" , {"text" : "dibyam is a bad"})

print(response.json())


