import time

class Time:
    def __init__(self,hour,minute,seconds):
        self.Hour = hour
        self.Minute = minute
        self.Seconds = seconds
        pass
####################
    def Show_Time(self):
        print(self.Hour," : ",self.Minute," : ",self.Seconds)
####################
    def Subtraction_of_two_times(self,time2):
        hour = self.Hour - time2.Hour
        minute = self.Minute - time2.Minute
        seconds = self.Seconds - time2.Seconds
        return (Time(hour,minute,seconds))
####################
    def The_sum_of_two_times(self,time2):
        hour = self.Hour + time2.Hour
        minute = self.Minute + time2.Minute
        seconds = self.Seconds + time2.Seconds
        return (Time(hour,minute,seconds))
####################
    def Convert_time_to_seconds(self):
        Se = ((self.Hour*3600)+(self.Minute*60)+(self.Seconds))
        return Se
####################
    def Convert_seconds_to_time(self,seconds):
        hour = int(seconds/3600)
        seconds -= (hour*3600)
        minute = int(seconds/60)
        seconds -= (minute*60)
        return (Time(hour,minute,seconds))
####################
    def World_time_conversion_to_Tehran_time(self):
        gmt = time.gmtime(time.time())
        print("GMT time -> ",gmt.tm_hour, ':', gmt.tm_min, ':', gmt.tm_sec)
        hour = int(gmt.tm_hour + 3)
        minute = int(gmt.tm_min + 30)
        return (Time(hour,minute,gmt.tm_sec))
####################
    def Check_Fix(self):
        if self.Seconds >= 60:
            minute = int(self.Seconds/60)
            self.Seconds = (self.Seconds - (minute * 60))
            self.Minute += minute
        if (self.Minute) >= 60:
            hour = int(self.Minute/60)
            self.Minute = (self.Minute - (hour*60))
            self.Hour += hour
        if (self.Hour) >= 24:
            self.Hour = (self.Hour-24)
        return (Time(self.Hour,self.Minute,self.Seconds))
####################
Hour1 = int(input("Enter Hour of first time: "))
Minute1 = int(input("Enter Minute of first time: "))
Seconds1 = int(input("Enter Seconds of second time: "))
Hour2 = int(input("Enter Hour of second time: "))
Minute2 = int(input("Enter Minute of first time: "))
Seconds2 = int(input("Enter Seconds of second time: "))
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
T = Time(Hour1,Minute1,Seconds1)
T2 = Time(Hour2,Minute2,Seconds2)
print("Show first time: ")
T.Check_Fix()
T.Show_Time()
print("Show second time: ")
T2.Check_Fix()
T2.Show_Time()
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
print("The sum of two times: ")
T = Time(Hour1,Minute1,Seconds1)
T2 = Time(Hour2,Minute2,Seconds2)
T_A = T.The_sum_of_two_times(T2)
T_A = T_A.Check_Fix()
T_A.Show_Time()
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
print("The Subtraction of two times: ")
T = Time(Hour1,Minute1,Seconds1)
T2 = Time(Hour2,Minute2,Seconds2)
T_A = T.Subtraction_of_two_times(Time(8,4,2))
T_A = T_A.Check_Fix()
T_A.Show_Time()
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
T = Time(Hour1,Minute1,Seconds1)
T_A = T.Convert_time_to_seconds()
print("Convert first time to seconds: ",T_A)
T2 = Time(Hour2,Minute2,Seconds2)
T_A2 = T2.Convert_time_to_seconds()
print("Convert second time to seconds: ",T_A2)
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
print("Convert first seconds to time : ")
T = T.Convert_seconds_to_time(T_A)
T = T.Check_Fix()
T.Show_Time()
print("Convert second seconds to time : ")
T = T.Convert_seconds_to_time(T_A2)
T = T.Check_Fix()
T.Show_Time()
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
print("World time(GMT) conversion to Tehran time : ")
T = Time(Hour1,Minute1,Seconds1)
T_A = T.World_time_conversion_to_Tehran_time()
T_A = T_A.Check_Fix()
T_A.Show_Time()