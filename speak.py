
import time

from time import ctime
import csv

from win32com.client import constants
import win32com.client
   
def createRollList():
        
    rolllist=[];
    

    for i in range(1,95+1):
        rolllist.append(str(i))



    for di in range(1,18+1):
        rolllist.append("D"+str(di));

      

    rolllist.append("IP16");
    rolllist.append("IP19");
    rolllist.append("IP89");
    rolllist.append("IP74");#Check for smriti
    rolllist.append("EE32");
    rolllist.append("EE34");

    return (rolllist)



def speak(audioString):
    print("B: "+audioString)
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(audioString)
	



#-------------------------------------------------------------------------	

speak("Response to your attendance")
rolllist=createRollList()
c=len(rolllist)



todaysAttendance=[]
datetime=ctime()
todaysAttendance.append(datetime);
for i in range (0,5):   #c
    speak(rolllist[i]) #input();  
    x=input()  #0/1
    todaysAttendance.append(x)
    


print(todaysAttendance)

#Write todays attendance in csv
with open("Attendance.csv",'a',newline='') as resultFile:
    wr = csv.writer(resultFile, dialect='excel')
    wr.writerow(todaysAttendance)

