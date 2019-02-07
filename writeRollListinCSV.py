
import csv
def createRollList():
        
    rolllist=[];
    rolllist.append("Date_Time");

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


rolllist=createRollList()
with open("Attendance.csv",'a',newline='') as resultFile:
    wr = csv.writer(resultFile, dialect='excel')
    wr.writerow(rolllist)
