from datetime import datetime
#from playsound import playsound

time = input("Enter the time that the alarm needs to be set: HH:MM:SS\n")
hour = time[0:2]
minute = time[3:5]
seconds = time[6:8]
period = time[9:11].upper()
print("Creating the alarm...")

while True:
    now = datetime.now()
    curr_hour = now.strftime("%I")
    curr_minute = now.strftime("%M") #stops here when waiting to set the alarm
    curr_second = now.strftime("%S")
    curr_period = now.strftime("%p")

    if(hour == curr_hour):
        if(minute == curr_minute):
            if(seconds == curr_second):
                print("Wake up sleepy head")
                #playsound('audio.mp3')
                break