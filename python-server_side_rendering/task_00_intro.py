#!/usr/bin/python3

import os

def generate_invitations(template, attendees):
    try:
        if not isinstance(template, str):
            raise TypeError("template not a string")
        
        if len(template) == 0:
            raise IndexError("string is empty")

        if not isinstance(attendees, list): 
            raise TypeError("attendees not a list")
        
        if len(attendees) == 0:
            raise IndexError("List is empty")
        
        if not isinstance(attendees[0], dict):
            raise TypeError("not a list of dicts")
        
        for i in range(len(attendees)):
            
            for k, v in attendees[i].items():
            
                temp1 = template.replace("{name}", attendees[i]["name"])
                temp2 = temp1.replace("{event_title}", attendees[i]["event_title"])
                temp3 = temp2.replace("{event_date}", attendees[i]["event_date"])
                temp4 = temp3.replace("{event_location}", attendees[i]["event_location"])
              

            with open(f"output_{i+1}.txt", 'w') as file:
                if os.path.exists(f"output_{i+1}.txt") == False:
                    file.write(temp4)
                else:
                    file.write(temp4)
        
    except Exception as e:
        print(e)

