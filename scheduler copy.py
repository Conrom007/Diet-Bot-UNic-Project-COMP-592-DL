import time
import requests
import asyncio


async def Scheduled_Message(target_hour, target_minutes):
    API_ENDPOINT = "http://localhost:5005/webhooks/rest/webhook"

    messagePayload = {'sender': 'default', 'message': 'Your message is here'}
    
    while True: #create infinite loop to constantly monitor 
    #(IF I USE RETURN IN EACH CONDITIONAL STEP THEN THE LOOP NEEDS TO BE IN THE CUSTOM ACTION)
        
        #Calculate local time in seconds 
        local_hour = int(time.strftime("%H", time.localtime()))
        local_mins = int(time.strftime("%M", time.localtime()))
        local_secs = int(time.strftime("%S", time.localtime()))
        local_time = (local_hour*3600) + (local_mins*60) + local_secs
        print(local_time)
        
        #calculate seconds in a day
        day_secs = 24 * 3600
        
        #calculate target time in seconds
        target_time = (target_hour * 3600) + (target_minutes*60)
        print(target_time)
        
        #Scheduled reminder
        scheduled_reminder = target_time - local_time
        
        
        #scheduled reminder when target time has passed and you need to reset day first
        scheduled_reminder_late = target_time + (day_secs - local_time) #parenthesis = seconds until day resets 
        
        #Logic to send reminder
    
        if local_time < target_time:
            await asyncio.sleep(scheduled_reminder)
            print("Time to log your meals for the day.") 
          
        elif local_time >= target_time:
            await asyncio.sleep(scheduled_reminder_late)
            print("Time to log your meals for the day.")
            
        
        
        

    
Scheduled_Message(20,28)

