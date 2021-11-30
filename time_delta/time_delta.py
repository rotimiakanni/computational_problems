from os.path import realpath, join, dirname

from datetime import datetime, timedelta

'''
Link to problem: https://www.hackerrank.com/challenges/python-time-delta/problem

When users post an update on social media,such as a URL, 
image, status update etc., other users in their network are 
able to view this new post on their news feed. Users can 
also see exactly when the post was published, i.e, how many 
hours, minutes or seconds ago.

Since sometimes posts are published and viewed in different 
time zones, this can be confusing. You are given two timestamps 
of one such post that a user can see on his newsfeed in the 
following format:

Day dd Mon yyyy hh:mm:ss +xxxx

Here +xxxx represents the time zone. Your task is to print the 
absolute difference (in seconds) between them.

sample input:
2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000

sample output:
25200
88200

explanation:
In the first query, when we compare the time in UTC for both 
the time stamps, we see a difference of 7 hours. which is 7*3600
seconds or 25200 seconds.

Similarly, in the second query, time difference is 5 hours and 
30 minutes for time zone adjusting for that we have a difference 
of 1 day and 30 minutes. Or 
'''

class TimeStructure():
    def __init__(self, date_time):
        self.date_time = ' '.join(date_time[:5])
        self.time_zone = date_time[5]
        self.hour_diff = self.time_zone[1:3]
        self.min_diff = self.time_zone[3:]
        self.is_positive = True if self.time_zone[0] == '+' else False
        self.dt_obj = None
        
    def __str__(self):
        return self.date_time
    
    def __sub__(self, other):
        return self.dt_obj - other.dt_obj
        
    def set_date_time(self):
        self.dt_obj = datetime.strptime(self.date_time, '%a %d %b %Y %H:%M:%S')
        if not self.is_positive:
            self.dt_obj = self.dt_obj + timedelta(
                hours=int(self.hour_diff),
                minutes=int(self.min_diff))
        else:
            self.dt_obj = self.dt_obj - timedelta(
                hours=int(self.hour_diff),
                minutes=int(self.min_diff))
        return
    
    def get_seconds_diff(self, other):
        if self.dt_obj and other.dt_obj:
            total_seconds = (self.dt_obj - other.dt_obj).total_seconds()
            return total_seconds
        elif type(self.dt_obj) is not datetime.timedelta:
            raise TypeError('Method not available for Non-datetime Type object.')

# Complete the time_delta function below.
def time_delta(t1, t2):
    t1_dt = TimeStructure(t1.split())
    t1_dt.set_date_time()
    t2_dt = TimeStructure(t2.split())
    t2_dt.set_date_time()
    seconds_diff = int(t1_dt.get_seconds_diff(t2_dt))
    return str(abs(seconds_diff))
    
if __name__ == '__main__':
    fptr = open('res.txt', 'w')

    input_file = join(dirname(realpath(__file__)), 'sample.txt')
    ip_file = open(input_file)
    t = int(ip_file.readline())

    for t_itr in range(t):
        t1 = ip_file.readline().strip()

        t2 = ip_file.readline().strip()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
