import time
import requests
import asyncio

def Scheduled_Message(target_hour, target_minutes):
       
    TEST_API_ENDPOINT = "http://127.0.0.1:5000/webhook"
    API_ENDPOINT = "http://localhost:5005/conversations/user123/trigger_intent?output_channel=latest"
    messagePayload = {"name": "EXTERNAL_scheduled", "entities": {"reminder": "time"}}
        
    while True: #create infinite loop to constantly monitor 
            
        #Calculate local time in seconds 
        local_hour = int(time.strftime("%H", time.localtime()))         
        local_mins = int(time.strftime("%M", time.localtime()))
        local_secs = int(time.strftime("%S", time.localtime()))
        local_time = (local_hour*3600) + (local_mins*60) + local_secs
        print(local_time)
            
        #calculate seconds in a day
        day_secs = 24 * 3600
        tester_secs = 10
                
        #calculate target time in seconds
        target_time = (target_hour * 3600) + (target_minutes*60)
        print(target_time)
                
        #Scheduled reminder
        scheduled_reminder = target_time - local_time
                
                
        #scheduled reminder when target time has passed and you need to reset day first
        scheduled_reminder_late = target_time + (day_secs - local_time) #parenthesis = seconds until day resets 
                
        #Logic to send reminder
            
        if local_time < target_time:
            time.sleep(scheduled_reminder)
            print("Time to log your meals for the day.")
            r = requests.post(url = TEST_API_ENDPOINT, data = messagePayload)
        else:
            time.sleep(scheduled_reminder_late)
            #time.sleep(tester_secs)
            print("Time to log your meals for the day.")
            r = requests.post(url = TEST_API_ENDPOINT, data = messagePayload)
            



                
                
#testScheduled_Message(13,43)
                


