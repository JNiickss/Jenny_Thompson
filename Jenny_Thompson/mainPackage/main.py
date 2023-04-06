# Name: Josh Nickol 
# email: nickolje@mail.uc.edu
# Assignment Title: Assignment 10
# Course: IS 4010
# Semester/Year: Spring 2023
# Brief Description: This project demonstrates that I can use Eclipse to create a PyDev project to 
#build a URL with a data request, submit it to a server, receieve the results and then parse them into a python dictionary
# Citations:
# Anything else that's relevant:
import requests
import json
# This is the request to the server which are then stored in response
response = requests.get('https://api.ftc.gov/v0/hsr-early-termination-notices?api_key=0PmoM6eQHN168ZuY0UrGy1bCLo7viDAUkMva919O')
json_string = response.content
# This will be the python dictionary
parsed_json = json.loads(json_string)
# Here I'm only getting the attributes which are basically certain parties that have filed for large mergers or aquisitions
# and are waiting for the government to review these requests and this also tells you when these requests were created 
# and/or updated.
for x in parsed_json['data']:
    print(x['attributes'])
