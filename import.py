import sys
import dictionaries

def main():
    attendanceLog = dictionaries.newAttendanceLog(sys.argv)
    print ('\n',attendanceLog)

    if __name__ =='__main__':
        main()




