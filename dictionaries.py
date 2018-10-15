def newAttendanceLog(Dictionary):
    if((len(Dictionary)%3)==1): #check if the length of the list is divisible by 3
        attendanceLog = dict() #creates an empty attendance log
        for k in range(1,len(Dictionary), 3):
            studentName = Dictionary[1]
            studentMatricule = Dictionary[2]
            studentPhoneNbr = Dictionary[3]
            studentInfo = (studentMatricule, studentPhoneNbr)
            attendanceLog[studentName] = studentInfo


        return attendanceLog
    return '\nRuntime Error: Not enough arguments to create and attendanceLog, 03 minimum required'